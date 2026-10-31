---
id: emb-cemb-0021
title: "What is the difference between C-style and C++ casts?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
---

## Short answer

**A C-style cast** looks like `(T)x` and can perform several kinds of conversion at once: numeric conversion, removing `const`, pointer reinterpretation. Because of this it is short but imprecise and can hide a dangerous operation.[^dou-embedded-interview]

In C++ it is better to use explicit casts: `static_cast` for ordinary safer conversions, `const_cast` only for changing cv-qualifiers, `reinterpret_cast` for low-level reinterpretation, `dynamic_cast` for runtime-checked casts in polymorphic classes. They are longer, but they show intent and are easier to find in code.

## Detailed explanation

TODO
