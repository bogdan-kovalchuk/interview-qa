---
id: emb-raii-0031
title: "How does move semantics let an RAII object be returned from a function?"
description: "The move constructor transfers resource ownership without copying and without double release."
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
  - source_id: cpp-draft-class-copy-elision
    title: "C++ working draft: Copy elision ([class.copy.elision])"
    url: https://eel.is/c++draft/class.copy.elision
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Allows, but does not require, omitting the copy or move when a named local object is returned; an example with a class whose copy constructor is inaccessible shows `return t;` using Thing(Thing&&) or eliding it. Says nothing about the source's state after a move."
  - source_id: cpp-draft-class-copy-ctor
    title: "C++ working draft: Copy/move constructors ([class.copy.ctor])"
    url: https://eel.is/c++draft/class.copy.ctor
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "A move constructor has X&& as its first parameter; if the class declares one, the implicit copy constructor is deleted. The implicit copy constructor is deprecated when the class has a user-declared destructor. Says nothing about the source's state after a move."
  - source_id: cpp-draft-unique-ptr-single
    title: "C++ working draft: unique_ptr for single objects ([unique.ptr.single])"
    url: https://eel.is/c++draft/unique.ptr.single
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "The unique_ptr move constructor gives the source the postcondition get() == nullptr; the copy constructor is deleted. Describes the standard library type, not a particular platform."
---

## Short answer

**The move ctor transfers resource ownership without copying and without double release.**

`return guard;` for a move-only type hands the handle to the caller.[^cpp-draft-class-copy-elision] The move ctor must leave the source with a null handle, so the source dtor frees nothing. This lets factory functions hand out ready-made RAII resources.

Rule: move-only RAII can be returned from functions; copy is deleted to avoid double release.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
