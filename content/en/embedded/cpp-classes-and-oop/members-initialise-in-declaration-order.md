---
id: emb-cppoop-0032
title: "What is the initialisation order of members in a constructor?"
description: "Members are initialised in declaration order in the class, not in init-list order"
track: embedded
section: cpp-classes-and-oop
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
  - source_id: cpp-draft-class-base-init
    title: "C++ working draft: Initializing bases and members ([class.base.init])"
    url: https://eel.is/c++draft/class.base.init
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Defines the initialization order (bases, then non-static members in declaration order regardless of the order of the mem-initializers, then the constructor body) and says the declaration order is mandated by the reverse order of destruction; says nothing about efficiency."
  - source_id: cpp-draft-basic-indet
    title: "C++ working draft: Indeterminate and erroneous values ([basic.indet])"
    url: https://eel.is/c++draft/basic.indet
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "States that evaluating an indeterminate value (outside the unsigned char and std::byte exceptions) is undefined behavior, and that for objects with automatic storage the bytes initially hold erroneous values and the corresponding behavior is erroneous behavior (C++26 draft). Does not concern specific compilers."
  - source_id: cppcg-c47-member-init-order
    title: "C++ Core Guidelines: C.47 – Define and initialize data members in the order of member declaration"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c47-define-and-initialize-data-members-in-the-order-of-member-declaration
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "A guideline with an example of a bug caused by list order; not a language requirement."
  - source_id: gcc-cpp-dialect-options
    title: "GCC 16.1.0: Options Controlling C++ Dialect (-Wreorder)"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/C_002b_002b-Dialect-Options.html#index-Wreorder
    accessed: 2026-10-06
    kind: official
    version: "16.1.0"
    applicability: "Documents -Wreorder: a warning when the order of mem-initializers differs from the order of execution; enabled by -Wall. GCC-specific."
---

## Short answer

**Non-static members are initialised in the order of declaration in the class, not in the order they appear in the init list.**[^cpp-draft-class-base-init] So if `a_` is declared before `b_` and the list reads `: b_{x}, a_{b_ + 1}`, `a_` is initialised first and reads a not-yet-initialised `b_` – an error, usually undefined behavior. Defence: write the list in declaration order; GCC warns through `-Wreorder`, which `-Wall` enables.[^gcc-cpp-dialect-options]

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
