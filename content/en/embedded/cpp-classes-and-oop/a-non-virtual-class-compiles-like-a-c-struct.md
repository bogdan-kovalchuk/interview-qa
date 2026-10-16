---
id: emb-cppoop-0001
title: "What does \"zero-overhead abstraction\" mean for a C++ class?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-expr-prim-this
    title: "C++ working draft: [expr.prim.this] The keyword this"
    url: https://eel.is/c++draft/expr.prim.this
  - source_id: cpp-draft-class-prop
    title: "C++ working draft: [class.prop] Properties of classes"
    url: https://eel.is/c++draft/class.prop
  - source_id: cpp-draft-intro-abstract
    title: "C++ working draft: [intro.abstract] Abstract machine"
    url: https://eel.is/c++draft/intro.abstract
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
  - source_id: gcc-optimize-options
    title: "GCC 16.1.0: Optimize Options"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Optimize-Options.html
  - source_id: cpp-core-guidelines
    title: "C++ Core Guidelines: In.aims"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#ss-aims
---

## Short answer

**A non-virtual class can compile to the same machine code as a C struct with free functions, provided the optimizer sees the method bodies.**

A non-static member function receives an implicit `this`;[^cpp-draft-expr-prim-this] in typical ABIs a class without `virtual` has no vptr/vtable,[^itanium-cxx-abi] and simple methods are usually inlined. At `-O0` or across separate translation units (without LTO), the call may remain a regular call.[^gcc-optimize-options]

Rule: encapsulation via a class in embedded is usually free in a release build, as long as there are no virtual functions or extra state.[^cpp-core-guidelines]

## Detailed explanation

TODO
