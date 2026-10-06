---
id: emb-cppoop-0019
title: "What is polymorphism through a `Sensor*` array for?"
description: "A heterogeneous collection of different concrete types behind a common interface in one array or container"
track: embedded
section: cpp-classes-and-oop
level: junior
type: concept
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
  - source_id: cpp-draft-conv-ptr
    title: "C++ working draft: Pointer conversions ([conv.ptr])"
    url: https://eel.is/c++draft/conv.ptr
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Defines that a pointer to a derived class can be converted to a pointer to its base class; this is what lets pointers to different derived types be held as Sensor*. It does not cover virtual dispatch."
  - source_id: cpp-draft-expr-call
    title: "C++ working draft: Function call ([expr.call])"
    url: https://eel.is/c++draft/expr.call
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Says that a virtual function call runs its final overrider in the dynamic type of the object; the standard does not specify the mechanism (vptr/vtable)."
  - source_id: cpp-draft-class-virtual
    title: "C++ working draft: Virtual functions ([class.virtual])"
    url: https://eel.is/c++draft/class.virtual
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Defines a class with a virtual function as polymorphic and notes that the meaning of a virtual call depends on the dynamic type of the object, while a non-virtual call depends only on the static type of the pointer or reference; it does not mention vtables."
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
    accessed: 2026-10-06
    kind: spec
    version: null
    applicability: "Describes the vtable as the table used to dispatch virtual functions and the vptr in an object of a dynamic class. It is an ABI, not the language standard: the ABI of a given toolchain can differ."
---

## Short answer

**A heterogeneous collection: different concrete types behind a common interface in one array/container.**

```cpp
Sensor* arr[] = { &temp, &pressure, &humid };
for (auto s : arr) s->read();
```

A call through a base pointer runs the final overrider for the dynamic type of the object,[^cpp-draft-expr-call] and this is typically implemented with a vptr and a vtable.[^itanium-cxx-abi]

Rule: when you need to hold different types together and call them uniformly, virtual is the classic choice, though not the only one (tagged unions or a table of function pointers are others).

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
