---
id: emb-dtypes-0031
title: "Is there a difference between `int x;` and `int x = 0;` declared globally?"
description: "Both are zero at startup, but int x; lands explicitly in .bss and costs no Flash."
track: embedded
section: data-types-and-memory-layout
level: middle
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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
    applicability: "Origin of the question and answer; the answer is not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
---

## Short answer

Behaviorally – **NO**: both are 0 at startup. But there is a section difference:

`int x;` -> `.bss`: takes no Flash, startup code sets zero.
`int x = 0;` -> `.data` (or `.bss` if the compiler recognizes zero-init): value 0 may be stored in Flash.

<span class="warn">Practice</span>: write `int x;` without `= 0` for globals – explicitly in `.bss`, does not waste Flash on zeros.[^embeddedinterviewlab]

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
