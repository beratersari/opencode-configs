---
name: i18n
description: Internationalization skill. Load when changing user-visible strings, locales, RTL, dates, or translation files. Use for implement, debug, or review.
license: MIT
compatibility: opencode
---

# i18n

## Rules

- New user-visible English (or any language) hardcoded
  when the project already uses a message catalog.
- Concatenated sentences that break translator word
  order (`"Hello " + name + ", you have " + n`).
- Date/number/currency without a locale.
- Plural rules using `n == 1` only.
- RTL: padding/left icons that assume LTR on a new
  layout.
- Encoding: assume UTF-8; do not store user text in
  Latin-1.

## Do not

- Demand i18n in a single-locale internal tool with
  no catalog.
