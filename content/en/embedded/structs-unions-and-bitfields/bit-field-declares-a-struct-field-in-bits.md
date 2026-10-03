---
id: emb-structs-0020
title: "What is a bit-field in a C struct?"
description: "A bit-field lets you declare a struct field with a specified number of bits, for example unsigned mode : 3;."
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

**Bit-field** is a struct or union member with an explicitly specified width in bits, for example `unsigned int mode : 3;`.[^iso-c-n1570]

The implementation places bit-fields in storage units; bit order and fields crossing unit boundaries are implementation-defined. Permitted types are limited by the standard or implementation. This suits compact flags but can be risky for hardware registers and wire formats.[^iso-c-n1570]

For hardware or protocol layouts, rely on bit-fields only when the format and the specific compiler ABI are documented and verified.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
