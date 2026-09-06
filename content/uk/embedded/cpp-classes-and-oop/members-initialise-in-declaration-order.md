---
id: emb-cppoop-0032
title: "Який порядок ініціалізації членів у конструкторі?"
description: "Члени ініціалізуються у порядку ОГОЛОШЕННЯ в класі, а не в порядку запису в init list."
track: embedded
section: cpp-classes-and-oop
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

**Члени ініціалізуються у порядку ОГОЛОШЕННЯ в класі, а не в порядку запису в init list.**

Тому якщо `b_` у списку йде перед `a_`, але оголошений після – реально `a_` ініціалізується першим. Залежність `b_{a_}` при неправильному порядку оголошення дасть читання неініціалізованого `a_`.

Захист: пиши init list у тому ж порядку, що й оголошення членів; `-Wreorder` попередить.[^embeddedinterviewlab]

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
