---
id: emb-cppfound-0049
title: "How does pointer arithmetic behave when subtracting two pointers?"
description: "What pointer subtraction returns and when it is defined."
track: embedded
section: c-in-embedded
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 3
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

Subtracting two pointers of the same type returns **ptrdiff_t** – the number of elements between them (not bytes).

`int *p = arr+4; int *q = arr+1; p - q = 3` (three `int` elements).

Condition: both pointers must point to the **same array** (or one-past-the-end). Subtracting pointers that point to different arrays/objects -> <span class="warn">undefined behavior</span>.

Application: `strlen`-like counting, offset between buffer elements.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
