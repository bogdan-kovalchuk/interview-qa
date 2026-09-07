---
id: emb-cppoop-0006
title: "Навіщо потрібен member initialization list у конструкторі?"
description: "Ініціалізує members до входу в тіло конструктора – єдиний спосіб для const і reference членів."
track: embedded
section: cpp-classes-and-oop
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
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

## Question code

```c
Gpio(uint32_t base, uint8_t pin)
  : odr_{(volatile uint32_t*)(base + 0x14)}, pin_{pin} {}
```

## Short answer

**Ініціалізує members до входу в тіло конструктора – єдиний спосіб для `const` і reference членів.**

`const uint8_t pin_` не можна присвоїти в тілі; його треба ініціалізувати у списку. Це також ефективніше: пряма ініціалізація замість «default + присвоєння».

Правило: ініціалізуй усі члени у списку, у порядку їх оголошення в класі.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
