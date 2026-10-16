---
id: emb-cppoop-0021
title: "CRTP versus virtual: when do you choose which?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-expr-call
    title: "C++ working draft: Function call ([expr.call])"
    url: https://eel.is/c++draft/expr.call
  - source_id: cpp-draft-temp-inst
    title: "C++ working draft: Implicit instantiation ([temp.inst])"
    url: https://eel.is/c++draft/temp.inst
  - source_id: cpp-draft-conv-ptr
    title: "C++ working draft: Pointer conversions ([conv.ptr])"
    url: https://eel.is/c++draft/conv.ptr
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
  - source_id: gcc-optimize-options
    title: "GCC 16.1.0: Optimize Options"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Optimize-Options.html
---

## Short answer

**Virtual** – heterogeneous collections (an array of `Base*` with different types) and runtime dispatch on the dynamic type;[^cpp-draft-expr-call] the base-class code exists in one copy.

CRTP (Curiously Recurring Template Pattern) – when the types are known at compile time: the call is static, and no vptr or vtable is needed.[^itanium-cxx-abi] The price is a separate instantiation of the base code for every derived type.[^cpp-draft-temp-inst]

Rule: different types in one container -> virtual; known types and a noticeable dispatch cost, confirmed by measurement -> CRTP.

## Detailed explanation

TODO
