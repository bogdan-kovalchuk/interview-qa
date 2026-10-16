---
id: emb-dtypes-0007
title: "What is the C runtime init sequence before `main()` on Cortex-M?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: cmsis-startup
    title: "CMSIS-Core startup file documentation"
    url: https://github.com/ARM-software/CMSIS_6/blob/main/CMSIS/Documentation/Doxygen/Core/src/core_startup_c.md
  - source_id: gnu-ld-data
    title: "GNU ld: Output Section LMA"
    url: https://sourceware.org/binutils/docs/ld/Output-Section-LMA.html
---

## Short answer

After reset, a Cortex-M core obtains the initial `MSP` and `Reset_Handler` address from the Vector Table’s first entries; their addresses in memory depend on the specific MCU implementation. Startup code performs early system initialization, copies initialized data into RAM, zeroes zero-initialized regions, transfers control to the C/C++ runtime, and the runtime eventually calls `main()`. The exact order and copy tables depend on the startup file and toolchain.[^cmsis-startup] [^gnu-ld-data]

## Detailed explanation

TODO
