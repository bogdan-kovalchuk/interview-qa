---
id: emb-fnptr-0023
title: "What is the interrupt vector table in terms of function pointers?"
track: embedded
section: function-pointers-and-callbacks
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: arm-cortex-m-startup
    title: "Arm: Decoding the startup file for Arm Cortex-M4"
    url: https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/decoding-the-startup-file-for-arm-cortex-m4
---

## Short answer

**It is an architecture-defined table of vectors**, including handler addresses used on exception/interrupt entry.

On Cortex-M the first entry provides the initial stack pointer, and subsequent entries contain addresses such as Reset_Handler. This is not a regular C callback API: the layout is defined by the architecture, startup code and linker configuration.[^arm-cortex-m-startup]

The ISR handler signature and vector table placement must match the startup code, linker script and platform ABI.[^arm-cortex-m-startup]

## Detailed explanation

TODO
