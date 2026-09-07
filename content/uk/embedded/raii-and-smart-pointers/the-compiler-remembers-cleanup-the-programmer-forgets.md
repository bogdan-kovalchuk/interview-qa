---
id: emb-raii-0020
title: "Чим RAII кращий за ручний init/deinit (таблиця відмінностей)?"
description: "RAII дає гарантію очищення, безпечний early return, один dtor замість повторів, автоматичний порядок знищення і нульовий runtime після inlining."
track: embedded
section: raii-and-smart-pointers
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
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

- **Гарантія очищення:** компілятор кличе dtor vs програміст мусить пам'ятати;
- **Error-шлях:** early return безпечний vs кожен вихід – шанс на баг;
- **Дублювання:** dtor написаний раз vs повтор на кожному виході;
- **Порядок:** автоматичне reverse-знищення vs ручні виклики у зворотному порядку;
- **Runtime:** часто нульовий після inlining, але це треба перевіряти на release-прапорцях.

Правило: RAII не додає можливостей – він прибирає цілий клас людських помилок.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
