---
id: emb-cppoop-0024
title: "What are the advantages of composition in embedded?"
description: "Predictable size, flexible substitution and loose coupling keep modules independently testable"
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
  - source_id: cpp-draft-expr-sizeof
    title: "C++ working draft: [expr.sizeof] Sizeof"
    url: https://eel.is/c++draft/expr.sizeof
    accessed: 2026-10-06
    kind: spec
    version: "working draft"
    applicability: "States that for a class sizeof is the number of bytes in an object of that class including any padding needed to place such objects in an array, and that the amount and placement of padding is a property of the implementation. Gives no concrete values."
  - source_id: iso-tr-18015
    title: "ISO/IEC TR 18015:2006 Technical Report on C++ Performance"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/TR18015.pdf
    accessed: 2026-10-06
    kind: spec
    version: "TR 18015:2006"
    applicability: "Section 5.3.1 says a class without a virtual function needs as much space as a struct with the same data (apart from possible padding), a non-virtual function takes no space in the object, and a polymorphic class pays one pointer per object plus a table per class. A 2006 report: concrete sizes depend on the implementation."
  - source_id: cppcg-c120
    title: "C++ Core Guidelines: C.120 – Use class hierarchies to represent concepts with inherent hierarchical structure (only)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c120-use-class-hierarchies-to-represent-concepts-with-inherent-hierarchical-structure-only
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Guideline: use a class hierarchy only for concepts with inherent hierarchical structure; calls inheritance tight coupling and advises against it when a data member will do. Sets no numeric thresholds."
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
---

## Short answer

**Predictable size, flexible substitution, loose coupling.** A class without virtual functions takes as much space as a struct with the same fields, so a member component adds only its own size and padding, with no vptr.[^iso-tr-18015] Substitution is possible at runtime through a pointer or reference to an interface, where different implementations are interchangeable,[^cppcg-c122] or at compile time through a template parameter. Inheritance, by contrast, couples tightly to the base.[^cppcg-c120]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
