---
id: emb-raii-0031
title: "How does move semantics let an RAII object be returned from a function?"
track: embedded
section: raii-and-smart-pointers
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-class-copy-elision
    title: "C++ working draft: Copy elision ([class.copy.elision])"
    url: https://eel.is/c++draft/class.copy.elision
  - source_id: cpp-draft-class-copy-ctor
    title: "C++ working draft: Copy/move constructors ([class.copy.ctor])"
    url: https://eel.is/c++draft/class.copy.ctor
  - source_id: cpp-draft-unique-ptr-single
    title: "C++ working draft: unique_ptr for single objects ([unique.ptr.single])"
    url: https://eel.is/c++draft/unique.ptr.single
---

## Short answer

**The move ctor transfers resource ownership without copying and without double release.**

`return guard;` for a move-only type hands the handle to the caller.[^cpp-draft-class-copy-elision] The move ctor must leave the source with a null handle, so the source dtor frees nothing. This lets factory functions hand out ready-made RAII resources.

Rule: move-only RAII can be returned from functions; copy is deleted to avoid double release.[^embeddedinterviewlab]

## Detailed explanation

TODO
