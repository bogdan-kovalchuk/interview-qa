---
id: emb-tmplcx-0028
title: "Чому шаблони зазвичай header-only?"
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

**Компілятору потрібне повне визначення шаблону в кожному TU (translation unit), щоб інстанціювати його під конкретні типи.**

Якщо визначення сховати в `.cpp`, інші translation units не зможуть згенерувати потрібну інстанціацію -> linker error. Тому шаблони кладуть у заголовки.

Правило: визначення шаблонів – у header; для контролю інстанціацій використовуй `extern template`.[^embeddedinterviewlab]

## Detailed explanation

TODO
