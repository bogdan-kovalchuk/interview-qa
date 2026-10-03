---
id: emb-structs-0021
title: "What is the range of `unsigned mode : 3`?"
description: "From 0 to 7; three unsigned bits represent 2^3 = 8 values."
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

## Short answer

**From `0` to `7`**.

Three bits in an `unsigned int` bit-field represent `2^3 = 8` values, from `0` to `7`. On assignment, a value outside this range is converted to the unsigned bit-field modulo `2^3`; this conversion is not a substitute for validating input.[^iso-c-n1570]

Check the allowed range before assignment, especially when the value comes from a protocol or other external input.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
