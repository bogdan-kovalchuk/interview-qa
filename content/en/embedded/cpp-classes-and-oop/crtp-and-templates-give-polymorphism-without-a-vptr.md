---
id: emb-cppoop-0035
title: "Can you get polymorphism without the RAM overhead of a vptr?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
  - source_id: cpp-draft-expr-static-cast
    title: "C++ working draft: Static cast ([expr.static.cast])"
    url: https://eel.is/c++draft/expr.static.cast
  - source_id: cpp-draft-temp-inst
    title: "C++ working draft: Implicit instantiation ([temp.inst])"
    url: https://eel.is/c++draft/temp.inst
  - source_id: cpp-draft-intro-object
    title: "C++ working draft: Object model ([intro.object])"
    url: https://eel.is/c++draft/intro.object
---

## Short answer

**Yes – CRTP (Curiously Recurring Template Pattern, compile-time) or simply templates/composition.**

A CRTP base has no virtual functions, so it is not a dynamic class and needs no vptr;[^itanium-cxx-abi] its `static_cast` to the derived type is valid only if the object really is a `D`.[^cpp-draft-expr-static-cast] The price: the type set is fixed at compile time and the base's code is instantiated per `D`.[^cpp-draft-temp-inst]

Rule: polymorphism over compile-time-known types, where vptr × many objects costs too much RAM -> CRTP or templates, not virtual.

## Detailed explanation

TODO
