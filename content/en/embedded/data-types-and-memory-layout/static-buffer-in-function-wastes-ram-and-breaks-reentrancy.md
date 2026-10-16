---
id: emb-dtypes-0076
title: "Trap in embedded: what are the risks? `static uint8_t buffer[4096];`"
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

A local variable declared `static` has static storage duration: its storage lasts for the whole program execution and it is initialized once; placement in `.bss` depends on the toolchain and linker script.[^iso-c-n1570] The buffer is not inherently non-reentrant, but concurrent calls or an ISR and main loop accessing the same state can conflict. A 4096-byte buffer is 20% only when the RAM budget is 20 KiB.[^iso-c-n1570]

## Detailed explanation

TODO
