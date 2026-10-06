---
id: emb-cppoop-0023
title: "Composition versus inheritance: what is the difference?"
description: "Composition is has-a through member objects; inheritance is is-a and couples tightly to the base"
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
  - source_id: cpp-draft-intro-object
    title: "C++ working draft: [intro.object] Object model"
    url: https://eel.is/c++draft/intro.object
    accessed: 2026-10-06
    kind: spec
    version: "working draft"
    applicability: "States that objects can contain other objects (subobjects) and that a subobject is a member subobject, a base class subobject or an array element. Says nothing about design quality or coupling."
  - source_id: cppcg-c120
    title: "C++ Core Guidelines: C.120 – Use class hierarchies to represent concepts with inherent hierarchical structure (only)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c120-use-class-hierarchies-to-represent-concepts-with-inherent-hierarchical-structure-only
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Guideline: use a class hierarchy only for concepts with inherent hierarchical structure; the idea in the base must exactly match all derived types, and the tight coupling of inheritance should be chosen only when there is no better way to express it; do not use inheritance when a data member will do (it is needed when the derived class overrides a base virtual function or needs a protected member). Sets no numeric thresholds."
  - source_id: cppcg-c121
    title: "C++ Core Guidelines: C.121 – If a base class is used as an interface, make it a pure abstract class"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c121-if-a-base-class-is-used-as-an-interface-make-it-a-pure-abstract-class
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Guideline: a class is more stable if it contains no data; an interface consists of public pure virtual functions and an empty or defaulted virtual destructor. A style recommendation, not a language requirement."
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

**Composition ("has-a")**: a class holds its components as member objects and delegates work to them, using only their public interface. **Inheritance ("is-a")**: a derived class is a kind of its base, and the idea in the base must exactly match all derived types; this is tight coupling.[^cppcg-c120] If a data member is enough, do not use inheritance. Rule: inheritance for a stable interface (a base without data), composition for everything else.[^cppcg-c121]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
