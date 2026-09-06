---
name: ios
description: Apple iOS / UIKit skill. Load when the diff changes Info.plist, *.xib, *.storyboard, or iOS target Swift under an .xcodeproj.
license: MIT
compatibility: opencode
---

# iOS

Project rules still win. Honor the deployment target.

## Look for

- UIKit work off the main thread.
- Retain cycle (`delegate` strong, closure capturing `self`).
- Info.plist usage string missing for a privacy API this
  change calls (camera, photos, location, tracking).
- ATS / HTTP exception added without need.
- Keychain / UserDefaults for a secret that should be
  Keychain (or the reverse of the project's existing split).
- Background task that never ends (`beginBackgroundTask`).

## Do not flag

- SwiftUI vs UIKit as a rewrite.
- Suggesting APIs above the deployment target.
