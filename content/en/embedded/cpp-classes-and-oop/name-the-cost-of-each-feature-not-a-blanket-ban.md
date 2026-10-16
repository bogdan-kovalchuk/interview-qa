---
id: emb-cppoop-0037
title: "What should a candidate say about C++ OOP in embedded?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-core-guidelines-in-aims
    title: "C++ Core Guidelines: In.aims"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#inaims-aims
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
  - source_id: arm-cpp-abi
    title: "C++ ABI for the Arm Architecture (CPPABI32)"
    url: https://raw.githubusercontent.com/ARM-software/abi-aa/main/cppabi32/cppabi32.rst
  - source_id: itanium-abi-atexit
    title: "Itanium C++ ABI: DSO Object Destruction API"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html#dso-dtor-runtime-api
  - source_id: gcc-fexceptions
    title: "GCC 16.1.0: Code Gen Options, -fexceptions"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Code-Gen-Options.html#index-fexceptions
  - source_id: gcc-fno-rtti
    title: "GCC 16.1.0: C++ Dialect Options, -fno-rtti"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/C_002b_002b-Dialect-Options.html#index-fno-rtti
  - source_id: libstdcxx-no-exceptions
    title: "libstdc++ manual: Doing without"
    url: https://gcc.gnu.org/onlinedocs/libstdc++/manual/using_exceptions.html#intro.using.exception.no
---

## Short answer

**A candidate should name the cost of each C++ feature rather than ban OOP wholesale.**

A class without `virtual` needs no vptr; `virtual` adds a vptr to every object and a vtable per class;[^itanium-cxx-abi] the first costs RAM, the second usually sits in ROM. CRTP and templates give compile-time polymorphism without a vptr; composition is the usual default. Startup and runtime cost too: walking `.init_array` on Arm,[^arm-cpp-abi] atexit registration of global destructors,[^itanium-abi-atexit] and the consequences of `-fno-exceptions`/`-fno-rtti`.[^gcc-fexceptions][^gcc-fno-rtti]

Rule: name the cost in bytes and cycles, not just the syntax.

## Detailed explanation

TODO
