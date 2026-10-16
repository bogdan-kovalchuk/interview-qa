---
id: emb-cppoop-0017
title: "Why does a base class with virtual methods need a virtual destructor?"
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
  - source_id: cpp-draft-class-dtor
    title: "C++ working draft: Destructors ([class.dtor])"
    url: https://eel.is/c++draft/class.dtor
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
  - source_id: cpp-core-guidelines-c35
    title: "C++ Core Guidelines: C.35 (base class destructor)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c35-a-base-class-destructor-should-be-either-public-and-virtual-or-protected-and-non-virtual
  - source_id: cpp-core-guidelines-c127
    title: "C++ Core Guidelines: C.127 (virtual or protected destructor)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c127-a-class-with-a-virtual-function-should-have-a-virtual-or-protected-destructor
---

## Short answer

<span class="warn">Without a virtual destructor, deleting a derived object through a `Base*` is undefined behavior.</span>[^cpp-draft-expr-delete]

In practice `Base* p = new Derived; delete p;` usually calls only `~Base()`, so the derived resources are not freed, but the standard does not guarantee even that. Protection: if a class has virtual functions and may be deleted through a base pointer, declare `virtual ~Base()`; if such deletion is not intended, make the destructor protected and non-virtual.[^cpp-core-guidelines-c35]

## Detailed explanation

TODO
