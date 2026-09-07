---
id: emb-raii-0025
title: "Що таке rule of three / five / zero?"
description: "Якщо клас керує ресурсом – визнач (або видали) усі спецфункції разом."
track: embedded
section: raii-and-smart-pointers
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

**Якщо клас керує ресурсом – визнач (або видали) усі спецфункції разом.**

Rule of three: dtor, copy ctor, copy assign. Rule of five (C++11): + move ctor, move assign. Rule of zero: не керуй ресурсами вручну – нехай члени-RAII (smart pointers, guards) роблять це, і не пиши жодної спецфункції.

Правило: прагни rule of zero; якщо керуєш ресурсом сам – не лишай дефолтні copy, що дадуть double-free.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
