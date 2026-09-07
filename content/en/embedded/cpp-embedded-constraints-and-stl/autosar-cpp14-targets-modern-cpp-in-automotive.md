---
id: emb-cppstl-0024
title: "How does AUTOSAR C++14 differ from MISRA C++?"
description: "AUTOSAR C++14 is an automotive rule set that governs safe use of modern C++14 features in safety-critical code."
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

**AUTOSAR (AUTomotive Open System ARchitecture) C++14 is an automotive rule set for modern C++14; it governs templates, `constexpr`, `auto`, range-based for and other features.**

It is not "C++ banned" but a set of rules for safe use of the language in safety-critical code. MISRA C++ and AUTOSAR are close in purpose but have different editions, scope and specific rules.

Rule: AUTOSAR C++14 is modern C++ within a safety discipline, not a license to write any abstraction without control.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
