---
id: emb-align-0024
title: "Pitfall: why can exchanging raw C structs between LE and BE nodes corrupt data?"
description: "Padding, type sizes, and endianness can differ; a C struct is not a portable wire format."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: pitfall
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

<span class="warn">Exchanging raw C structs between LE and BE nodes does not define a portable data format.</span>

The byte order of numeric fields, padding, alignment, and even type sizes can depend on the implementation. The field offset and bytes on the wire cannot be inferred from the names M4 and PowerPC alone.

Guard: define a wire format and serialize each field explicitly; specify its width and byte order.[^iso-c-n1570]

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
