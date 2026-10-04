---
id: emb-align-0032
title: "How do you correctly send data between two different MCUs?"
description: "Define an explicit wire format and serialize field by field with explicit byte order."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 4
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

**Define an explicit wire format and serialize field by field with explicit byte order.**

The format defines fields, widths, byte order, signedness, versioning, and length checks. Do not send a struct as raw bytes across different ABIs: padding, alignment, and type representations can differ. `htonl`/`htons` cover 32- and 16-bit values in network byte order; they are not general encoders.[^iso-c-n1570]

An explicit specification and matching encoders/decoders remove dependence on a particular struct layout; portability still depends on the types and rules the format defines.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
