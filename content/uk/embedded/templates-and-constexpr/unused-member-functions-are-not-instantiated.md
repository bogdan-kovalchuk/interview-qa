---
id: emb-tmplcx-0032
title: "Чи генерує компілятор код для невикористаних member-функцій шаблону?"
description: "Зазвичай ні – при неявній інстанціації class template генеруються лише member-функції, які реально потрібні."
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

**Зазвичай ні – при неявній інстанціації class template генеруються лише member-функції, які реально потрібні.**

Це обмежує bloat: якщо у `CircularBuffer<T,N>` не викликати `pop()`, його код зазвичай не потрапить у Flash для цієї інстанціації. Винятки: explicit instantiation, virtual-функції та інші ODR-use сценарії можуть змусити згенерувати більше.

Правило: невикористані методи шаблону часто безкоштовні, але перевіряй linker map для template-heavy коду.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
