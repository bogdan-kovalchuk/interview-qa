---
id: emb-dtypes-0074
title: "What is an ABI, and how does it affect type sizes?"
description: "An ABI fixes type sizes, the calling convention, and struct alignment so compiled modules stay compatible."
track: embedded
section: data-types-and-memory-layout
level: middle
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

**ABI** (Application Binary Interface) – rules for interaction between compiled modules: type sizes, calling convention, struct alignment, register usage.

ARM AAPCS (Cortex-M):
- `int` = 32 bits
- `long` = 32 bits (not 64!)
- `long long` = 64 bits
- `float` = 32 bits
- `double` = 64 bits
- `pointer` = 32 bits

ABI is the reason `sizeof(int)` on Cortex-M equals 4. Changing the ABI (cross-compile) breaks binary compatibility.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
