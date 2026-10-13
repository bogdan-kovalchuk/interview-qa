---
id: emb-raii-0029
title: "Trap: what happens to the resource if a wrapper object is created on the heap and never deleted?"
description: "The destructor is never called so the resource is never freed, causing a leak despite being an RAII class."
track: embedded
section: raii-and-smart-pointers
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-13
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
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-13; this source is not proof of the claims."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Authoritative section-level reference for the C++ language rules involved; freestanding and vendor toolchains can differ."
  - source_id: cpp-draft-basic-stc-dynamic
    title: "C++ working draft: [basic.stc.dynamic.general]"
    url: https://eel.is/c++draft/basic.stc.dynamic.general
    accessed: 2026-10-13
    kind: spec
    version: null
    applicability: "Exact clause: objects with dynamic storage duration are created by new-expressions and destroyed by delete-expressions. It does not describe RTOS resources and does not concern automatic objects."
  - source_id: cpp-draft-unique-ptr-dtor
    title: "C++ working draft: [unique.ptr.single.dtor]"
    url: https://eel.is/c++draft/unique.ptr.single.dtor
    accessed: 2026-10-13
    kind: spec
    version: null
    applicability: "Exact clause: the destructor of a single-object std::unique_ptr calls the deleter on the stored pointer if it is not null. It concerns std::unique_ptr, not RTOS handles."
  - source_id: cpp-core-guidelines-r5
    title: "C++ Core Guidelines, R.5: Prefer scoped objects, don’t heap-allocate unnecessarily"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r5-prefer-scoped-objects-dont-heap-allocate-unnecessarily
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Guideline R.5 of the C++ Core Guidelines: prefer scoped objects to heap allocation that is not needed. It does not forbid heap allocation where it is required."
---

## Short answer

<span class="warn">The destructor is never called -> the resource is never freed (leak), despite this being an RAII class.</span>[^cpp-draft-basic-stc-dynamic]

An object created with `new` is destroyed only by a delete-expression, so `new LockGuard(...)` without delete is the same forgotten unlock.

Defense: keep RAII objects on the stack, as the C++ Core Guidelines recommend (R.5),[^cpp-core-guidelines-r5] or under `unique_ptr`, which calls its deleter (by default delete) in its destructor.[^cpp-draft-unique-ptr-dtor]

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
