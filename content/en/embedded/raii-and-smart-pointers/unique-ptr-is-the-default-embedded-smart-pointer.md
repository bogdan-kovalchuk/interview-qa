---
id: emb-raii-0032
title: "Why is `unique_ptr` considered the default smart pointer for embedded?"
description: "Raw-pointer-level access, exclusive ownership, explicit transfer via move, custom deleter support for HAL."
track: embedded
section: raii-and-smart-pointers
level: junior
type: concept
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
  - source_id: cpp-draft-unique-ptr-single
    title: "C++ working draft: unique_ptr for single objects ([unique.ptr.single])"
    url: https://eel.is/c++draft/unique.ptr.single
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Says the destructor calls the deleter on a non-null pointer; operator* and operator-> return *get() with the precondition get() != nullptr; the move constructor gives the source get() == nullptr. Describes the standard library type, not a particular platform."
  - source_id: cpp-draft-unique-ptr-dltr-dflt
    title: "C++ working draft: default_delete ([unique.ptr.dltr.dflt])"
    url: https://eel.is/c++draft/unique.ptr.dltr.dflt
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "default_delete calls delete on its argument; its synopsis has no data members. This section does not define the size of unique_ptr in any particular implementation."
  - source_id: cppcg-r21
    title: "C++ Core Guidelines: R.21 – Prefer unique_ptr over shared_ptr unless you need to share ownership"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r21-prefer-unique_ptr-over-shared_ptr-unless-you-need-to-share-ownership
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Guideline: use unique_ptr unless shared ownership is needed; unique_ptr is simpler and more predictable because it does not maintain a use count. Not a measurement of cost on any particular platform."
  - source_id: cpp-draft-util-smartptr-shared-create
    title: "C++ working draft: shared_ptr creation ([util.smartptr.shared.create])"
    url: https://eel.is/c++draft/util.smartptr.shared.create
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Note: an implementation may allocate more than sizeof(T) for bookkeeping structures such as reference counts; make_shared should perform no more than one memory allocation. Not a guarantee for every implementation."
---

## Short answer

**Raw-pointer-level access, exclusive ownership, explicit transfer via move, custom deleter support for HAL.**

A `unique_ptr` with the default deleter stores a pointer and a `default_delete` with no data members, so in typical implementations its size equals a raw pointer's; `*` and `->` dereference that same pointer.[^cpp-draft-unique-ptr-dltr-dflt][^cpp-draft-unique-ptr-single] For most ownership cases that is enough: unlike `shared_ptr`, it keeps no reference count.[^cppcg-r21]

Rule: start with `unique_ptr`; move to `shared_ptr` only when shared ownership is genuinely needed.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
