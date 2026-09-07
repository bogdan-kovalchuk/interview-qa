---
id: emb-dtypes-0057
title: "What is a reentrant function, and why do `static` locals break reentrancy?"
description: "A static local is shared across all calls, so an ISR and the main loop racing through it causes a data race."
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

**Reentrant function** can be safely called concurrently from multiple threads or recursively.

A `static` local is one copy for the entire function (in `.data`/`.bss`), not on the stack: if an ISR interrupts the function and calls it again, both contexts will modify the same variable -> <span class="warn">race condition</span>.

Classic example: `strtok()` is not reentrant (static buffer). Use `strtok_r()`. In bare-metal: if a function is called from both ISR and main loop, avoid static locals.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
