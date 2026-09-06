---
id: emb-cppoop-0036
title: "Композиція чи успадкування: що легше тестувати і чому?"
description: "Композицію: компоненти-члени можна підмінити mock'ами незалежно."
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

**Композицію: компоненти-члени можна підмінити mock'ами незалежно.**

При успадкуванні для тесту похідного треба мокати/тягнути весь base (тісне зчеплення). Композиція дозволяє інжектувати фейкові компоненти (через шаблон чи вказівник) і тестувати юніт ізольовано.

Правило: дизайн на композиції – це ще й дизайн на тестованість.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
