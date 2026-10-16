---
id: emb-dtypes-0029
title: "What is a stack overflow, and what causes it in embedded systems?"
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

Stack overflow occurs when the stack pointer leaves the reserved stack region; consequences depend on the memory map and protection and can include data corruption or a fault.[^iso-c-n1570]

Causes:
1. **Large local arrays**: `uint8_t buf[2048]` on the stack;
2. Deep recursion;
3. Nested ISRs and interrupt context saving (the amount depends on architecture and configuration);
4. Stack too small in the linker script.

Diagnostics: stack canaries, stack-usage analysis, MPU protection, or filling the stack with a pattern to estimate its high-water mark.[^embeddedinterviewlab]

## Detailed explanation

TODO
