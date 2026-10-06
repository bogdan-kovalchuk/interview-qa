---
id: emb-raii-0001
title: "What is RAII and what does the acronym stand for?"
description: "RAII ties a resource lifetime to a C++ object lifetime so the constructor acquires and the destructor releases, with cleanup guaranteed on scope exit."
track: embedded
section: raii-and-smart-pointers
level: junior
type: concept
tags: []
status: published
updated: 2026-10-06
content_revision: 3
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-06; this source is not proof of the claims."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Authoritative section-level reference for the C++ language rules involved; freestanding and vendor toolchains can differ."
  - source_id: cpp-draft-stmt-dcl
    title: "C++ working draft: Declaration statement ([stmt.dcl])"
    url: https://eel.is/c++draft/stmt.dcl
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Paragraph 2: on every transfer of control within a function (including a return from it), automatic block variables active at the source point and not at the destination point are destroyed in reverse order of construction. Does not cover program termination through exit or abort and does not describe exceptions."
  - source_id: cpp-draft-except-ctor
    title: "C++ working draft: Stack unwinding ([except.ctor])"
    url: https://eel.is/c++draft/except.ctor
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Describes destruction of automatic objects in reverse order when an exception is thrown, and that an exception from a constructor runs destructors for already initialized subobjects; does not apply when exceptions are disabled by the compiler."
  - source_id: cpp-draft-except-handle
    title: "C++ working draft: Handling an exception ([except.handle])"
    url: https://eel.is/c++draft/except.handle
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Paragraph 8: if no matching handler is found, std::terminate is invoked, and whether the stack is unwound before that is implementation-defined. Says nothing about behavior when exceptions are disabled."
  - source_id: cpp-draft-support-start-term
    title: "C++ working draft: Start and termination ([support.start.term])"
    url: https://eel.is/c++draft/support.start.term
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "States that std::abort terminates the program without running destructors and that std::exit does not destroy automatic objects; freestanding implementations may not provide these functions."
  - source_id: cppcg-r1-raii
    title: "C++ Core Guidelines: R.1 – Manage resources automatically using resource handles and RAII"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r1-manage-resources-automatically-using-resource-handles-and-raii-resource-acquisition-is-initialization
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Guideline: wrap a resource with paired acquire/release in an object that acquires in the constructor and releases in the destructor; its examples are files, mutexes and memory, not hardware peripherals."
---

## Short answer

**RAII (Resource Acquisition Is Initialization)** – the resource lifetime is tied to the C++ object lifetime.

The constructor acquires the resource, the destructor releases it. The destructor of a local object runs when the scope is left by any path: end of block, early `return`, `break`, `goto`.[^cpp-draft-stmt-dcl] If exceptions are enabled, it also runs during stack unwinding, when the exception reaches a handler.[^cpp-draft-except-ctor]

Rule: anything that must be taken and given back, wrap in an object with a ctor/dtor.[^cppcg-r1-raii]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
