---
id: emb-dtypes-0056
title: "Trap: what happens? `free(ptr); free(ptr);`"
description: "A double free is undefined behavior that corrupts heap metadata and can open a security exploit."
track: embedded
section: data-types-and-memory-layout
level: middle
type: pitfall
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 4
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

**Double free** has undefined behavior: the C standard does not define its consequences. An implementation may terminate or corrupt allocator state, but a particular failure or exploit is not guaranteed.[^iso-c-n1570]

After `free(ptr)`, the saved pointer value is invalid for another deallocation; `free(NULL)` is allowed and does nothing. Setting `ptr = NULL` helps only for that particular pointer and does not fix its copies.[^iso-c-n1570]

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
