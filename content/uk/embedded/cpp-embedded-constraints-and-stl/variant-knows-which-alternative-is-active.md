---
id: emb-cppstl-0032
title: "Що таке `std::variant` і чим він кращий за union?"
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

**Type-safe union (C++17): знає, який саме тип зараз активний, і не дає прочитати інший.**

Сирий `union` не відстежує активний член – читання «не того» поля це UB (undefined behavior). `std::variant` + `std::visit` роблять це безпечно, без heap.

Захист: visitor має покривати всі альтернативи; некоректний visitor зазвичай ловиться на компіляції, а не в runtime.[^embeddedinterviewlab]

## Detailed explanation

TODO
