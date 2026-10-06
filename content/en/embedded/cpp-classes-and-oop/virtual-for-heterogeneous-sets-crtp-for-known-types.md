---
id: emb-cppoop-0021
title: "CRTP versus virtual: when do you choose which?"
description: "Virtual suits heterogeneous collections with runtime dispatch; CRTP suits types known at compile time"
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
  - source_id: cpp-draft-expr-call
    title: "C++ working draft: Function call ([expr.call])"
    url: https://eel.is/c++draft/expr.call
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Says that a virtual function call runs its final overrider in the dynamic type of the object; the standard does not specify the mechanism (vptr/vtable)."
  - source_id: cpp-draft-temp-inst
    title: "C++ working draft: Implicit instantiation ([temp.inst])"
    url: https://eel.is/c++draft/temp.inst
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Says that implicit instantiation of a class template specialization instantiates the declarations but not the definitions of its member functions, and that a member function specialization is instantiated when its definition is needed. It says nothing about code size."
  - source_id: cpp-draft-conv-ptr
    title: "C++ working draft: Pointer conversions ([conv.ptr])"
    url: https://eel.is/c++draft/conv.ptr
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Defines that a pointer to a derived class can be converted to a pointer to its base class; which classes are bases is defined elsewhere in the standard. It does not cover virtual dispatch."
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
    applicability: "Documents -fdevirtualize (an attempt to turn virtual function calls into direct calls; enabled at -O2, -O3 and -Os) and -fipa-icf (identical code folding; enabled at -O2 and -Os, more effective with LTO). Does not guarantee the result for any particular code."
---

## Short answer

**Virtual** – heterogeneous collections (an array of `Base*` with different types) and runtime dispatch on the dynamic type;[^cpp-draft-expr-call] the base-class code exists in one copy.

CRTP (Curiously Recurring Template Pattern) – when the types are known at compile time: the call is static, and no vptr or vtable is needed.[^itanium-cxx-abi] The price is a separate instantiation of the base code for every derived type.[^cpp-draft-temp-inst]

Rule: different types in one container -> virtual; known types and a noticeable dispatch cost, confirmed by measurement -> CRTP.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
