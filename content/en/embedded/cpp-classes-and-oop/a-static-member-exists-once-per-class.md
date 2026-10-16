---
id: emb-cppoop-0028
title: "What is a static class member and where does it live?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-class-static
    title: "C++ working draft: Static members ([class.static])"
    url: https://eel.is/c++draft/class.static
  - source_id: cpp-draft-basic-stc-static
    title: "C++ working draft: Static storage duration ([basic.stc.static])"
    url: https://eel.is/c++draft/basic.stc.static
  - source_id: cpp-draft-dcl-inline-variable
    title: "C++ working draft: The inline specifier ([dcl.inline])"
    url: https://eel.is/c++draft/dcl.inline
  - source_id: gcc-zero-bss
    title: "GCC 16.1.0: Optimize Options – -fno-zero-initialized-in-bss"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Optimize-Options.html
---

## Question code

```cpp
class Counter {
  static uint32_t count_; // одна на клас
};
```

## Short answer

**A static data member belongs to the class, not to an object:** one copy is shared by all instances (one per thread for `thread_local`), and it is not part of the class's subobjects, so it does not increase `sizeof`.[^cpp-draft-class-static] It has static storage duration,[^cpp-draft-basic-stc-static] so with GCC it lives outside the object: in `.bss` for a zero initial value, otherwise in the data section.[^gcc-zero-bss] A non-inline static member is defined once outside the class; `inline static` is a definition in the class itself.[^cpp-draft-class-static]

## Detailed explanation

TODO
