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
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: gcc-attributes
    title: "GCC: Common Attributes"
    url: https://gcc.gnu.org/onlinedocs/gcc/Common-Attributes.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "GCC documentation for attribute extensions and their limits."
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
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

Defense: for packed protocol data, read fields via `memcpy` into an aligned local variable or parse bytes explicitly.[^gcc-attributes]

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
