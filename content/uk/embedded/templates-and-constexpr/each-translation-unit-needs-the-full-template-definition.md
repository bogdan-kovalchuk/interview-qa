---
id: emb-tmplcx-0028
title: "Чому шаблони зазвичай header-only?"
description: "Компілятору потрібне повне визначення шаблону в кожному TU (translation unit), щоб інстанціювати його під конкретні типи."
track: embedded
section: templates-and-constexpr
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

**Компілятору потрібне повне визначення шаблону в кожному TU (translation unit), щоб інстанціювати його під конкретні типи.**

Якщо визначення сховати в `.cpp`, інші translation units не зможуть згенерувати потрібну інстанціацію -> linker error. Тому шаблони кладуть у заголовки.

Правило: визначення шаблонів – у header; для контролю інстанціацій використовуй `extern template`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
