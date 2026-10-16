---
id: emb-cppstl-0033
title: "Як виглядає типовий рядок компіляції embedded C++?"
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

## Question code

```text
arm-none-eabi-g++ -mcpu=cortex-m4 -mthumb -Os \
  -fno-exceptions -fno-rtti -fno-threadsafe-statics \
  -fno-use-cxa-atexit -fno-unwind-tables \
  -std=c++17 -Wall -Werror
```

## Short answer

**`-Os` (оптимізація за розміром) + набір `-fno-*`, що прибирають C++-runtime-важкі фічі, + `-std=c++17`.**

Це дає компактний детермінований код без винятків, RTTI, unwind-таблиць і thread-safe static guard'ів.

Правило: знати ці прапорці напам'ять – типове очікування на embedded C++ інтерв'ю.[^embeddedinterviewlab]

## Detailed explanation

TODO
