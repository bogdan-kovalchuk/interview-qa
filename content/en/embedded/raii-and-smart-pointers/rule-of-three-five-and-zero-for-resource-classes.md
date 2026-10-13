---
id: emb-raii-0025
title: "What are the rule of three, five and zero?"
description: "If a class manages a resource, define or delete all special functions together."
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
  - source_id: cpp-draft-class-copy-ctor
    title: "C++ working draft: Copy/move constructors ([class.copy.ctor])"
    url: https://eel.is/c++draft/class.copy.ctor
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Says that the implicit move constructor is not declared when the class has a user-declared destructor, and that an implicit copy constructor is deprecated in that case. Does not discuss optimization or generated code."
  - source_id: cpp-draft-unique-ptr-single
    title: "C++ working draft: unique_ptr for single objects ([unique.ptr.single])"
    url: https://eel.is/c++draft/unique.ptr.single
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Says the copy constructor and copy assignment of unique_ptr are deleted, while moves are allowed; its destructor calls the deleter only for a non-null pointer. Does not fix the size."
---

## Short answer

**If a class manages a resource, define or delete all special functions together.**

Rule of three: dtor, copy ctor, copy assign; rule of five (C++11) adds move ctor and move assign. Rule of zero: let RAII members (smart pointers, guards) manage resources, and write no special function at all. A user-declared destructor means no implicit move constructor, so moves fall back to copy.[^cpp-draft-class-copy-ctor]

Rule: aim for rule of zero; if you manage a resource yourself, do not leave default copy operations, which can cause double-free.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
