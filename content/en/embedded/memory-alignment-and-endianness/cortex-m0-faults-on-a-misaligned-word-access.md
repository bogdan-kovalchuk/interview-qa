---
id: emb-align-0007
title: "Trap: what happens on a misaligned 32-bit access on a Cortex-M0?"
description: "A HardFault occurs because Cortex-M0 does not support misaligned access"
track: embedded
section: memory-alignment-and-endianness
level: junior
type: pitfall
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
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Short answer

<span class="warn">HardFault.</span>

Cortex-M0/M0+ (as well as some RISC-V and ARM7TDMI) <span class="warn">do not support misaligned access</span>: any read or write of `uint16_t`/`uint32_t` at a misaligned address -> fault.

Fix: do not cast an offset `uint8_t*` to `uint32_t*`; for misaligned data use `memcpy` into an aligned variable.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
