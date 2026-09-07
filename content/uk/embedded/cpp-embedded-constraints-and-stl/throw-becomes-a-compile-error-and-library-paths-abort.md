---
id: emb-cppstl-0002
title: "Trap: що відбувається з `throw` і `try`/`catch` при `-fno-exceptions`?"
description: "У власному коді throw/try/catch зазвичай стають compile error; library-шляхи, які мали кинути виняток, часто завершуються abort()."
track: embedded
section: cpp-embedded-constraints-and-stl
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
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

<span class="warn">У власному коді `throw`/`try`/`catch` зазвичай стають compile error; library-шляхи, які мали кинути виняток, часто завершуються `abort()`.</span>

Це не «магічне прибирання» помилок: шлях із `vector::at()` out-of-range може аварійно зупинити систему замість обробленого винятку.

Захист: аудитуй throwing API (application programming interface) стандартної бібліотеки й замінюй їх на явні перевірки/статуси.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
