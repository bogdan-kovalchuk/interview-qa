---
id: emb-raii-0025
title: "What are the rule of three, five and zero?"
track: embedded
section: raii-and-smart-pointers
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-class-copy-ctor
    title: "C++ working draft: Copy/move constructors ([class.copy.ctor])"
    url: https://eel.is/c++draft/class.copy.ctor
  - source_id: cpp-draft-unique-ptr-single
    title: "C++ working draft: unique_ptr for single objects ([unique.ptr.single])"
    url: https://eel.is/c++draft/unique.ptr.single
---

## Short answer

**If a class manages a resource, define or delete all special functions together.**

Rule of three: dtor, copy ctor, copy assign; rule of five (C++11) adds move ctor and move assign. Rule of zero: let RAII members (smart pointers, guards) manage resources, and write no special function at all. A user-declared destructor means no implicit move constructor, so moves fall back to copy.[^cpp-draft-class-copy-ctor]

Rule: aim for rule of zero; if you manage a resource yourself, do not leave default copy operations, which can cause double-free.

## Detailed explanation

TODO
