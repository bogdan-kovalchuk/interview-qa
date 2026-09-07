---
id: emb-cppfound-0001
title: "What is a pointer in C and what does it store?"
description: "A pointer stores the address of another object or function; address-of and dereference are inverse operations, and pointers are critical in embedded for hardware registers, DMA buffers and callbacks."
track: embedded
section: c-in-embedded
level: junior
type: concept
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
    applicability: "Origin of the question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for c in embedded concepts; details of specific devices and toolchains can differ."
---

## Short answer

A **pointer** is a variable that stores the **address** of another object or function in memory. It does not store the value itself, only the location.

Two fundamental operations:
- `&x` – address-of: returns the address of object `x`;
- `*p` – dereference: reads/writes the value at address `p`.

They are inverse: `*(&x) == x` always. In embedded, pointers are critical for accessing hardware registers, DMA buffers and callback functions.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
