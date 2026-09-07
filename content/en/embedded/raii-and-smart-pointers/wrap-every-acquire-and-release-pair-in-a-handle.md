---
id: emb-raii-0005
title: "Which pairs of HAL functions are worth wrapping in a scoped handle?"
description: "Any acquire/release or init/deinit pair from a HAL, such as interrupt disable/restore, SPI bus lock, chip select, GPIO claim, or DMA channel, is a candidate for a scoped RAII handle."
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

**Any acquire/release (init/deinit) pair.**

A HAL is a hardware abstraction layer. Examples: interrupt disable/restore, SPI (serial peripheral interface) bus lock, CS (chip select) low -> CS high, GPIO (general-purpose input/output) claim, DMA (direct memory access) channel: take from the pool -> return.

Rule: if a C API (application programming interface) has paired acquire/release, wrap them in an RAII object with a ctor/dtor.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
