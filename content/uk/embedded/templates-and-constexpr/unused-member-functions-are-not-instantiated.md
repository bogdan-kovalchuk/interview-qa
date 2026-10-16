---
id: emb-tmplcx-0032
title: "Чи генерує компілятор код для невикористаних member-функцій шаблону?"
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

**Зазвичай ні – при неявній інстанціації class template генеруються лише member-функції, які реально потрібні.**

Це обмежує bloat: якщо у `CircularBuffer<T,N>` не викликати `pop()`, його код зазвичай не потрапить у Flash для цієї інстанціації. Винятки: explicit instantiation, virtual-функції та інші ODR-use сценарії можуть змусити згенерувати більше.

Правило: невикористані методи шаблону часто безкоштовні, але перевіряй linker map для template-heavy коду.[^embeddedinterviewlab]

## Detailed explanation

TODO
