---
id: emb-raii-0023
title: "Why should a custom deleter be stateless?"
description: "A stateless deleter type may occupy no space in `unique_ptr` thanks to empty base optimization."
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
    applicability: "Says unique_ptr stores a pointer and a deleter, and its destructor calls the deleter only for a non-null pointer; copy operations are deleted and move is allowed. Does not fix the object's size."
  - source_id: cpp-draft-intro-object
    title: "C++ working draft: Object model ([intro.object])"
    url: https://eel.is/c++draft/intro.object
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Says a base subobject of a standard-layout class with no non-static data members has zero size, and that otherwise the circumstances of zero size are implementation-defined. Gives no sizeof values."
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
    accessed: 2026-10-13
    kind: spec
    version: null
    applicability: "Class layout under the Itanium C++ ABI: an empty base is first placed at offset zero when possible. This is an ABI, not the C++ standard; vendor toolchains and other platforms can differ."
---

## Short answer

**A stateless deleter type (a lambda without capture or an empty functor) may occupy no space in `unique_ptr` thanks to empty base optimization.**

A capturing lambda carries state and has nonzero size, so it increases `unique_ptr`.[^cpp-draft-intro-object] A function pointer deleter has no class state, but its value must still be stored next to the pointer, so the size usually becomes two pointers.[^cpp-draft-unique-ptr-single]

Rule: a deleter without runtime state -> `unique_ptr` can stay the size of a raw pointer; a function pointer deleter is simple but not size-free.[^itanium-cxx-abi]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
