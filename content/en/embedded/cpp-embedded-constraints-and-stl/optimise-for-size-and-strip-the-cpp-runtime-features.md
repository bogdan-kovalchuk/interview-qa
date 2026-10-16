---
id: emb-cppstl-0033
title: "What does a typical embedded C++ compile line look like?"
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

**`-Os` (size optimization) + a set of `-fno-*` flags that strip C++-runtime-heavy features + `-std=c++17`.**

This gives compact, deterministic code without exceptions, RTTI, unwind tables or thread-safe static guards.

Rule: know these flags by heart – a typical expectation at an embedded C++ interview.[^embeddedinterviewlab]

## Detailed explanation

TODO
