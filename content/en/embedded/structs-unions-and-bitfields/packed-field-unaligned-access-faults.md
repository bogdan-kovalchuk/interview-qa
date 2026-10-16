---
id: emb-structs-0012
title: "Trap: why can `__attribute__((packed))` cause a HardFault?"
track: embedded
section: structs-unions-and-bitfields
sources:
  - source_id: gcc-attributes
    title: "GCC: Common Attributes"
    url: https://gcc.gnu.org/onlinedocs/gcc/Common-Attributes.html
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

<span class="warn">Because a multi-byte field can become unaligned.</span>

If `uint32_t value` in a packed struct sits at offset 1, accessing it can generate an unaligned load/store. On Cortex-M this depends on the core, its settings, and the instruction type: sometimes it runs slower, sometimes it triggers a UsageFault or HardFault, especially for certain halfword or word accesses or peripheral accesses.

Defense: for packed protocol data, read fields via `memcpy` into an aligned local variable or parse bytes explicitly.[^gcc-attributes]

## Detailed explanation

TODO
