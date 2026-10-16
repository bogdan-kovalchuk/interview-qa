---
id: emb-cppstl-0029
title: "Чому `enum class` кращий за звичайний `enum` для статусів?"
track: embedded
section: cpp-embedded-constraints-and-stl
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
---

## Short answer

**Scoped і strongly-typed: не конвертується неявно в `int` і не засмічує namespace.**

`Status::Ok` не сплутати з іншим enum'ом, і `if (status)` не скомпілюється випадково. Це ловить цілий клас помилок порівняння/перетворення.

Правило: для кодів помилок і станів використовуй `enum class`, а не голий `enum`.[^embeddedinterviewlab]

## Detailed explanation

TODO
