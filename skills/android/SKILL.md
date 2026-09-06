---
name: android
description: Android skill. Load when the diff changes AndroidManifest.xml, *.gradle with com.android, res/, or *.kt/*.java under an app/src/main tree.
license: MIT
compatibility: opencode
---

# Android

Project rules still win. Honor `minSdk` / `targetSdk`.

## Look for

- Work on the main thread (network / disk) this change added.
- Context leak: Activity/View stored on a singleton or
  static. Prefer `applicationContext` when that is enough.
- Missing permission in the manifest for an API this change
  calls, or using a permission without a runtime request
  when `targetSdk` requires it.
- Exported component (`android:exported`) that should not
  be. Intent extras trusted as if they were internal.
- Lifecycle: callback after `onDestroy`; coroutine without
  `lifecycleScope` / `viewModelScope`.

## Do not flag

- XML vs Compose as a rewrite.
- Suggesting APIs above `minSdk` without a compat check.
