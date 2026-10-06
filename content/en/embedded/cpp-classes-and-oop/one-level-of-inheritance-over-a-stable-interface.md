---
id: emb-cppoop-0012
title: "When is inheritance appropriate in embedded and when is it not?"
description: "Appropriate for a thin interface over a few implementations with a stable contract; avoid deep hierarchies and bases that carry data; numbers like 2–5 types are only a rule of thumb."
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
  - source_id: cppcg-c120
    title: "C++ Core Guidelines: C.120 – Use class hierarchies to represent concepts with inherent hierarchical structure (only)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c120-use-class-hierarchies-to-represent-concepts-with-inherent-hierarchical-structure-only
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Guideline: use a class hierarchy only for concepts with inherent hierarchical structure; the base must exactly match all derived types; do not use inheritance when a data member will do. Sets no numeric thresholds (number of types or levels)."
  - source_id: cppcg-c121
    title: "C++ Core Guidelines: C.121 – If a base class is used as an interface, make it a pure abstract class"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c121-if-a-base-class-is-used-as-an-interface-make-it-a-pure-abstract-class
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Guideline: a class is more stable if it contains no data; an interface should consist of public pure virtual functions and an empty or defaulted virtual destructor; without a virtual destructor, deleting through the base leaks."
  - source_id: cppcg-c122
    title: "C++ Core Guidelines: C.122 – Use abstract classes as interfaces when complete separation of interface and implementation is needed"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c122-use-abstract-classes-as-interfaces-when-complete-separation-of-interface-and-implementation-is-needed
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Guideline with a Device example (write/read): different implementations are used interchangeably through the interface and can be changed as long as access goes through it. A guideline, not a requirement of the standard."
  - source_id: cppcg-c129
    title: "C++ Core Guidelines: C.129 – When designing a class hierarchy, distinguish between implementation inheritance and interface inheritance"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c129-when-designing-a-class-hierarchy-distinguish-between-implementation-inheritance-and-interface-inheritance
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Guideline: distinguish interface inheritance from implementation inheritance; implementation and data in a base make the interface brittle (example: adding data to the base requires reviewing and recompiling all derived classes and users); the importance grows with hierarchy size, age and the number of organizations using it. Gives no numeric thresholds."
  - source_id: itanium-abi-vtable-components
    title: "Itanium C++ ABI: Virtual Table Components and Order"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html#vtable-components
    accessed: 2026-10-06
    kind: spec
    version: null
    applicability: "Section 2.5.2 says every virtual table always contains an offset-to-top and a typeinfo pointer, followed by virtual function pointers used for dispatch, and that an object's vptr holds an address within the vtable. This is an ABI, not the language standard; it gives no byte sizes or memory section."
---

## Short answer

**Appropriate**: one level (an interface base plus a few implementations) with a stable interface, when different types are used through one base, e.g. drivers behind a common `Device`.[^cppcg-c120][^cppcg-c122] <span class="warn">Avoid</span> deep hierarchies and bases carrying data: a change to such a base affects every derived class,[^cppcg-c129] and every polymorphic class adds a vtable while every object adds a vptr.[^itanium-abi-vtable-components] Counts like "2–5 types" or "3+ levels" are only rules of thumb; types known at compile time can use composition.

Rule: inheritance for the interface, everything else composition.[^cppcg-c120]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
