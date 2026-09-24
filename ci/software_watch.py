#!/usr/bin/env python3
"""Track upstream software heads/releases and refresh the public software index."""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any

FIELDS = [
    "id",
    "repository",
    "branch",
    "release_policy",
    "asset_regex",
    "release_link_text",
    "current_release",
    "source_sha",
]


class WatchError(RuntimeError):
    pass


@dataclass(frozen=True)
class Release:
    tag: str
    name: str
    prerelease: bool
    html_url: str
    asset_name: str
    asset_url: str


def read_manifest(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if reader.fieldnames != FIELDS:
            raise WatchError(
                f"{path}: expected header {FIELDS!r}, got {reader.fieldnames!r}"
            )
        rows = list(reader)

    seen: set[str] = set()
    for row in rows:
        identifier = row["id"]
        if not identifier or identifier in seen:
            raise WatchError(f"{path}: duplicate or empty id {identifier!r}")
        seen.add(identifier)
        if row["release_policy"] not in {"stable", "any"}:
            raise WatchError(
                f"{path}: {identifier}: release_policy must be stable or any"
            )
        try:
            re.compile(row["asset_regex"])
        except re.error as error:
            raise WatchError(
                f"{path}: {identifier}: invalid asset_regex: {error}"
            ) from error
        if not re.fullmatch(r"[0-9a-f]{40}", row["source_sha"]):
            raise WatchError(
                f"{path}: {identifier}: source_sha must be a full Git SHA"
            )
        if not row["current_release"]:
            raise WatchError(f"{path}: {identifier}: current_release is empty")
    return rows


def write_manifest(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=FIELDS, delimiter="\t", lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows)


def github_get(path: str) -> Any:
    api_root = os.environ.get("GITHUB_API_URL", "https://api.github.com").rstrip("/")
    request = urllib.request.Request(
        f"{api_root}/{path.lstrip('/')}",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "isomorphisms-software-watch",
        },
    )
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        request.add_header("Authorization", f"Bearer {token}")

    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.load(response)
    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8", "replace")
        raise WatchError(f"GitHub API {error.code} for {path}: {body}") from error
    except urllib.error.URLError as error:
        raise WatchError(f"GitHub API request failed for {path}: {error}") from error


def select_release(row: dict[str, str], releases: list[dict[str, Any]]) -> Release | None:
    pattern = re.compile(row["asset_regex"])

    candidates: list[tuple[str, Release]] = []
    for item in releases:
        if item.get("draft"):
            continue
        if row["release_policy"] == "stable" and item.get("prerelease"):
            continue

        matches = [
            asset
            for asset in item.get("assets", [])
            if pattern.fullmatch(str(asset.get("name", "")))
        ]
        if len(matches) > 1:
            names = ", ".join(str(asset.get("name")) for asset in matches)
            raise WatchError(
                f"{row['id']}: release {item.get('tag_name')} has multiple matching assets: {names}"
            )
        if not matches:
            continue

        asset = matches[0]
        tag = str(item.get("tag_name") or "")
        if not tag:
            raise WatchError(f"{row['id']}: release is missing tag_name")
        name = str(item.get("name") or tag)
        html_url = str(item.get("html_url") or "")
        asset_name = str(asset.get("name") or "")
        asset_url = str(asset.get("browser_download_url") or "")
        if not html_url or not asset_name or not asset_url:
            raise WatchError(f"{row['id']}: release {tag} has incomplete URLs")

        timestamp = str(item.get("published_at") or item.get("created_at") or "")
        candidates.append(
            (
                timestamp,
                Release(
                    tag=tag,
                    name=name,
                    prerelease=bool(item.get("prerelease")),
                    html_url=html_url,
                    asset_name=asset_name,
                    asset_url=asset_url,
                ),
            )
        )

    if not candidates:
        return None
    return max(candidates, key=lambda pair: pair[0])[1]


