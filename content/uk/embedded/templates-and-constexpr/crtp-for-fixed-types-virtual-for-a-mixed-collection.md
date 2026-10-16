---
id: emb-tmplcx-0031
title: "Коли обирати CRTP, а коли virtual у шаблонному дизайні?"
track: embedded
section: templates-and-constexpr
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
---

## Short answer

**CRTP – фіксовані типи, performance-critical (ISR, tight loops), без virtual dispatch і vtable на об'єкт.**

Virtual – потрібен runtime-поліморфізм: гетерогенні колекції, плагіни, динамічне завантаження драйверів. CRTP не дозволяє тримати різні типи в одному масиві без додаткової type-erasure обгортки.

Правило: відомі типи + швидкість -> CRTP; різні типи в runtime -> virtual.[^embeddedinterviewlab]

## Detailed explanation

TODO
