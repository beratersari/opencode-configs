---
name: vue
description: Vue skill. Load when the diff changes *.vue or files that import vue / @vue/*. Do not load for React-only trees.
license: MIT
compatibility: opencode
---

# Vue

Project rules still win. Honor Vue 2 vs 3 from package.json.

## Look for

- Mutating a prop.
- `v-html` with user data (XSS).
- Watcher missing `flush` / deep when this change nests state.
- Vue 3: `ref` unwrapped incorrectly in `reactive`, or lost
  reactivity after destructure without `toRefs`.
- Vue 2: adding a root field without `Vue.set` / `this.$set`.
- Leaked listener: `onMounted` addEventListener without
  `onBeforeUnmount` remove.

## Do not flag

- Options API in a Vue 2 or mixed codebase.
- Suggesting `<script setup>` as a rewrite.