def fetch_upstream(row: dict[str, str]) -> tuple[str, Release | None]:
    repository = row["repository"]
    branch = urllib.parse.quote(row["branch"], safe="")
    branch_data = github_get(f"repos/{repository}/branches/{branch}")
    source_sha = str(branch_data.get("commit", {}).get("sha", ""))
    if not re.fullmatch(r"[0-9a-f]{40}", source_sha):
        raise WatchError(f"{row['id']}: upstream branch did not return a full SHA")

    releases = github_get(f"repos/{repository}/releases?per_page=100")
    if not isinstance(releases, list):
        raise WatchError(f"{row['id']}: releases response is not a list")
    return source_sha, select_release(row, releases)


def begin_marker(identifier: str) -> str:
    return f"<!-- software-release:{identifier}:begin -->"


def end_marker(identifier: str) -> str:
    return f"<!-- software-release:{identifier}:end -->"


def release_block(row: dict[str, str], release: Release) -> str:
    suffix = " — prerelease" if release.prerelease else ""
    source_url = f"https://github.com/{row['repository']}"
    return (
        f"**{release.name}**{suffix} — "
        f"[Download APK]({release.asset_url}) · "
        f"[{row['release_link_text']}]({release.html_url}) · "
        f"[Source]({source_url})"
    )


def extract_block(text: str, identifier: str) -> str:
    start = begin_marker(identifier)
    finish = end_marker(identifier)
    if text.count(start) != 1 or text.count(finish) != 1:
        raise WatchError(f"README: expected exactly one marker pair for {identifier}")
    before, rest = text.split(start, 1)
    body, after = rest.split(finish, 1)
    del before, after
    return body.strip("\n")


def replace_block(text: str, identifier: str, body: str) -> str:
    start = begin_marker(identifier)
    finish = end_marker(identifier)
    if text.count(start) != 1 or text.count(finish) != 1:
        raise WatchError(f"README: expected exactly one marker pair for {identifier}")
    prefix, rest = text.split(start, 1)
    old_body, suffix = rest.split(finish, 1)
    del old_body
    return f"{prefix}{start}\n{body.rstrip()}\n{finish}{suffix}"


def verify_local(manifest_path: Path, readme_path: Path) -> None:
    rows = read_manifest(manifest_path)
    text = readme_path.read_text(encoding="utf-8")

    for row in rows:
        block = extract_block(text, row["id"])
        source_url = f"https://github.com/{row['repository']}"
        if source_url not in block:
            raise WatchError(f"README: {row['id']}: source URL missing from release block")

        tag = row["current_release"]
        if tag == "-":
            if "Download APK" in block:
                raise WatchError(
                    f"README: {row['id']}: current_release is '-' but APK is advertised"
                )
        else:
            if f"/releases/tag/{tag}" not in block:
                raise WatchError(
                    f"README: {row['id']}: release block does not point at {tag}"
                )
            if "Download APK" not in block:
                raise WatchError(f"README: {row['id']}: release has no APK link")


def update(
    manifest_path: Path,
    readme_path: Path,
    report_path: Path | None,
) -> bool:
    rows = read_manifest(manifest_path)
    text = readme_path.read_text(encoding="utf-8")
    changes: list[str] = []
    readme_changed = False

    for row in rows:
        old_source = row["source_sha"]
        old_release = row["current_release"]
        new_source, release = fetch_upstream(row)

        if new_source != old_source:
            changes.append(
                f"- **{row['id']} source:** {old_source[:12]} -> {new_source[:12]}"
            )
            row["source_sha"] = new_source

        if release is None:
            if old_release != "-":
                raise WatchError(
                    f"{row['id']}: tracked release {old_release} exists locally but no matching upstream release was found"
                )
            continue

        expected = release_block(row, release)
        current = extract_block(text, row["id"])
        if release.tag != old_release:
            changes.append(
                f"- **{row['id']} release:** {old_release} -> {release.tag}"
            )
            row["current_release"] = release.tag
        if current != expected:
            text = replace_block(text, row["id"], expected)
            readme_changed = True
            if release.tag == old_release:
                changes.append(
                    f"- **{row['id']} release metadata:** refreshed {release.tag}"
                )

    changed = bool(changes) or readme_changed
    if changed:
        write_manifest(manifest_path, rows)
        if readme_changed:
            readme_path.write_text(text, encoding="utf-8")

    verify_local(manifest_path, readme_path)

    if report_path is not None:
        report_path.parent.mkdir(parents=True, exist_ok=True)
        if changes:
            body = "# Upstream software refresh\n\n" + "\n".join(changes) + "\n"
        else:
            body = "# Upstream software refresh\n\nNo upstream changes detected.\n"
        report_path.write_text(body, encoding="utf-8")

    return changed


