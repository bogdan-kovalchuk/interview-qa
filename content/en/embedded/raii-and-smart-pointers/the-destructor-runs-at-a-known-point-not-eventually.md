---
id: emb-raii-0028
title: "Why does RAII give deterministic destruction while garbage collection does not?"
track: embedded
section: raii-and-smart-pointers
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-basic-stc-auto
    title: "C++ working draft: [basic.stc.auto]"
    url: https://eel.is/c++draft/basic.stc.auto
  - source_id: cpp-draft-stmt-jump
    title: "C++ working draft: Jump statements ([stmt.jump])"
    url: https://eel.is/c++draft/stmt.jump
  - source_id: cpp-core-guidelines-r1
    title: "C++ Core Guidelines, R.1: Manage resources automatically using resource handles and RAII"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r1-manage-resources-automatically-using-resource-handles-and-raii-resource-acquisition-is-initialization
  - source_id: cpp-draft-support-runtime
    title: "C++ working draft: [support.runtime] (setjmp, longjmp)"
    url: https://eel.is/c++draft/support.runtime
---

## Short answer

**The destructor runs at a precisely known moment, at scope exit.**

For an automatic object whose destructor has side effects, the implementation may not destroy it before the end of its block.[^cpp-draft-basic-stc-auto] So the resource acquired in the constructor is released when the block exits, without any garbage collector involved.[^cpp-draft-stmt-jump]

Rule: keep a resource that must be released on time in an RAII wrapper, not in a manual paired call that is easy to forget.[^cpp-core-guidelines-r1]

## Detailed explanation

TODO
