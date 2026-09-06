---
id: emb-cppstl-0033
title: "Як виглядає типовий рядок компіляції embedded C++?"
description: "-Os (оптимізація за розміром) + набір -fno-, що прибирають C++-runtime-важкі фічі, + -std=c++17."
track: embedded
section: cpp-embedded-constraints-and-stl
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-06
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання і відповіді; відповідь незалежно не перевірена."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C++; freestanding і вендорські тулчейни можуть відрізнятися."
---

## Short answer

```text
arm-none-eabi-g++ -mcpu=cortex-m4 -mthumb -Os \
  -fno-exceptions -fno-rtti -fno-threadsafe-statics \
  -fno-use-cxa-atexit -fno-unwind-tables \
  -std=c++17 -Wall -Werror
```

**`-Os` (оптимізація за розміром) + набір `-fno-*`, що прибирають C++-runtime-важкі фічі, + `-std=c++17`.**

Це дає компактний детермінований код без винятків, RTTI, unwind-таблиць і thread-safe static guard'ів.

Правило: знати ці прапорці напам'ять – типове очікування на embedded C++ інтерв'ю.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
