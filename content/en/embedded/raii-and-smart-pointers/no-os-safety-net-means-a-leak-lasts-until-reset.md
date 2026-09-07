---
id: emb-raii-0002
title: "Why is RAII critical specifically in embedded?"
description: "Without an OS or garbage collector, a forgotten resource on an MCU can stay occupied until reset, so RAII prevents fatal leaks rather than merely adding convenience."
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

**No OS (operating system) safety net and no garbage collector – a forgotten resource can stay occupied until reset.**

A forgotten `mutex_unlock()` -> a permanent deadlock; an unclosed DMA (direct memory access) channel becomes unavailable until reboot. On a desktop the OS cleans up after the process; on an MCU (microcontroller unit) it often does not.

Rule: in embedded, RAII is not a convenience but protection against a whole class of fatal leaks.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
