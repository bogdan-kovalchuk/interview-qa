---
id: emb-cppoop-0035
title: "Can you get polymorphism without the RAM overhead of a vptr?"
description: "Yes – CRTP or plain templates/composition resolve calls at compile time, so the object needs no vptr"
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
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
    accessed: 2026-10-06
    kind: spec
    version: null
    applicability: "Defines a dynamic class (with virtual functions or virtual bases) as a class that requires a virtual table pointer; so a class without them does not; the vtable is described as a per-class table. In its layout rules (section 2.4) an empty base class is first tried at offset zero. An ABI, not the language standard: other ABIs can differ in detail."
  - source_id: cpp-draft-expr-static-cast
    title: "C++ working draft: Static cast ([expr.static.cast])"
    url: https://eel.is/c++draft/expr.static.cast
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Defines a static_cast from a base pointer to a derived pointer as valid only if that base is actually a subobject of an object of the derived type; otherwise the behavior is undefined. The compiler does not check this."
  - source_id: cpp-draft-temp-inst
    title: "C++ working draft: Implicit instantiation ([temp.inst])"
    url: https://eel.is/c++draft/temp.inst
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "States that implicit instantiation of a class template specialization instantiates the declarations but not the definitions of member functions, and that a member function specialization is instantiated when its definition is needed. Says nothing about code size."
  - source_id: cpp-draft-intro-object
    title: "C++ working draft: Object model ([intro.object])"
    url: https://eel.is/c++draft/intro.object
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "States that an object of a class with virtual functions or virtual bases has nonzero size, that a base class subobject of a standard-layout class without non-static data members has zero size, and that otherwise zero size is implementation-defined. The actual sizeof depends on the ABI."
---

## Short answer

**Yes – CRTP (Curiously Recurring Template Pattern, compile-time) or simply templates/composition.**

A CRTP base has no virtual functions, so it is not a dynamic class and needs no vptr;[^itanium-cxx-abi] its `static_cast` to the derived type is valid only if the object really is a `D`.[^cpp-draft-expr-static-cast] The price: the type set is fixed at compile time and the base's code is instantiated per `D`.[^cpp-draft-temp-inst]

Rule: polymorphism over compile-time-known types, where vptr × many objects costs too much RAM -> CRTP or templates, not virtual.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
