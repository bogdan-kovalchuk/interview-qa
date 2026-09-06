---
id: emb-cppoop-0007
title: "Що таке RAII у контексті конструкторів/деструкторів?"
description: "RAII (Resource Acquisition Is Initialization): конструктор захоплює/налаштовує ресурс, деструктор автоматично звільняє його при виході з scope."
track: embedded
section: cpp-classes-and-oop
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

**RAII (Resource Acquisition Is Initialization): конструктор захоплює/налаштовує ресурс, деструктор автоматично звільняє його при виході з scope.**

Наприклад: ctor вмикає clock і конфігурує периферію, dtor вимикає clock або звільняє DMA (direct memory access) канал. Немає шансу забути деініціалізацію – компілятор вставляє виклик dtor.

Правило: прив'язуй lifetime ресурсу (clock, DMA, lock) до lifetime об'єкта – це і є RAII.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
