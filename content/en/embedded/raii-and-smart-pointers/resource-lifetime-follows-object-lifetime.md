---
id: emb-raii-0001
title: "What is RAII and what does the acronym stand for?"
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
  - source_id: cpp-draft-except-ctor
    title: "C++ working draft: Stack unwinding ([except.ctor])"
    url: https://eel.is/c++draft/except.ctor
  - source_id: cpp-draft-except-handle
    title: "C++ working draft: Handling an exception ([except.handle])"
    url: https://eel.is/c++draft/except.handle
  - source_id: cpp-draft-support-start-term
    title: "C++ working draft: Start and termination ([support.start.term])"
    url: https://eel.is/c++draft/support.start.term
  - source_id: cppcg-r1-raii
    title: "C++ Core Guidelines: R.1 – Manage resources automatically using resource handles and RAII"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r1-manage-resources-automatically-using-resource-handles-and-raii-resource-acquisition-is-initialization
---

## Short answer

**RAII (Resource Acquisition Is Initialization)** – the resource lifetime is tied to the C++ object lifetime.

The constructor acquires the resource, the destructor releases it. The destructor of a local object runs when the scope is left by any path: end of block, early `return`, `break`, `goto`.[^cpp-draft-stmt-dcl] If exceptions are enabled, it also runs during stack unwinding, when the exception reaches a handler.[^cpp-draft-except-ctor]

Rule: anything that must be taken and given back, wrap in an object with a ctor/dtor.[^cppcg-r1-raii]

## Detailed explanation

TODO
