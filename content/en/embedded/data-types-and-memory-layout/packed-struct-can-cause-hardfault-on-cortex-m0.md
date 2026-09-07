---
id: emb-dtypes-0051
title: "Trap: why can a `packed struct` cause a HardFault on Cortex-M0?"
description: "Cortex-M0 does not support misaligned access, so a packed struct without padding can trigger a HardFault."
track: embedded
section: data-types-and-memory-layout
level: middle
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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
    applicability: "Origin of the question and answer; the answer is not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
---

## Short answer

Cortex-M0/M0+ <span class="warn">does not support misaligned memory access</span>: any access to a 2/4-byte type at an unaligned address -> <span class="warn">HardFault</span>.

`__attribute__((packed))` removes padding – fields may land at odd addresses. Accessing a `uint32_t` at offset 1 -> HardFault.

M3/M4 support misaligned access (but slower). Fix: for serial/network buffers, serialize/deserialize via `memcpy` into an aligned buffer.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
