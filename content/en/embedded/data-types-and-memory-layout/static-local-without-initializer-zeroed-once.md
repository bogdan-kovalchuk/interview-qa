---
id: emb-dtypes-0041
title: "Trap: is this zero-initialized inside a function? `static int x;`"
description: "A static local without an initializer is equivalent to static int x = 0 and is zeroed only once, at boot."
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

**Yes.** A block-scope `static int x;` has static storage duration and is implicitly initialized to zero before program execution; this does not happen on every function call.[^iso-c-n1570]

`static int x = 5;` is initialized to 5 once, and subsequent changes persist between calls.

A <span class="warn">regular</span> uninitialized local `int x;` has an indeterminate value; do not assume it is zero.[^iso-c-n1570]

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
