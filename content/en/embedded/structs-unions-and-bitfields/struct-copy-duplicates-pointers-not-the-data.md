---
id: emb-structs-0051
title: "Trap: why can copying a struct with pointer fields be a shallow-copy bug?"
description: "Structure assignment copies the pointer value, not the data it points to."
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

<span class="warn">Structure assignment copies the pointer value, not the data it points to.</span>

After `b = a`, both structures may point to the same buffer. If one structure frees or modifies the buffer, the other sees the consequences. In embedded, this commonly occurs with DMA buffers, queues, and driver config pointers.

Mitigation: define ownership: either the pointer is borrowed and this is documented, a deep copy is needed, or the buffer is passed separately with a lifetime contract.[^embeddedinterviewlab]

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