def self_test() -> None:
    row = {
        "id": "demo",
        "repository": "owner/repo",
        "branch": "main",
        "release_policy": "stable",
        "asset_regex": r"^demo-[0-9.]+\.apk$",
        "release_link_text": "Release notes",
        "current_release": "v1",
        "source_sha": "a" * 40,
    }
    releases = [
        {
            "tag_name": "v2-rc",
            "name": "Demo 2 RC",
            "draft": False,
            "prerelease": True,
            "published_at": "2026-09-02T00:00:00Z",
            "html_url": "https://example/v2-rc",
            "assets": [
                {
                    "name": "demo-2.0.apk",
                    "browser_download_url": "https://example/demo-2.0.apk",
                }
            ],
        },
        {
            "tag_name": "v1",
            "name": "Demo 1",
            "draft": False,
            "prerelease": False,
            "published_at": "2026-09-01T00:00:00Z",
            "html_url": "https://example/v1",
            "assets": [
                {
                    "name": "demo-1.0.apk",
                    "browser_download_url": "https://example/demo-1.0.apk",
                }
            ],
        },
    ]
    selected = select_release(row, releases)
    assert selected is not None and selected.tag == "v1"

    row_any = dict(row)
    row_any["release_policy"] = "any"
    selected_any = select_release(row_any, releases)
    assert selected_any is not None and selected_any.tag == "v2-rc"

    duplicate = [dict(releases[1])]
    duplicate[0]["assets"] = [
        {"name": "demo-1.0.apk", "browser_download_url": "https://example/a"},
        {"name": "demo-1.1.apk", "browser_download_url": "https://example/b"},
    ]
    try:
        select_release(row, duplicate)
    except WatchError:
        pass
    else:
        raise AssertionError("multiple matching APKs must be rejected")

    sample = (
        "before\n"
        + begin_marker("demo")
        + "\nold\n"
        + end_marker("demo")
        + "\nafter\n"
    )
    replaced = replace_block(sample, "demo", "new")
    assert extract_block(replaced, "demo") == "new"

    try:
        extract_block("no markers", "demo")
    except WatchError:
        pass
    else:
        raise AssertionError("missing markers must be rejected")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--manifest", type=Path, default=Path("tracked-software.tsv")
    )
    parser.add_argument("--readme", type=Path, default=Path("README.md"))
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("verify-local")
    sub.add_parser("self-test")
    refresh = sub.add_parser("update")
    refresh.add_argument("--report", type=Path)

    arguments = parser.parse_args()

    try:
        if arguments.command == "verify-local":
            verify_local(arguments.manifest, arguments.readme)
            print("PASS local software index")
            return 0
        if arguments.command == "self-test":
            self_test()
            print("PASS software watch self-test")
            return 0
        if arguments.command == "update":
            changed = update(
                arguments.manifest,
                arguments.readme,
                arguments.report,
            )
            print("CHANGED" if changed else "UNCHANGED")
            return 0
        raise AssertionError(arguments.command)
    except WatchError as error:
        print(f"FAIL {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
