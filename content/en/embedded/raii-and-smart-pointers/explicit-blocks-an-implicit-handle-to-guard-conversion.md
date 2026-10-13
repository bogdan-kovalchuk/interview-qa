---
id: emb-raii-0027
title: "Why is an RAII guard constructor made `explicit`?"
description: "To forbid implicit conversion from handle to guard."
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
  - source_id: cpp-draft-class-conv-ctor
    title: "C++ working draft: [class.conv.ctor]"
    url: https://eel.is/c++draft/class.conv.ctor
    accessed: 2026-10-13
    kind: spec
    version: null
    applicability: "Exact clause: an explicit constructor is used only for direct-initialization or explicit casts, not for implicit conversions. It does not describe the behavior of particular RTOS handles."
  - source_id: cpp-core-guidelines-c46
    title: "C++ Core Guidelines, C.46: By default, declare single-argument constructors explicit"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c46-by-default-declare-single-argument-constructors-explicit
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Guideline C.46 of the C++ Core Guidelines: by default declare single-argument constructors explicit, to avoid unintended conversions; the guideline allows an implicit conversion when it is intended. It does not establish RTOS behavior."
---

## Short answer

**To forbid implicit conversion from handle to guard.**

`explicit LockGuard(osMutexId_t)` prevents accidentally creating a temporary guard through an implicit conversion (for example, when a mutex is passed to a function that takes a guard by value); such a temporary guard would acquire the lock at the call site.[^cpp-draft-class-conv-ctor]

By default, make single-argument constructors `explicit`; the exception is a type where the implicit conversion is an intended part of its design.[^cpp-core-guidelines-c46]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
