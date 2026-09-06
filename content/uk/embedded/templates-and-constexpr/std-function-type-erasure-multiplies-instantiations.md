---
id: emb-tmplcx-0017
title: "Trap: чому `std::function` може різко роздути Flash?"
description: "std::function – template-heavy type erasure; різні сигнатури й callable-типи можуть породити багато окремого коду."
track: embedded
section: templates-and-constexpr
level: junior
type: pitfall
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

`std::function` – template-heavy type erasure; різні сигнатури й callable-типи можуть породити багато окремого коду.

Кожна сигнатура – окрема інстанціація type-erasure машинерії, а реалізація може тягнути додатковий runtime-код.

Захист: для простих callback'ів часто достатньо function pointer + `void* context`. На flash-обмежених MCU перевіряй `std::function` через linker map.[^embeddedinterviewlab]

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
