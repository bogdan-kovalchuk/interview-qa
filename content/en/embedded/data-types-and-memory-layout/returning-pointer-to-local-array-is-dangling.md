---
id: emb-dtypes-0080
title: "Find the bug: `char* get_name(void) { char buf[32] = \"test\"; return buf; }`"
description: "When the function ends, the local array reaches the end of its lifetime, so the returned pointer cannot be used safely."
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

When the block ends, a local array with automatic storage duration reaches the end of its lifetime, and C makes a pointer value to such an object indeterminate.[^iso-c-n1570] A function therefore cannot safely return a pointer for the caller to use to access `buf`; “stack” describes a common implementation, not a requirement of the standard.[^iso-c-n1570] Pass in a caller-owned buffer, return static storage with an explicit sharing model, or allocate memory with documented ownership.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
