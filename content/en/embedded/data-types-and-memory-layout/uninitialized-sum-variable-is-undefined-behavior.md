---
id: emb-dtypes-0043
title: "Find the bug: `int sum; for(int i = 0; i < n; i++) sum += arr[i];`"
description: "sum has no initializer, so the first addition reads stack garbage - undefined behavior."
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

An uninitialized automatic local `int sum;` has an indeterminate value. For an ordinary automatic object in C, reading that uninitialized value is undefined behavior; it is not necessarily “stack garbage.”[^iso-c-n1570]

Initialize the accumulator explicitly, for example `int sum = 0;`, before adding elements.[^iso-c-n1570]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
