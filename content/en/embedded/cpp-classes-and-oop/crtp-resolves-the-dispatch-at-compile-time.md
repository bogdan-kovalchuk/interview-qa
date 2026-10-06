---
id: emb-cppoop-0020
title: "What is CRTP and which problem does it solve?"
description: "Curiously Recurring Template Pattern provides compile-time polymorphism via a static cast to the derived type"
track: embedded
section: cpp-classes-and-oop
level: junior
type: mechanism
tags: []
status: published
updated: 2026-10-06
content_revision: 3
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-06; this source is not proof of the claims."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Authoritative section-level reference for the C++ language rules involved; freestanding and vendor toolchains can differ."
  - source_id: cpp-draft-expr-static-cast
    title: "C++ working draft: Static cast ([expr.static.cast])"
    url: https://eel.is/c++draft/expr.static.cast
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Defines that static_cast from a pointer to a base class to a pointer to a derived class is valid only if the base is actually a subobject of an object of the derived type; otherwise the behavior is undefined. The compiler does not check this."
  - source_id: cpp-draft-temp-inst
    title: "C++ working draft: Implicit instantiation ([temp.inst])"
    url: https://eel.is/c++draft/temp.inst
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Says that implicit instantiation of a class template specialization instantiates the declarations but not the definitions of its member functions, and that a member function specialization is instantiated when its definition is needed. It says nothing about code size."
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
    accessed: 2026-10-06
    kind: spec
    version: null
    applicability: "Defines a dynamic class (one with virtual functions or virtual bases) as a class requiring a virtual table pointer, so a class without them does not need one. It is an ABI, not the language standard: other ABIs can differ in detail."
  - source_id: gcc-optimize-options
    title: "GCC 16.1.0: Optimize Options"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Optimize-Options.html
    accessed: 2026-10-06
    kind: official
    version: "16.1.0"
    applicability: "Documents that without optimization GCC does not expand functions inline (-fno-inline is the default) and that -finline-small-functions is enabled at -O2, -O3 and -Os; the actual heuristic decisions depend on the code."
---

## Question code

```cpp
template <typename D>
class SensorBase {
public:
  int16_t read() {
    return static_cast<D*>(this)->read_impl();
  }
};
```

## Short answer

**Curiously Recurring Template Pattern – compile-time polymorphism** via `static_cast` to the derived type.

The derived class inherits `SensorBase<Derived>`, and `read()` calls `read_impl()` as an ordinary (non-virtual) function, so no vptr or vtable is needed for it.[^itanium-cxx-abi] The optimizer may inline such a call, but without optimization (`-O0`) GCC does not inline functions.[^gcc-optimize-options] The `static_cast` is valid only when the object really has type `Derived`, otherwise it is undefined behavior.[^cpp-draft-expr-static-cast]

Rule: CRTP removes the dispatch cost (vptr, indirect call), but does not guarantee zero overhead overall.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
