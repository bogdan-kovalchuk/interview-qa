---
id: emb-align-0007
title: "Trap: what happens on a misaligned 32-bit access on a Cortex-M0?"
track: embedded
section: memory-alignment-and-endianness
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: arm-cortex-m0-alignment
    title: "Arm Cortex-M0 Devices Generic User Guide: Address alignment"
    url: https://documentation-service.arm.com/static/5ea6ce5e9931941038def8c1
  - source_id: learncpp-object-sizes
    title: "LearnCpp: Object sizes and the sizeof operator"
    url: https://www.learncpp.com/cpp-tutorial/object-sizes-and-the-sizeof-operator/
  - source_id: acode-next-cpp
    title: "aCode: End? What next?"
    url: https://acode.com.ua/end-cpp-what-is-next/
---

## Short answer

<span class="warn">HardFault.</span>

Cortex-M0 does not support unaligned memory accesses: a halfword access requires a halfword-aligned address and a word access requires a word-aligned address. A violating load or store raises HardFault.

Do not generalize this answer to every Cortex-M or unrelated ISA. For bytes at an arbitrary offset, copy into an aligned object with `memcpy` and decode the byte order.[^embeddedinterviewlab]

## Detailed explanation

The Cortex-M0 guide defines an aligned word access as one using a word-aligned address and an aligned halfword access as one using a halfword-aligned address. Byte accesses are always aligned. It explicitly states that Cortex-M0 has no unaligned-access support and raises HardFault for an attempted unaligned memory operation.[^arm-cortex-m0-alignment]

This is separate from the C rule. A conversion from `uint8_t *` to `uint32_t *` can produce a pointer that is not correctly aligned; using it is undefined behavior in C even on a processor that supports some unaligned instructions.[^iso-c-n1570]

### Symptom

The device enters `HardFault_Handler` at the failing load or store. Cortex-M0 has fewer configurable fault-status registers than larger Cortex-M cores, so diagnosis usually starts from the stacked PC, register state, faulting instruction, and the effective address it computed.

### Why it happens

The compiler emits a halfword or word instruction because the expression's type promises suitable alignment. If the actual address violates that promise, Cortex-M0 cannot split the instruction into supported unaligned accesses and faults.

A common trigger is parsing a packed frame this way:

```c
uint32_t value = *(const uint32_t *)&frame[1];
```

The cast changes the pointer type, not the alignment of `frame + 1`.

### How to avoid

Copy the representation into aligned storage, then interpret its byte order:

```c
uint32_t value;
memcpy(&value, &frame[1], sizeof value);
```

For a protocol, explicit shifts from bytes are often clearer because `memcpy` preserves host byte order rather than converting it. Enable alignment warnings, inspect packed-member warnings, and keep DMA/MMIO accesses at widths and alignments required by the device reference manual.
