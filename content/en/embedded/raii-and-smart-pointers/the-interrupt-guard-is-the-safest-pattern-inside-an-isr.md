---
id: emb-raii-0030
title: "Which RAII pattern is the safest to use inside an ISR?"
description: "An interrupt-disable and restore scope guard using register-level operations only."
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

**Interrupt-disable/restore scope guard, register-level operations only.**

It saves PRIMASK (interrupt mask register), disables interrupts in the ctor and restores the previous state in the dtor. No blocking or heap operations, so this is one of the few RAII patterns allowed in interrupt context.

Rule: in an ISR (interrupt service routine), RAII must touch only registers; everything blocking stays outside the interrupt.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
