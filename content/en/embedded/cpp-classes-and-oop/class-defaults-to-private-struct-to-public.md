---
id: emb-cppoop-0002
title: "How does `class` differ from `struct` in C++?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-class-access-general
    title: "C++ working draft: [class.access.general] Member access control, General"
    url: https://eel.is/c++draft/class.access.general
  - source_id: cpp-draft-class-access-base
    title: "C++ working draft: [class.access.base] Accessibility of base classes and base class members"
    url: https://eel.is/c++draft/class.access.base
  - source_id: cpp-draft-class-prop
    title: "C++ working draft: [class.prop] Properties of classes"
    url: https://eel.is/c++draft/class.prop
  - source_id: cpp-core-guidelines
    title: "C++ Core Guidelines: C.2 (class or struct)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#rc-struct
---

## Short answer

**The main difference is default access: `class` is private, `struct` is public.**[^cpp-draft-class-access-general]

Default access to a base class differs in the same way: `class Derived : Base` inherits private, while `struct Derived : Base` inherits public.[^cpp-draft-class-access-base] Otherwise they are identical: both can have methods, constructors, and inheritance.

Convention: per the C++ Core Guidelines, `struct` is for data that can vary independently, `class` for when there is an invariant.[^cpp-core-guidelines]

## Detailed explanation

TODO
