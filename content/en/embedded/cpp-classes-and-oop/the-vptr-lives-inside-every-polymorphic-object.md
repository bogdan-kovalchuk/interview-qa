---
id: emb-cppoop-0015
title: "What is the vptr and where is it stored?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-class-virtual
    title: "C++ working draft: Virtual functions ([class.virtual])"
    url: https://eel.is/c++draft/class.virtual
  - source_id: cpp-draft-class-cdtor
    title: "C++ working draft: Construction and destruction ([class.cdtor])"
    url: https://eel.is/c++draft/class.cdtor
  - source_id: cpp-draft-class-copy-ctor
    title: "C++ working draft: Copy/move constructors ([class.copy.ctor])"
    url: https://eel.is/c++draft/class.copy.ctor
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
---

## Short answer

**A vptr is a hidden pointer inside every object with virtual functions, pointing at the vtable of its dynamic type.** The compiler typically adds it as a hidden member, so `sizeof` grows by about one pointer (4 bytes on 32-bit, subject to alignment). Its position is ABI-dependent, not set by the C++ standard; the Itanium C++ ABI uses offset 0 when the class has no primary base. Only the first virtual function in a hierarchy adds a vptr; later ones do not grow the object.[^itanium-cxx-abi]

## Detailed explanation

TODO
