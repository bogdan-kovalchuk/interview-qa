---
id: emb-dtypes-0001
title: "What is the `.text` section in an embedded program's memory?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: embedded-ld-layout
    title: "GNU ld documentation: linker scripts and output section LMA"
    url: https://sourceware.org/binutils/docs/ld/Output-Section-LMA.html
---

## Short answer

In a typical embedded linker script, `.text` contains executable instructions; its address and access permissions are determined by the target's link layout. Code often runs from Flash, but XIP, copying to RAM, and write protection depend on the MCU and configuration. The name `.text` alone does not guarantee a HardFault on a write attempt.[^embedded-ld-layout]

## Detailed explanation

TODO
