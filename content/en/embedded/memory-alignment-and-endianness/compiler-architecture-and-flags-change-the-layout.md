---
id: emb-align-0041
title: "Trap: why can the same `struct` in source have a different binary layout?"
description: "Padding and alignment depend on the compiler, architecture, and build options, so the same struct header can yield different binary layouts."
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

<span class="warn">Padding and alignment depend on the compiler, architecture, and build options.</span>

The same code on M4 and PowerPC will produce different field offsets, and opposite endianness also reverses the bytes. So "the same .h file" ≠ "the same byte format".

Defense: never assume two compilers have compatible layouts; define an explicit wire format and serialize field by field.[^embeddedinterviewlab]

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
