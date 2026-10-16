---
id: emb-cppstl-0019
title: "What are the key compilation flags for embedded C++?"
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

**`-fno-exceptions`, `-fno-rtti`, `-fno-threadsafe-statics`, `-fno-use-cxa-atexit`, `-fno-unwind-tables`.**

They strip: exceptions, RTTI, the mutex on static initialization (pthread), destructor registration via `__cxa_atexit`, and `.eh_frame` tables. Often combined with `-Os` and `-std=c++17`.

Rule: these flags make C++ deterministic and compact on bare metal.[^embeddedinterviewlab]

## Detailed explanation

TODO
