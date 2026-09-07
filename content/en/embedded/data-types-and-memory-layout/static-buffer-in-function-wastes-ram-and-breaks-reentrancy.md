---
id: emb-dtypes-0076
title: "Trap in embedded: what are the risks? `static uint8_t buffer[4096];`"
description: "A static buffer inside a function lives in .bss forever, permanently costs RAM, and breaks reentrancy."
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

`static` in a function -> buffer in `.bss` (RAM, zeroed at boot). 4096B can be a critical portion of RAM (20% of 20KB!).

Risks:
1. <span class="warn">Function is not reentrant</span> – ISR and main loop share the buffer;
2. Occupies RAM all the time (even when unused);
3. If in multiple functions – RAM is quickly exhausted;
4. Static analysis does not always detect the overlap.

Alternative: one global buffer + mutex, or a memory pool.[^embeddedinterviewlab]

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
