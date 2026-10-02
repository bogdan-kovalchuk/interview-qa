---
id: emb-dtypes-0026
title: "Why can't you rely on `sizeof(int)` in network/serial protocols?"
description: "The width of int depends on the C implementation and ABI, so protocols need an explicitly serialized, fixed-width format."
track: embedded
section: data-types-and-memory-layout
level: middle
type: pitfall
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 3
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
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
---

## Short answer

`int` width depends on the C implementation and ABI, so its raw bytes do not define a portable message format.[^iso-c-n1570] Use `uint16_t` only when appropriate and available, then serialize it in a defined byte order; the type does not specify wire order.

If one side sends two bytes and the other reads four, fields shift or are misread. Define the format in the protocol, independent of either device's `int` width.[^iso-c-n1570]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
