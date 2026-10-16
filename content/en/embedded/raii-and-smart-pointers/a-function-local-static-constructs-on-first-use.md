---
id: emb-raii-0016
title: "What is a static RAII singleton and when do its constructor and destructor run?"
track: embedded
section: raii-and-smart-pointers
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-stmt-dcl
    title: "C++ working draft: Declaration statement ([stmt.dcl])"
    url: https://eel.is/c++draft/stmt.dcl
  - source_id: cpp-draft-basic-start-term
    title: "C++ working draft: Termination ([basic.start.term])"
    url: https://eel.is/c++draft/basic.start.term
  - source_id: cpp-draft-support-start-term
    title: "C++ working draft: Start and termination ([support.start.term])"
    url: https://eel.is/c++draft/support.start.term
  - source_id: gcc-cxx-threadsafe-statics
    title: "GCC: C++ Dialect Options, -fno-threadsafe-statics"
    url: https://gcc.gnu.org/onlinedocs/gcc/C_002b_002b-Dialect-Options.html#index-fthreadsafe-statics
---

## Question code

```c
Driver& instance() {
  static Driver d; // ctor - при 1-му виклику
  return d;
}
```

## Short answer

**Function-local static: the constructor runs once, on the first pass through its declaration; the destructor runs at exit, including return from main.**[^cpp-draft-basic-start-term]

The object is created on the first pass through the declaration, not at program start, so this is lazy initialization that avoids the static initialization order fiasco between translation units.[^cpp-draft-stmt-dcl] But GCC adds thread-safe initialization code by default; `-fno-threadsafe-statics` removes it, leaving a concurrent first entry unsynchronized.[^gcc-cxx-threadsafe-statics]

Rule: Meyers' singleton is heap-free but not always runtime-free; check the generated code on your toolchain.

## Detailed explanation

TODO
