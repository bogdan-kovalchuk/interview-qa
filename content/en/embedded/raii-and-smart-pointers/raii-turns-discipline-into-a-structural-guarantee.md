---
id: emb-raii-0034
title: "How would you state the main value of RAII in one sentence?"
track: embedded
section: raii-and-smart-pointers
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cppcg-r1-raii
    title: "C++ Core Guidelines: R.1 – Manage resources automatically using resource handles and RAII"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r1-manage-resources-automatically-using-resource-handles-and-raii-resource-acquisition-is-initialization
  - source_id: cpp-draft-stmt-jump
    title: "C++ working draft: Jump statements ([stmt.jump])"
    url: https://eel.is/c++draft/stmt.jump
---

## Short answer

**RAII turns resource management from a discipline problem (remembering `deinit()`) into a structural guarantee: the compiler calls the destructor of a local object when it leaves its scope.**[^cpp-draft-stmt-jump]

Instead of relying on the programmer not forgetting to free a resource on every path, you encode the release once in the destructor.[^cppcg-r1-raii]

Rule: this phrase is a strong summary answer to the question "why RAII".[^embeddedinterviewlab]

## Detailed explanation

TODO
