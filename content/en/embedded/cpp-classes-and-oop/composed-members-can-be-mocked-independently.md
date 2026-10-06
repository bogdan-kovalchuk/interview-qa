---
id: emb-cppoop-0036
title: "Composition or inheritance: which is easier to test, and why?"
description: "Composition with dependency injection: a member component can be swapped for a mock through a template parameter or an interface"
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
  - source_id: cpp-core-guidelines-c120
    title: "C++ Core Guidelines: C.120 (class hierarchies)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c120-use-class-hierarchies-to-represent-concepts-with-inherent-hierarchical-structure-only
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Rule C.120: use class hierarchies only for concepts with inherent hierarchical structure; its reason names the \"tight coupling of inheritance\". A style recommendation; the rule does not discuss testing."
  - source_id: cpp-core-guidelines-c129
    title: "C++ Core Guidelines: C.129 (implementation vs interface inheritance)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c129-when-designing-a-class-hierarchy-distinguish-between-implementation-inheritance-and-interface-inheritance
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Rule C.129: implementation details in an interface make it brittle, and data in a base class increases the complexity of implementing the base and can lead to code replication; distinguish implementation inheritance from interface inheritance. A style recommendation; the rule does not discuss testing."
  - source_id: gmock-for-dummies
    title: "GoogleTest: gMock for Dummies"
    url: https://google.github.io/googletest/gmock_for_dummies.html#a-case-for-mock-turtles
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "Describes dependency injection through an interface (a class with virtual functions) and a mock class that inherits that interface. Does not cover non-virtual dependencies or embedded specifics."
  - source_id: gmock-cookbook-nonvirtual
    title: "GoogleTest: gMock Cookbook, Mocking Non-virtual Methods"
    url: https://google.github.io/googletest/gmock_cook_book.html#MockingNonVirtualMethods
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "States that for non-virtual classes the mock is a separate type with no common base but the same method signatures, and the choice between the real class and the mock is made at compile time through a template parameter. Says nothing about embedded costs."
---

## Short answer

**Composition with dependency injection: a member component can be swapped for a mock via a template parameter or an interface.**

Implementation inheritance couples tightly,[^cpp-core-guidelines-c120] and data in a base complicates it,[^cpp-core-guidelines-c129] so a derived-class test runs the base's code. But composing a concrete type (`Uart uart_;`) allows no mock by itself, while a mock inheriting a pure interface is the standard substitute.[^gmock-for-dummies]

Rule: testability comes from being able to substitute the dependency, not from composition as such.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
