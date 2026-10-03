---
id: emb-structs-0001
title: "What is a `struct` in C and what is it for in embedded?"
description: "A struct groups several fields of different types into a single object with a fixed field declaration order."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 3
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

**`struct`** groups several fields of different types into one object whose fields have a defined declaration order, while exact offsets and padding depend on the C implementation.[^iso-c-n1570]

In embedded, structs are used for peripheral register maps, protocol frames, driver state, configuration blocks, and DMA descriptors. Importantly, a struct has not only logical fields but also a physical layout in memory: offsets, padding, alignment.

Rule: when a struct crosses the boundary to hardware, a binary protocol, or a Flash layout, its size and offsets must be verified explicitly.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
