---
id: emb-cppoop-0002
title: "How does `class` differ from `struct` in C++?"
description: "The main difference is default access: class is private, struct is public; default inheritance differs the same way."
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
  - source_id: cpp-draft-class-access-general
    title: "C++ working draft: [class.access.general] Member access control, General"
    url: https://eel.is/c++draft/class.access.general
    accessed: 2026-10-06
    kind: spec
    version: "working draft"
    applicability: "Confirms that members of a class defined with class are private by default, and members of one defined with struct or union are public by default. Does not cover access to base classes (that is [class.access.base])."
  - source_id: cpp-draft-class-access-base
    title: "C++ working draft: [class.access.base] Accessibility of base classes and base class members"
    url: https://eel.is/c++draft/class.access.base
    accessed: 2026-10-06
    kind: spec
    version: "working draft"
    applicability: "Confirms that when a base class has no access-specifier, public is assumed for struct and private for class."
  - source_id: cpp-draft-class-prop
    title: "C++ working draft: [class.prop] Properties of classes"
    url: https://eel.is/c++draft/class.prop
    accessed: 2026-10-06
    kind: spec
    version: "working draft"
    applicability: "Defines a standard-layout class: among the conditions is the same access control for all non-static data members; a standard-layout struct is defined the same way for class-key struct and class, so the keyword does not matter."
  - source_id: cpp-core-guidelines
    title: "C++ Core Guidelines: C.2 (class or struct)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#rc-struct
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Rule C.2: use class if there is an invariant, struct if the data members can vary independently. This is a style convention, not a language requirement; the neighboring rule C.8 recommends class if any member is non-public."
---

## Short answer

**The main difference is default access: `class` is private, `struct` is public.**[^cpp-draft-class-access-general]

Default access to a base class differs in the same way: `class Derived : Base` inherits private, while `struct Derived : Base` inherits public.[^cpp-draft-class-access-base] Otherwise they are identical: both can have methods, constructors, and inheritance.

Convention: per the C++ Core Guidelines, `struct` is for data that can vary independently, `class` for when there is an invariant.[^cpp-core-guidelines]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
