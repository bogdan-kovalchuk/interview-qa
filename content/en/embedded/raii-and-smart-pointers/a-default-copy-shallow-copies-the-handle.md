---
id: emb-raii-0026
title: "Trap: why is forgetting `= delete` on the copy constructor of a resource wrapper critical?"
description: "The default copy constructor makes a shallow handle copy so two objects own one resource, causing double free."
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
  - source_id: cpp-draft-class-copy-ctor
    title: "C++ working draft: [class.copy.ctor]"
    url: https://eel.is/c++draft/class.copy.ctor
    accessed: 2026-10-13
    kind: spec
    version: null
    applicability: "Exact clause: the implicitly defined copy constructor performs a memberwise copy of bases and members. It does not describe what copying a particular RTOS handle means."
  - source_id: cpp-draft-new-delete-single
    title: "C++ working draft: [new.delete.single]"
    url: https://eel.is/c++draft/new.delete.single
    accessed: 2026-10-13
    kind: spec
    version: null
    applicability: "Exact clause: the precondition of operator delete is that the pointer comes from an earlier operator new and has not been invalidated by an earlier operator delete. A second delete of the same pointer violates it. It does not cover RTOS handles."
  - source_id: cpp-draft-structure-specifications
    title: "C++ working draft: [structure.specifications]"
    url: https://eel.is/c++draft/structure.specifications
    accessed: 2026-10-13
    kind: spec
    version: null
    applicability: "Exact clause: violating the Preconditions of a library function results in undefined behavior. It does not describe RTOS APIs, which the C++ standard does not define."
---

## Short answer

<span class="warn">The default copy ctor makes a shallow copy of the handle -> two objects own one resource -> double free.</span>[^cpp-draft-class-copy-ctor]

On destruction of both, the dtor releases the resource twice. For `new`/`delete` this is undefined behavior, because the precondition of `operator delete` is violated,[^cpp-draft-new-delete-single][^cpp-draft-structure-specifications] while for an RTOS handle the result depends on the API: an error, corruption, or closing an already closed resource.

Defense: usually either `= delete` copy or move semantics with zeroing the source.[^embeddedinterviewlab]

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
