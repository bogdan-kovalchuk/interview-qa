---
id: emb-cppoop-0034
title: "Why should an abstract base declare its virtual destructor `= default`?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-expr-delete
    title: "C++ working draft: Delete ([expr.delete])"
    url: https://eel.is/c++draft/expr.delete
  - source_id: cpp-draft-class-virtual
    title: "C++ working draft: Virtual functions ([class.virtual])"
    url: https://eel.is/c++draft/class.virtual
  - source_id: cpp-draft-class-dtor
    title: "C++ working draft: Destructors ([class.dtor])"
    url: https://eel.is/c++draft/class.dtor
  - source_id: cpp-draft-dcl-fct-def-default
    title: "C++ working draft: Explicitly-defaulted functions ([dcl.fct.def.default])"
    url: https://eel.is/c++draft/dcl.fct.def.default
  - source_id: cpp-draft-class-copy-ctor
    title: "C++ working draft: Copy/move constructors ([class.copy.ctor])"
    url: https://eel.is/c++draft/class.copy.ctor
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
  - source_id: itanium-abi-atexit
    title: "Itanium C++ ABI: DSO Object Destruction API"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html#dso-dtor-runtime-api
  - source_id: cpp-core-guidelines-c35
    title: "C++ Core Guidelines: C.35 (base class destructor)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c35-a-base-class-destructor-should-be-either-public-and-virtual-or-protected-and-non-virtual
  - source_id: cpp-core-guidelines-c121
    title: "C++ Core Guidelines: C.121 (base class used as an interface)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c121-if-a-base-class-is-used-as-an-interface-make-it-a-pure-abstract-class
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
