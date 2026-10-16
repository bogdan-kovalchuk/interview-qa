---
id: emb-cppstl-0027
title: "Чому в embedded уникають `<iostream>` на користь `printf`?"
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

<span class="warn">`<iostream>` може тягнути locale, heap-буфери, глобальну ініціалізацію й десятки КБ Flash.</span>

`std::cout` ініціалізує важку інфраструктуру ще до `main()`; на MCU це часто неприйнятно. `printf` (особливо урізаний/nano) або власний trace backend зазвичай значно легші.

Правило: для логів на MCU – `printf`/власний trace backend, не `iostream`.[^embeddedinterviewlab]

## Detailed explanation

TODO
