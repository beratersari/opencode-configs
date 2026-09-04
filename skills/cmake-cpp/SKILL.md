---
name: cmake-cpp
description: C++ build-system review. Load when the diff touches CMakeLists.txt, CMakePresets.json, Makefile, meson.build, compile_commands.json, conan, vcpkg, or *.vcxproj. Do not load when no build file changed. Dialect skill already loaded this turn is a hard ceiling.
license: MIT
compatibility: opencode
---

# C++ build files

Review **this change** for a build that will fail or silently
change the language dialect. Project rules still win.

## Look for

- `add_executable` / `add_library` listing a file that is not
  in this MR and is not on the target branch (configure/build
  fail on a clean tree).
- `CMAKE_CXX_STANDARD` (or `-std=`) that disagrees with
  `AGENTS.md` / `CODE_REVIEW.md`, or that is dropped.
- `CMAKE_CXX_STANDARD` without `CMAKE_CXX_STANDARD_REQUIRED`
  when the project claims a floor.
- A new source file in the MR that is never added to a target.
- `include_directories` / global flags instead of
  `target_include_directories` / `target_compile_features`
  only when that actually breaks an install or a second target.
- `file(GLOB` sources: a newly added `.cpp` will not build
  until cmake is re-run; prefer an explicit list for libraries.
- Install rules that omit a public header this MR added.
- Sanitizer / warning flags that apply to only one target by
  accident, or that are forced on MSVC with GCC syntax.

## Impact

A missing source on a target is a silent “works on my machine”
if the author already had an old cmake cache. Say so.

## Do not flag

- `cmake_minimum_required` older than latest unless it actually
  miscompiles this change.
- Style of CMake modern vs classic when the build is correct.
