---
id: emb-cppstl-0019
title: "Які ключові прапорці компіляції для embedded C++?"
description: "-fno-exceptions, -fno-rtti, -fno-threadsafe-statics, -fno-use-cxa-atexit, -fno-unwind-tables."
track: embedded
section: cpp-embedded-constraints-and-stl
level: junior
type: concept
tags: []
status: published
updated: 2026-09-06
content_revision: 1
reconciled_with:
  en: 2
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

**`-fno-exceptions`, `-fno-rtti`, `-fno-threadsafe-statics`, `-fno-use-cxa-atexit`, `-fno-unwind-tables`.**

Вони прибирають: винятки, RTTI, mutex на ініціалізації static (pthread), реєстрацію dtor через `__cxa_atexit`, та `.eh_frame`-таблиці. Часто з `-Os` і `-std=c++17`.

Правило: ці прапорці роблять C++ детермінованим і компактним на голому залізі.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
