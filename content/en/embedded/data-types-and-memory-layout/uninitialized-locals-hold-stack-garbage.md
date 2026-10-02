---
id: emb-dtypes-0022
title: "Where are local variables stored, and are they initialized automatically?"
description: "Automatic local objects without initializers have indeterminate values; the C standard does not require them to reside on the stack."
track: embedded
section: data-types-and-memory-layout
level: junior
type: concept
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

A local object with automatic storage duration and no explicit initializer has an indeterminate value; C does not require it to reside on the stack. An initializer such as `int x = 0;` gives it a defined initial value, while static-storage objects follow separate zero-initialization rules. Reading an indeterminate value is not a reliable way to obtain leftover stack bytes and can cause undefined behavior, depending on the expression and type.[^iso-c-n1570][^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
