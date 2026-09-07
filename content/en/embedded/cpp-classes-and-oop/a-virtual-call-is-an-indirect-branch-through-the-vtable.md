---
id: emb-cppoop-0018
title: "How does virtual dispatch hurt determinism on simple cores?"
description: "A virtual call is an indirect branch through the vptr and vtable, which hurts WCET analysis and branch prediction"
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

**A virtual call is an indirect branch through the vptr/vtable, so the call target is not visible directly from the instruction.**

On simple Cortex-M cores this is an extra pointer read and an indirect branch; on more complex cores it can also hurt branch prediction. The main problem for safety/real-time is that proving worst-case execution time and the call graph becomes harder.

Rule: AUTOSAR (Automotive Open System Architecture) C++14 and MISRA C++ (Motor Industry Software Reliability Association C++) restrict virtual dispatch in time-critical paths; in hot paths CRTP or templates are often chosen instead.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
