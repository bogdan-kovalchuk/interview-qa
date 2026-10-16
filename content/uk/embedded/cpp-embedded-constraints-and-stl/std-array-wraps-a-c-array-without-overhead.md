---
id: emb-cppstl-0011
title: "Чим `std::array` кращий за сирий C-масив?"
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

**Zero-overhead обгортка над C-масивом з `.size()`, `.at()` (з bounds checking) і сумісністю з ``.**

Він не decay-иться у вказівник при передачі, знає свій розмір і працює з `std::sort`/`std::find`. Розмір і layout ідентичні C-масиву.

Правило: у C++ embedded `std::array` повністю заміняє `T[]` як дефолтний контейнер.[^embeddedinterviewlab]

## Detailed explanation

TODO
