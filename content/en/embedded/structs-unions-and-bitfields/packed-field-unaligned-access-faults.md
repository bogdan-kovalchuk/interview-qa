---
id: emb-structs-0012
title: "Trap: why can `__attribute__((packed))` cause a HardFault?"
description: "Because a multi-byte field can become unaligned."
track: embedded
section: structs-unions-and-bitfields
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

<span class="warn">Because a multi-byte field can become unaligned.</span>

If `uint32_t value` in a packed struct sits at offset 1, accessing it can generate an unaligned load/store. On Cortex-M this depends on the core, its settings, and the instruction type: sometimes it runs slower, sometimes it triggers a UsageFault or HardFault, especially for certain halfword or word accesses or peripheral accesses.

Defense: for packed protocol data, read fields via `memcpy` into an aligned local variable or parse bytes explicitly.[^embeddedinterviewlab]

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
