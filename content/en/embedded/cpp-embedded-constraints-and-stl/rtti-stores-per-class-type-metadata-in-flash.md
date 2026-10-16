---
id: emb-cppstl-0003
title: "Why is RTTI disabled (`-fno-rtti`) and what does it take away?"
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

**RTTI (run-time type information) stores per-class type metadata in Flash; disabling it saves ROM.**

Consequences: `dynamic_cast` is unavailable (use `static_cast` when the type is known) and `typeid` (replace with template specialisation / tag dispatch). Virtual functions still work – vtable is not RTTI.

Rule: without RTTI rely on compile-time type knowledge, not runtime checks.[^embeddedinterviewlab]

## Detailed explanation

TODO
