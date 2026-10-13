---
id: emb-tmplcx-0012
title: "What are the advantages of CRTP over virtual dispatch?"
description: "No mandatory vptr, no indirect call, and easier WCET analysis compared to virtual dispatch."
track: embedded
section: templates-and-constexpr
level: junior
type: concept
tags: []
status: published
updated: 2026-10-13
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
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-13; this source is not proof of the claims."
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
    accessed: 2026-10-13
    kind: spec
    version: null
    applicability: "Defines a dynamic class (one with virtual functions or virtual bases) as a class requiring a virtual table pointer, so a class without them does not need one. It is an ABI, not the language standard: other ABIs can differ in detail."
  - source_id: cpp-draft-class-virtual
    title: "C++ working draft: Virtual functions ([class.virtual])"
    url: https://eel.is/c++draft/class.virtual
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "A note in this clause says a virtual function call is interpreted by the dynamic type of the object, and a non-virtual call by the static type of the pointer or reference. The vptr/vtable mechanism is not specified here."
  - source_id: cpp-draft-temp-inst
    title: "C++ working draft: Implicit instantiation ([temp.inst])"
    url: https://eel.is/c++draft/temp.inst
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Says that a function template or member function specialization is instantiated when its definition is needed; implicit instantiation of a class template instantiates only the member declarations. It says nothing about code size."
  - source_id: cpp-draft-expr-static-cast
    title: "C++ working draft: Static cast ([expr.static.cast])"
    url: https://eel.is/c++draft/expr.static.cast
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Defines a static_cast from a pointer to a base to a pointer to a derived class as valid only when the base is a subobject of an object of the derived type; otherwise the behavior is undefined."
---

## Short answer

**No mandatory vptr (virtual pointer), no indirect call, and easier WCET (worst-case execution time) analysis.** A class without virtual functions and virtual bases does not need a vptr under the Itanium ABI,[^itanium-cxx-abi] and a non-virtual call is resolved by the static type, so it is a direct call.[^cpp-draft-class-virtual] The vptr size depends on the ABI (application binary interface) and pointer width.

Rule: CRTP – when the type is known at compile time; virtual – when the type is chosen at run time (plugins, dynamic driver loading).

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
