---
id: emb-cppoop-0036
title: "Composition or inheritance: which is easier to test, and why?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-core-guidelines-c120
    title: "C++ Core Guidelines: C.120 (class hierarchies)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c120-use-class-hierarchies-to-represent-concepts-with-inherent-hierarchical-structure-only
  - source_id: cpp-core-guidelines-c129
    title: "C++ Core Guidelines: C.129 (implementation vs interface inheritance)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c129-when-designing-a-class-hierarchy-distinguish-between-implementation-inheritance-and-interface-inheritance
  - source_id: gmock-for-dummies
    title: "GoogleTest: gMock for Dummies"
    url: https://google.github.io/googletest/gmock_for_dummies.html#a-case-for-mock-turtles
  - source_id: gmock-cookbook-nonvirtual
    title: "GoogleTest: gMock Cookbook, Mocking Non-virtual Methods"
    url: https://google.github.io/googletest/gmock_cook_book.html#MockingNonVirtualMethods
---

## Short answer

**Composition with dependency injection: a member component can be swapped for a mock via a template parameter or an interface.**

Implementation inheritance couples tightly,[^cpp-core-guidelines-c120] and data in a base complicates it,[^cpp-core-guidelines-c129] so a derived-class test runs the base's code. But composing a concrete type (`Uart uart_;`) allows no mock by itself, while a mock inheriting a pure interface is the standard substitute.[^gmock-for-dummies]

Rule: testability comes from being able to substitute the dependency, not from composition as such.

## Detailed explanation

TODO
