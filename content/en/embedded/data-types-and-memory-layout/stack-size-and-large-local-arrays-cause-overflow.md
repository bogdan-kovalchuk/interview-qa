---
id: emb-dtypes-0042
title: "What are typical Cortex-M stack sizes, and the most common cause of stack overflow?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

There is no fixed Cortex-M stack size: the memory layout, linker script, and system requirements determine it.

Large automatic arrays, such as `uint8_t buf[2048]`, can substantially increase a function’s stack requirement; actual placement is implementation-dependent.

Assess stack use across the full call depth and nested ISRs, using the configuration for the specific linker script.[^iso-c-n1570]

## Detailed explanation

TODO
