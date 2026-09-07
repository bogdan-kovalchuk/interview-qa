---
id: emb-cppfound-0023
title: "What is a function pointer and what is its declaration syntax?"
description: "A pointer that stores a function's code address and is called through it, used for ISR tables, state machines, and callbacks."
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
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for c in embedded concepts; details of specific devices and toolchains can differ."
---

## Short answer

**Function pointer** – a pointer to a function: it stores the address of the function's code for calling through it.

Syntax: `return_type (*name)(param_types);` Example: `void (*isr)(void) = &my_handler;`

Call: `(*isr)();` or simply `isr();` (both are valid).

Uses in embedded: ISR dispatch tables, state machine transitions, RTOS task functions, callback API (`HAL_UART_RegisterCallback`).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
