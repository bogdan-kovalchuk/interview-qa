---
id: emb-raii-0006
title: "What does an interrupt-disable RAII guard look like and why is it safe in an ISR?"
description: "The constructor saves the interrupt state in PRIMASK and disables interrupts; the destructor restores the previous state, allowing safe nesting even in ISR context."
track: embedded
section: raii-and-smart-pointers
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

**The ctor saves the current interrupt state and disables interrupts; the dtor restores the previous state.**

An ISR is an interrupt service routine. The guard operates only on the PRIMASK (interrupt mask register), with no blocking calls, so it can be acceptable even in ISR context. Restoring the previous state (rather than an unconditional enable) allows nesting.

Rule: the safest RAII in an ISR is register-level interrupt disable/restore; do not use mutexes or heap there.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
