---
id: emb-structs-0027
title: "What does an unnamed zero-width bit-field do?"
description: "A zero-width unnamed bit-field forces the next bit-field onto a new allocation unit."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: mechanism
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

## Question code

```c
struct F {
    unsigned a : 3;
    unsigned   : 0;
    unsigned b : 5;
};
```

## Short answer

A **zero-width unnamed bit-field** forces the next bit-field to start at a new allocation unit.

This is a way to insert a boundary between groups of bit-fields. The actual size and alignment still depend on the underlying type and the compiler ABI.

Embedded rule: this can help with internal layout, but it does not make bit-field mapping portable for a hardware register manual.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
