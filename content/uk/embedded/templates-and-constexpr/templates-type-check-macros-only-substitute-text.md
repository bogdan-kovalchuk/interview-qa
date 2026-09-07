---
id: emb-tmplcx-0022
title: "Templates vs макроси: ключові відмінності?"
description: "Templates: повний type checking, аргументи раз, дебаг, constexpr-обчислення."
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

**Templates: повний type checking, аргументи раз, дебаг, constexpr-обчислення. Макроси: текст, double evaluation, лише preprocessor output.**

Ціна: templates ризикують code bloat (копія на інстанціацію) і повільнішим білдом; макроси – швидкі й портативні на C89, але небезпечні.

Правило: у C++ обирай templates для типобезпеки; макроси лишай для того, що шаблон не вміє (`#`/`##`, conditional compilation).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
