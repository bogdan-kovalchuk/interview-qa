---
id: emb-fnptr-0024
title: "How do you declare an ISR handler type with no arguments and no return value?"
description: "Typedef a pointer to a void function taking void, then use it as the vector table entry type."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 1
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
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Short answer

Typically:

`typedef void (*isr_handler_t)(void);`

After that the vector table can contain `isr_handler_t` entries. On Cortex-M the real vector table often has a special layout because the first entry is the initial stack pointer, not a function pointer.

Rule: do not mix data pointers and function pointers without understanding the startup ABI; the vector table is usually described by separate linker/startup constructs.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
