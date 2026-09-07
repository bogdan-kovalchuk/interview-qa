---
id: emb-structs-0029
title: "What is a designated initializer and why is it useful for structs?"
description: "A designated initializer explicitly names the field being initialized, such as .baud = 115200."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: concept
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

A **designated initializer** explicitly specifies which field is being initialized: `.baud = 115200`.

This makes the code more resilient to field reordering and more readable for configuration structs. Unspecified fields receive zero initialization when the initializer is an aggregate initializer.

Embedded rule: for driver config, `UART_Config cfg = { .baud = 115200, .parity = PARITY_NONE };` is better than a positional initializer with a long list of numbers.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
