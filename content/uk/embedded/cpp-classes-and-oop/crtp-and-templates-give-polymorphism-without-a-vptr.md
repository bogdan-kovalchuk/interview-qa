---
id: emb-cppoop-0035
title: "Чи можна вибрати поліморфізм без RAM-оверхеду на vptr?"
description: "Так – CRTP (Curiously Recurring Template Pattern, compile-time) або просто templates/композиція."
track: embedded
section: cpp-classes-and-oop
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

**Так – CRTP (Curiously Recurring Template Pattern, compile-time) або просто templates/композиція.**

CRTP резолвить виклики статично через `static_cast` до похідного типу, тож об'єкт не містить vptr. Це ідеально, коли набір типів фіксований на етапі компіляції.

Правило: потрібен поліморфізм, але дорога RAM (random-access memory) на vptr × багато об'єктів -> бери CRTP замість virtual.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
