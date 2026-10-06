---
id: emb-raii-0013
title: "Trap: what is wrong with \"RAII only works with smart pointers\"?"
description: "RAII is the principle of tying a resource to an object's lifetime within a scope, not a feature of smart pointers."
track: embedded
section: raii-and-smart-pointers
level: junior
type: pitfall
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
  - source_id: cpp-draft-stmt-jump-general
    title: "C++ working draft: Jump statements, general ([stmt.jump.general])"
    url: https://eel.is/c++draft/stmt.jump.general
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "States in a note that on exit from a scope (however accomplished) objects with automatic storage duration constructed in it are destroyed in reverse order of construction, and that a program can be terminated by std::exit or std::abort without destroying such objects. Says nothing about specific embedded resources."
  - source_id: cpp-draft-thread-lock-guard
    title: "C++ working draft: Class template lock_guard ([thread.lock.guard])"
    url: https://eel.is/c++draft/thread.lock.guard
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "States that lock_guard controls the ownership of a lockable object within a scope and maintains it throughout its lifetime; the constructor calls lock(), the destructor calls unlock(); copy construction and assignment are deleted; the only member is a reference to the mutex. Does not describe interrupt guards or other embedded resources."
  - source_id: cppcg-r1
    title: "C++ Core Guidelines: R.1 – Manage resources automatically using resource handles and RAII"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r1-manage-resources-automatically-using-resource-handles-and-raii-resource-acquisition-is-initialization
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Guideline: a resource that needs paired acquire/release calls (fopen/fclose, lock/unlock, new/delete) should be wrapped in an object that acquires it in the constructor and releases it in the destructor. Does not restrict RAII to pointers."
  - source_id: cppcg-cp20
    title: "C++ Core Guidelines: CP.20 – Use RAII, never plain lock()/unlock()"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#cp20-use-raii-never-plain-lockunlock
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Guideline: use an RAII wrapper instead of manual lock() and unlock(), because unlock() is easy to forget or to skip with a return or an exception. Says nothing about interrupts or bare-metal."
---

## Short answer

<span class="warn">RAII is the principle of tying a resource to an object's lifetime within a scope, not a feature of smart pointers.</span>

The constructor acquires the resource and the destructor releases it: this is how `std::lock_guard`, which holds a mutex for its lifetime,[^cpp-draft-thread-lock-guard] a custom interrupt guard or a scoped peripheral handle work, with no heap pointer at all. A smart pointer is just one application of the idea, for the `new`/`delete` pair.[^cppcg-r1]

Defense: think of RAII as ctor acquires, dtor releases, not as `unique_ptr`.

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
