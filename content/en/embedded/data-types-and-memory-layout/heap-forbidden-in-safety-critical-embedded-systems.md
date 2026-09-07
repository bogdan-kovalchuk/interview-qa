---
id: emb-dtypes-0027
title: "Why is heap allocation often banned in safety-critical embedded systems?"
description: "malloc is non-deterministic, fragments memory, and resists worst-case analysis, so safety standards require static allocation."
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

Heap (`malloc`/`free`) has three problems:

1. **Non-deterministic time** – `malloc` takes varying time depending on heap state;
2. **Heap fragmentation** – free memory exists, but not as a contiguous block of the needed size -> `malloc` returns NULL;
3. **Hard to analyze** worst-case memory usage.

MISRA C, DO-178C require static allocation. `malloc` only at initialization, not in the real-time part.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
