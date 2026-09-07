---
id: emb-raii-0009
title: "Як передати володіння ресурсом через `unique_ptr`?"
description: "Через std::move() – копіювання заборонене, передача явна."
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

**Через `std::move()` – копіювання заборонене, передача явна.**

`auto b = std::move(a);` переносить власність: `a` стає порожнім, `b` тепер відповідає за звільнення. Це робить ownership видимим у коді.

Правило: `unique_ptr` – move-only; явний `std::move` документує, хто тепер власник.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
