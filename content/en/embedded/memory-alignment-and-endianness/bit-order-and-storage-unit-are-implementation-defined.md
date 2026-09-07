---
id: emb-align-0034
title: "Trap: why is bitfield layout not portable between platforms?"
description: "The standard defines neither bit order nor storage unit for bitfields; this is implementation-defined."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 3
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

<span class="warn">The standard defines neither the bit order within a storage unit nor the storage unit itself; this is implementation-defined.</span>

On LE and BE (and between different compilers), fields may be packed from opposite ends, so the same bitfield struct will produce different bits on the wire.

Guard: for protocols and registers, do not rely on bitfields in a wire format; use explicit masks and shifts over `uint32_t`.[^embeddedinterviewlab]

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
