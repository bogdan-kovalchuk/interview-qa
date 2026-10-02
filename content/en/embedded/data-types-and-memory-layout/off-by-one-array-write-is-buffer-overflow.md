---
id: emb-dtypes-0053
title: "What is the bug here? `char buf[256]; buf[256] = '\\0';`"
description: "Valid indices for buf[256] are 0..255, so writing to buf[256] is an out-of-bounds write."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
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

For `char buf[256]`, valid indices are `0..255`; `buf[256]` does not designate an array element, and writing there has undefined behavior.[^iso-c-n1570]

The standard does not define the outcome: data may be corrupted or the program may fail, but no particular variable or address can be predicted.[^iso-c-n1570]

To store 256 characters plus the terminating `\\0`, the buffer needs at least 257 bytes; for a shorter string, write the terminator within the actual capacity.[^iso-c-n1570]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
