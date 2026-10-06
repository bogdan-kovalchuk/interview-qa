---
id: emb-cppoop-0022
title: "Trap: what is the main drawback of CRTP?"
description: "The base code is duplicated for every derived type as a separate template instantiation, which can inflate ROM"
track: embedded
section: cpp-classes-and-oop
level: junior
type: pitfall
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
  - source_id: cpp-draft-temp-inst
    title: "C++ working draft: Implicit instantiation ([temp.inst])"
    url: https://eel.is/c++draft/temp.inst
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Says that implicit instantiation of a class template specialization instantiates the declarations but not the definitions of its member functions, and that a member function specialization is instantiated when its definition is needed. It says nothing about machine-code size."
  - source_id: cpp-draft-conv-ptr
    title: "C++ working draft: Pointer conversions ([conv.ptr])"
    url: https://eel.is/c++draft/conv.ptr
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Defines that a pointer to a derived class can be converted to a pointer to its base class; which classes are bases is defined elsewhere in the standard. It does not cover virtual dispatch."
  - source_id: gcc-optimize-options
    title: "GCC 16.1.0: Optimize Options"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Optimize-Options.html
    accessed: 2026-10-06
    kind: official
    version: "16.1.0"
    applicability: "Documents -finline-small-functions (inlining functions whose body is smaller than the call code; enabled at -O2, -O3 and -Os) and -fipa-icf (identical code folding; enabled at -O2 and -Os, more effective with LTO). Does not guarantee the result for any particular code."
---

## Short answer

<span class="warn">The base code is duplicated for every derived type</span> (a separate template instantiation of every used member function).[^cpp-draft-temp-inst]

With many derived types and large base methods this can <span class="warn">inflate ROM</span>, though inlining and identical-code folding may offset it.[^gcc-optimize-options] You also cannot hold different CRTP types in one array: `SensorBase<A>` is not a base of `B`, so there is no common pointer type.[^cpp-draft-conv-ptr]

Protection: use CRTP for a small number of types; keep base methods small and move heavy logic into non-template code.

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
