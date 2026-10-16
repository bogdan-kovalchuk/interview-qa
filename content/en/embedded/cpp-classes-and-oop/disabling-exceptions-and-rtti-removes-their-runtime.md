---
id: emb-cppoop-0025
title: "Why are `-fno-exceptions` and `-fno-rtti` used in embedded C++?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: gcc-fexceptions
    title: "GCC: Options for Code Generation Conventions (-fexceptions)"
    url: https://gcc.gnu.org/onlinedocs/gcc/Code-Gen-Options.html#index-fexceptions
  - source_id: gcc-fno-rtti
    title: "GCC: C++ Dialect Options (-fno-rtti)"
    url: https://gcc.gnu.org/onlinedocs/gcc/C_002b_002b-Dialect-Options.html#index-fno-rtti
  - source_id: iso-tr-18015
    title: "ISO/IEC TR 18015:2006 Technical Report on C++ Performance"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/TR18015.pdf
---

## Short answer

**`-fno-exceptions` omits the code and data needed to propagate exceptions, and `-fno-rtti` omits the type information for `dynamic_cast` and `typeid`.**[^gcc-fexceptions][^gcc-fno-rtti] This shrinks the binary, and the time from `throw` to `catch` is hard to predict, so exceptions may not suit real-time work.[^iso-tr-18015] So on such targets do not use `throw`, `typeid` or a downcasting `dynamic_cast` – rely on error codes and static polymorphism.

## Detailed explanation

TODO
