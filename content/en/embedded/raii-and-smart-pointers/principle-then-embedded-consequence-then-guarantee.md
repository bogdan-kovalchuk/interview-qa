---
id: emb-raii-0033
title: "What should a candidate say about why RAII matters in embedded?"
description: "Answer structure: principle, embedded consequence, compiler guarantee."
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
  - source_id: cppcg-r1-raii
    title: "C++ Core Guidelines: R.1 – Manage resources automatically using resource handles and RAII"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r1-manage-resources-automatically-using-resource-handles-and-raii-resource-acquisition-is-initialization
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Guideline: wrap paired acquire/release (fopen/fclose, lock/unlock, new/delete) in an object that acquires in its constructor and releases in its destructor. A rule, not a language guarantee; does not describe embedded peripherals."
  - source_id: cpp-draft-stmt-jump
    title: "C++ working draft: Jump statements ([stmt.jump])"
    url: https://eel.is/c++draft/stmt.jump
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Note 2: on exit from a scope by any means, automatic-storage objects constructed in it are destroyed in reverse order; the program can be terminated by std::exit or std::abort without destroying such objects. Says nothing about embedded resources."
  - source_id: cpp-draft-class-temporary
    title: "C++ working draft: Temporary objects ([class.temporary])"
    url: https://eel.is/c++draft/class.temporary
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Temporary objects are destroyed as the last step of evaluating the full-expression that (lexically) contains the point where they were created. Says nothing about embedded resources."
---

## Short answer

**Answer structure: principle -> embedded consequence -> compiler guarantee.**

Principle: ctor acquires, dtor releases.[^cppcg-r1-raii] Consequence: no OS to release resources for you, so a leak or deadlock can persist until reset. Guarantee: the dtor of a local object runs on every exit from its scope, including early return, except when the program ends through `exit` or `abort`.[^cpp-draft-stmt-jump]

Rule: emphasise that RAII removes a class of human errors rather than adding capabilities.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
