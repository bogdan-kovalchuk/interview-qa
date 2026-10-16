---
id: emb-cppstl-0022
title: "Trap: `vector::at()` з out-of-bounds при `-fno-exceptions` – що буде?"
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

<span class="warn">У багатьох embedded toolchain замість винятку `std::out_of_range` library-шлях завершується `abort()` або іншим fatal handler.</span>

`-fno-exceptions` не прибирає bounds check; змінюється реакція на провал. На MCU це часто виглядає як аварійна зупинка або HardFault без нормальної діагностики.

Захист: використовуй `std::array` або власну bounds-checking обгортку, що логує дані перед зупинкою.[^embeddedinterviewlab]

## Detailed explanation

TODO
