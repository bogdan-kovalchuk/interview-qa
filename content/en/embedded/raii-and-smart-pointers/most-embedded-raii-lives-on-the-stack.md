---
id: emb-raii-0014
title: "Does RAII require heap allocation?"
description: "No – RAII does not require the heap: a guard can be a local variable, a class member or a global object."
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
  - source_id: cppcg-r5
    title: "C++ Core Guidelines: R.5 – Prefer scoped objects, don’t heap-allocate unnecessarily"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r5-prefer-scoped-objects-dont-heap-allocate-unnecessarily
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Guideline: a scoped object (local, global or member) has no allocation and deallocation cost in excess of that already used for the containing scope or object; the new/delete example is inefficient and leak-prone; for limited stack space it allows a local const unique_ptr to a big object. A guideline, not a measurement."
  - source_id: cpp-draft-thread-lock-guard
    title: "C++ working draft: Class template lock_guard ([thread.lock.guard])"
    url: https://eel.is/c++draft/thread.lock.guard
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "States that lock_guard controls the ownership of a lockable object within a scope, its constructor calls lock(), its destructor calls unlock(), and its only member is a reference to the mutex. Does not describe interrupt guards or other embedded resources."
  - source_id: cpp-draft-stmt-jump-general
    title: "C++ working draft: Jump statements, general ([stmt.jump.general])"
    url: https://eel.is/c++draft/stmt.jump.general
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "States in a note that on exit from a scope (however accomplished) objects with automatic storage duration constructed in it are destroyed in reverse order of construction, and that a program can be terminated by std::exit or std::abort without destroying such objects. Says nothing about specific embedded resources."
  - source_id: cpp-draft-basic-start-term
    title: "C++ working draft: Termination ([basic.start.term])"
    url: https://eel.is/c++draft/basic.start.term
    accessed: 2026-10-06
    kind: spec
    version: "working draft"
    applicability: "States that constructed objects with static storage duration are destroyed as part of a call to std::exit, and that returning from main invokes std::exit. Does not say whether main returns in firmware."
---

## Short answer

**No – RAII does not require the heap.**

An RAII object can be a local variable, a class member or a global object, so it needs no separate allocation: a scoped object adds no alloc/dealloc beyond what its enclosing scope already has.[^cppcg-r5] Typical embedded RAII – lock guards and scope handles – wraps resources that exist independently (a mutex, an interrupt mask), and `std::lock_guard` by specification stores only a reference to the mutex.[^cpp-draft-thread-lock-guard]

Rule: a stack-allocated guard is the most common and fully heap-free RAII.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
