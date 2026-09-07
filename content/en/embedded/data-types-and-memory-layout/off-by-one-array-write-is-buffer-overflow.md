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

<span class="warn">Off-by-one error -> buffer overflow.</span> Valid indices for array `buf[256]`: `0..255`. `buf[256]` is already out of bounds.

Writing there -> undefined behavior: it can corrupt another local variable, the return address, or `.bss`.

Correct: `buf[255] = '\0';` or `char buf[257]` if a 256-character string + null-terminator is needed.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
