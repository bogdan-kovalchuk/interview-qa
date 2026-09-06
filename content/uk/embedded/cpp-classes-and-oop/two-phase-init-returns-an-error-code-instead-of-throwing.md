---
id: emb-cppoop-0011
title: "Як ініціалізувати об'єкт, коли exceptions вимкнені (`-fno-exceptions`)?"
description: "Two-phase init: тривіальний конструктор + окремий метод init(), що повертає код помилки."
track: embedded
section: cpp-classes-and-oop
level: junior
type: concept
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

**Two-phase init: тривіальний конструктор + окремий метод `init()`, що повертає код помилки.**

Конструктор не може сигналізувати про збій без exceptions, тому «важку» ініціалізацію (що може впасти) виносять у `err_t init()`, який викликач перевіряє.

Правило: на цілях без exceptions конструктор лишай простим (no-fail), а fallible-логіку – в окремий init з return code.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
