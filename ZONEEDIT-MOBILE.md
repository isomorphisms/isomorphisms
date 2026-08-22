# ZoneEdit Mobile

A deliberately small Android wrapper around the ZoneEdit control panel.

## Why this shape

ZoneEdit does not publish a general DNS-record-management API. It does publish narrowly scoped Dynamic DNS and ACME TXT endpoints, but those are not enough to implement a complete native DNS editor. This app therefore keeps ZoneEdit itself as the authority for authentication and record editing instead of scraping its forms or storing a ZoneEdit password.

The app:

- opens `https://cp.zoneedit.com/login.php` directly;
- keeps ZoneEdit navigation in the app;
- opens non-ZoneEdit links in the normal browser;
- lets Android/WebView handle cookies and autofill;
- injects only a small mobile stylesheet for larger controls, responsive images, and horizontally scrollable tables;
- permits HTTPS only and disables WebView file/content access.

## Build

GitHub Actions builds a debug APK on pushes to `zoneedit-mobile` and on pull requests.

Locally, with Android SDK 35 and Gradle 8.9 installed:

```sh
gradle :app:assembleDebug
```

The APK is written to:

```text
app/build/outputs/apk/debug/app-debug.apk
```

## Next useful step

Try the APK against the real ZoneEdit control panel on a phone. The useful question is whether the CSS injection makes the existing forms comfortable enough. If individual ZoneEdit pages still fight the phone layout, fix those selectors specifically rather than building a second DNS-management system.
