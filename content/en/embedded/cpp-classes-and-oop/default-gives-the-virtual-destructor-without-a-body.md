---
id: emb-cppoop-0034
title: "Why should an abstract base declare its virtual destructor `= default`?"
description: "It ensures correct polymorphic destruction without a hand-written empty body"
track: embedded
section: cpp-classes-and-oop
level: junior
type: mechanism
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
  - source_id: cpp-draft-expr-delete
    title: "C++ working draft: Delete ([expr.delete])"
    url: https://eel.is/c++draft/expr.delete
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Paragraph 3: in a single-object delete-expression, if the static type is not similar to the dynamic type, the static type must be a base of the dynamic type and have a virtual destructor, otherwise the behavior is undefined. Does not describe what a particular compiler does."
  - source_id: cpp-draft-class-virtual
    title: "C++ working draft: Virtual functions ([class.virtual])"
    url: https://eel.is/c++draft/class.virtual
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "States that a virtual function call depends on the dynamic type of the object while a non-virtual call depends on the static type. Does not discuss destructors specifically."
  - source_id: cpp-draft-class-dtor
    title: "C++ working draft: Destructors ([class.dtor])"
    url: https://eel.is/c++draft/class.dtor
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Defines a trivial destructor: not user-provided, not virtual, and the destructors of all direct bases and class-type members are trivial too; so a virtual destructor is never trivial. Does not say whether the compiler registers the object's destruction."
  - source_id: cpp-draft-dcl-fct-def-default
    title: "C++ working draft: Explicitly-defaulted functions ([dcl.fct.def.default])"
    url: https://eel.is/c++draft/dcl.fct.def.default
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Defines a user-provided function as user-declared and not explicitly defaulted or deleted on its first declaration; a function explicitly defaulted on its first declaration is implicitly inline. Says nothing about the generated machine code."
  - source_id: cpp-draft-class-copy-ctor
    title: "C++ working draft: Copy/move constructors ([class.copy.ctor])"
    url: https://eel.is/c++draft/class.copy.ctor
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "States that an implicit move constructor is declared only if, among other conditions, the class has no user-declared destructor, and that implicitly defining the copy constructor when a destructor is user-declared is deprecated. Does not cover how this is optimized."
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
    accessed: 2026-10-06
    kind: spec
    version: null
    applicability: "Section 2.5.2 says a virtual destructor occupies a pair of vtable entries: the complete object destructor (no delete) and the deleting destructor (destroys the object and calls delete). An ABI, not the language standard; says nothing about the contents of a particular link."
  - source_id: itanium-abi-atexit
    title: "Itanium C++ ABI: DSO Object Destruction API"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html#dso-dtor-runtime-api
    accessed: 2026-10-06
    kind: spec
    version: null
    applicability: "Section 3.3.6.3 says that after constructing a global (or local static) object that will need destruction at exit, a termination function is registered through __cxa_atexit. An ABI, not the language standard; the Arm EABI uses __aeabi_atexit."
  - source_id: cpp-core-guidelines-c35
    title: "C++ Core Guidelines: C.35 (base class destructor)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c35-a-base-class-destructor-should-be-either-public-and-virtual-or-protected-and-non-virtual
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Rule C.35: a base class destructor should be either public and virtual or protected and non-virtual; protected forbids deleting through a base pointer. A style recommendation, not a language requirement."
  - source_id: cpp-core-guidelines-c121
    title: "C++ Core Guidelines: C.121 (base class used as an interface)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c121-if-a-base-class-is-used-as-an-interface-make-it-a-pure-abstract-class
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Rule C.121: an interface should consist of public pure virtual functions and a default or empty virtual destructor. A style recommendation, not a language requirement."
---

## Question code

```cpp
virtual ~Sensor() = default;
```

## Short answer

**It ensures correct polymorphic destruction without a hand-written empty body.**

`= default` asks the compiler to generate the destructor, and `virtual` makes it non-trivial by definition.[^cpp-draft-class-dtor] Without `virtual`, `delete base_ptr` on a derived object is undefined behavior,[^cpp-draft-expr-delete] whereas with it the destructor is selected by the dynamic type.[^cpp-draft-class-virtual]

Rule: if a base may be deleted through a pointer to it, write `public virtual ~T() = default;`, otherwise use a `protected` non-virtual destructor.[^cpp-core-guidelines-c35]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
