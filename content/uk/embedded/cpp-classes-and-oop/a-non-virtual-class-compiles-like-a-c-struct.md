---
id: emb-cppoop-0001
title: "Що означає «zero-overhead abstraction» для C++ класу?"
description: "Non-virtual клас може компілюватися у такий самий машинний код, як C-struct із вільними функціями, якщо оптимізатор бачить тіло методів."
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

**Non-virtual клас може компілюватися у такий самий машинний код, як C-struct із вільними функціями, якщо оптимізатор бачить тіло методів.**

Нестатична member-функція фактично отримує неявний `this`; без `virtual` немає vtable/vptr, а прості методи зазвичай інлайняться. На `-O0` або через окремі translation units виклик може лишитися звичайним call.

Правило: інкапсуляція через клас у embedded зазвичай безкоштовна в release-збірці, поки немає virtual і зайвого стану.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
