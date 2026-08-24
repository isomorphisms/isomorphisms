# Branch project boards

This repository owns the account-level synchronization of live development branches into three user GitHub Projects:

- Rusty Tool Shed
- Math Toy Box
- Playroom

The source of truth is `.github/branch-boards.tsv`. A repository belongs to exactly one board. Every branch other than that repository's default branch is represented unless it is fully merged into the default branch or explicitly listed in `.github/branch-board-ignore.tsv`.

Cards are GitHub Project draft issues, not repository issues. The body carries a stable `branch-board-key` marker plus repository, branch, head commit, open PR, and CI state. The synchronizer only edits or deletes draft items carrying its marker; hand-written project items are left alone.

When a branch is deleted, fully merged, reclassified to another board, or ignored, its managed card disappears on the next run. The synchronizer does not impose priority or reorder cards.

## Authentication

GitHub's repository `GITHUB_TOKEN` cannot edit user Projects. Add a repository secret named `PROJECTS_TOKEN` containing a classic personal access token with `project` and `repo` scopes. The workflow uses that token only through `gh` to read repositories and mutate the three Projects.

## Running

The workflow runs hourly and after synchronization code/config lands on `master`. `workflow_dispatch` can also run it manually; choose dry-run to print intended mutations without changing the Projects.
