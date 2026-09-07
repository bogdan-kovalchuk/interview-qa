---
id: emb-cppoop-0025
title: "Why are `-fno-exceptions` and `-fno-rtti` used in embedded C++?"
description: "They remove exception-handling and RTTI infrastructure to shrink the binary and meet AUTOSAR and MISRA style"
track: embedded
section: cpp-classes-and-oop
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Authoritative section-level reference for the C++ language rules involved; freestanding and vendor toolchains can differ."
---

## Short answer

**`-fno-exceptions` removes the exception-handling infrastructure; `-fno-rtti` removes RTTI (runtime type information).**

Exceptions add unwind/runtime support and complicate deterministic error handling; RTTI adds type metadata for `dynamic_cast`/`typeid`. They are disabled to shrink the binary and to comply with AUTOSAR (Automotive Open System Architecture) / MISRA C++ (Motor Industry Software Reliability Association C++) style.

Rule: on targets with these flags, do not use `throw`, `dynamic_cast`, `typeid` – rely on return codes and static polymorphism.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
