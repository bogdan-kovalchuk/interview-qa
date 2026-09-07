---
id: emb-cppfound-0097
title: "What is an array of function pointers and where is it used in embedded systems?"
description: "How function-pointer arrays implement constant-time dispatch tables."
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

`void (*handlers[8])(void)` – an array of 8 function pointers.

Usage:
- **Software interrupt router**: `handlers[irq_id]();`;
- **State machine**: `state_fn[current_state]();`;
- **Protocol parser**: `cmd_handlers[cmd_id](payload);`;
- **Bootloader jump**: a table of entry points in Flash.

Advantages: O(1) dispatch, easy to extend by changing the table. The Cortex-M Vector Table is a hardware implementation of this pattern.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
