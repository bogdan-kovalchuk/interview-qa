---
id: emb-dtypes-0067
title: "What does `-fstack-usage` do in GCC, and how do you read its output?"
description: "-fstack-usage emits .su files with file:line:col:function bytes type lines for stack-frame analysis."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
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

`-fstack-usage` makes GCC generate a `.su` file for each `.o`.

Format: `source.c:line:col:function bytes type`
Where type: `static` (fixed), `dynamic` (VLA/alloca), `dynamic,bounded`.

Analysis command: `grep -h "" *.su | sort -k2 -rn | head -20`

Complement: `-Wstack-usage=256` - warning for functions >256B. Critical for bare-metal RTOS where each task's stack is defined in the linker script.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
