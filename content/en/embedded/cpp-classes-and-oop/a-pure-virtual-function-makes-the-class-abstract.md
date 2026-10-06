---
id: emb-cppoop-0016
title: "What is a pure virtual function and an abstract class?"
description: "A pure virtual function declared with = 0 makes its class abstract and uninstantiable"
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
  - source_id: cpp-draft-class-abstract
    title: "C++ working draft: Abstract classes ([class.abstract])"
    url: https://eel.is/c++draft/class.abstract
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Defines a pure virtual function (pure-specifier) and an abstract class (a pure virtual function whose final overrider is pure), forbids objects of an abstract class except as subobjects of derived classes, allows a pure virtual function to be defined for calls through a qualified-id, and makes a virtual call to a pure function from a constructor or destructor of the same object undefined behavior. It says nothing about a vptr or vtable."
  - source_id: cpp-draft-class-dtor
    title: "C++ working draft: Destructors ([class.dtor])"
    url: https://eel.is/c++draft/class.dtor
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Paragraph 11: a destructor may be virtual and have a pure-specifier; if the destructor is virtual and objects of that class or a derived class are created in the program, it must be defined. It does not cover interfaces without a destructor."
  - source_id: cpp-core-guidelines
    title: "C++ Core Guidelines: C.121 (interface as pure abstract class)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c121-if-a-base-class-is-used-as-an-interface-make-it-a-pure-abstract-class
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Rule C.121: an interface normally consists only of public pure virtual functions and a default or empty virtual destructor. This is a style recommendation, not a language requirement; it says nothing about HAL or embedded code."
---

## Question code

```cpp
class Sensor {
public:
  virtual int16_t read() = 0;
  virtual ~Sensor() = default;
};
```

## Short answer

**`= 0` makes a function pure virtual; a class with a function whose final overrider is pure is abstract, so its objects can exist only as subobjects of derived classes.**[^cpp-draft-class-abstract] It defines an interface (contract): a derived class that leaves any pure virtual function unimplemented stays abstract too. In embedded code it is the C++ way to describe a driver/HAL interface; the Core Guidelines advise building it from pure virtual functions and a virtual destructor.[^cpp-core-guidelines]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
