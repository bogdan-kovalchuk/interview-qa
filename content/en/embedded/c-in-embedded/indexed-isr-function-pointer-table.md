---
id: emb-cppfound-0085
title: "What does void(*isr_table[16])(void) do, and how is an ISR called by index?"
description: "How an indexed table of function pointers dispatches interrupt handlers."
track: embedded
section: c-in-embedded
level: junior
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

`void(*isr_table[16])(void)` – an array of 16 function pointers: each points to a function with no arguments that returns void. Initialization: `isr_table[0] = nmi_handler; isr_table[1] = hardfault_handler;` Call: `isr_table[irq_num]();` or `(*isr_table[irq_num])();` This is a software interrupt controller or event dispatcher pattern; the Cortex-M Vector Table in Flash is the hardware analogue: an array of interrupt handler addresses.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
