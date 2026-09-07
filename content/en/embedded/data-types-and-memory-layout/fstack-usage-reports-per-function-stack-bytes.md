---
id: emb-dtypes-0058
title: "How do you check a function's stack frame size in GCC?"
description: "The -fstack-usage flag makes GCC emit .su files reporting each function's stack frame size."
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

The **-fstack-usage** flag: GCC generates `.su` files alongside `.o`.

Line format in `.su`: `file.c:10:5:foo 2048 static`
Fields (space-separated): [1] `file:line:col:func`, [2] bytes, [3] type.

Analyzing the largest stack frames: `cat *.su | sort -k2 -rn | head -20`

Also: `-Wstack-usage=N` - warning if a function uses >N bytes. Always check functions called from ISR.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
