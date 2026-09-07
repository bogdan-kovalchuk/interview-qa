---
id: emb-cppfound-0099
title: "What is dangerous about an uninitialized pointer and how can it be protected?"
description: "Why a wild pointer is not detected by a NULL check and how to initialize safely."
track: embedded
section: c-in-embedded
level: junior
type: concept
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
    applicability: "Origin of the question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for c in embedded concepts; details of specific devices and toolchains can differ."
---

## Short answer

**Wild pointer** – a pointer with a garbage address (stack value), not NULL. A check `if(p != NULL)` does not detect it.

Dangers:
- Write to an arbitrary address -> corruption of critical data;
- On an MCU: write to peripheral registers -> unpredictable hardware behavior;
- Hard to reproduce – depends on stack state.

Protection:
- Always initialize: `int *p = NULL;` or immediately `= &x`;
- `-fsanitize=address` during development;
- Static analysis: PC-lint, Coverity.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
