---
id: emb-cppstl-0023
title: "What do MISRA C++ rules usually restrict in embedded C++?"
description: "MISRA C++ restricts exception-based control flow, dynamic allocation, RTTI, unsafe casts, goto, complex inheritance and raw unions."
track: embedded
section: cpp-embedded-constraints-and-stl
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

**MISRA (Motor Industry Software Reliability Association) C++ restricts exception-based control flow, dynamic allocation, RTTI (run-time type information), unsafe casts, `goto`, complex inheritance hierarchies and raw unions.**

The goal is determinism, analyzability and controlled data/control flow. Exact wording depends on the standard version and project profile, so in an interview it is better to say "restricts/regulates" rather than "bans everything".

Rule: MISRA C++ is about predictability; under it you write with return codes, static allocation and minimal runtime magic.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
