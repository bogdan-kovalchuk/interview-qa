---
id: emb-tmplcx-0002
title: "Скільки інстанціацій template опиниться у бінарнику?"
description: "Рівно стільки, скільки РІЗНИХ типів реально використано."
track: embedded
section: templates-and-constexpr
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

**Рівно стільки, скільки РІЗНИХ типів реально використано.**

Якщо викликати `max<int>()` і `max<float>()` – у бінарнику буде дві інстанціації. Компілятор генерує код лише для фактично задіяних типів, не для «всіх можливих».

Правило: кожен унікальний набір template-аргументів = окрема копія коду у Flash.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
