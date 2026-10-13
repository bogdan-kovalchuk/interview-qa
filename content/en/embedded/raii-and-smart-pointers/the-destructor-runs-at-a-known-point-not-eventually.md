---
id: emb-raii-0028
title: "Why does RAII give deterministic destruction while garbage collection does not?"
description: "The destructor runs at a precisely known moment, at scope exit."
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
  - source_id: cpp-draft-basic-stc-auto
    title: "C++ working draft: [basic.stc.auto]"
    url: https://eel.is/c++draft/basic.stc.auto
    accessed: 2026-10-13
    kind: spec
    version: null
    applicability: "Exact clause: an automatic object whose destructor has side effects may not be destroyed before the end of its block. It does not describe RTOS, ISR or garbage collection."
  - source_id: cpp-draft-stmt-jump
    title: "C++ working draft: Jump statements ([stmt.jump])"
    url: https://eel.is/c++draft/stmt.jump
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Note on [stmt.jump]: on exit from a scope (however accomplished), automatic objects constructed in it are destroyed in reverse order of construction; std::exit and std::abort can end the program without destroying such objects. It does not describe embedded resources."
  - source_id: cpp-core-guidelines-r1
    title: "C++ Core Guidelines, R.1: Manage resources automatically using resource handles and RAII"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r1-manage-resources-automatically-using-resource-handles-and-raii-resource-acquisition-is-initialization
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Guideline R.1 of the C++ Core Guidelines: acquire the resource in the constructor and release it in the destructor, performed automatically on all paths, including exceptions. It does not describe garbage collection."
  - source_id: cpp-draft-support-runtime
    title: "C++ working draft: [support.runtime] (setjmp, longjmp)"
    url: https://eel.is/c++draft/support.runtime
    accessed: 2026-10-13
    kind: spec
    version: null
    applicability: "Exact clause: a setjmp/longjmp pair has undefined behavior if replacing them with catch/throw would invoke non-trivial destructors of automatic objects. It does not describe other ways of leaving a function."
---

## Short answer

**The destructor runs at a precisely known moment, at scope exit.**

For an automatic object whose destructor has side effects, the implementation may not destroy it before the end of its block.[^cpp-draft-basic-stc-auto] So the resource acquired in the constructor is released when the block exits, without any garbage collector involved.[^cpp-draft-stmt-jump]

Rule: keep a resource that must be released on time in an RAII wrapper, not in a manual paired call that is easy to forget.[^cpp-core-guidelines-r1]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
