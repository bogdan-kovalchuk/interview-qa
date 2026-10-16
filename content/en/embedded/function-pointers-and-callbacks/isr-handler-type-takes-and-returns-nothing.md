---
id: emb-fnptr-0024
title: "How do you declare an ISR handler type with no arguments and no return value?"
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

Typically:

`typedef void (*isr_handler_t)(void);`

This typedef declares a C function pointer type, but does not by itself describe a hardware vector table. On Cortex-M the first vector is the initial stack pointer, so the table has a special layout.[^arm-cortex-m-startup]

Do not declare the entire Cortex-M vector table as a homogeneous array of `isr_handler_t`; startup code and the linker script define its platform-specific format.[^arm-cortex-m-startup]

## Detailed explanation

TODO
