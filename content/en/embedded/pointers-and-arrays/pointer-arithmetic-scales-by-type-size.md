---
id: emb-cppfound-0007
title: "How does pointer arithmetic work and why does it scale by sizeof(T)?"
track: embedded
section: pointers-and-arrays
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: armv7m-arm
    title: "ARMv7-M Architecture Reference Manual"
    url: https://developer.arm.com/documentation/ddi0403/e/
---

## Short answer

Pointer arithmetic always accounts for the **size of the element type**:

`T *p; p + n` -> physically: `(char*)p + n * sizeof(T)`

Examples:
- `uint8_t *p; p+1` -> +1 byte
- `uint16_t *p; p+1` -> +2 bytes
- `uint32_t *p; p+1` -> +4 bytes

This allows iterating arrays naturally: `p++` moves to the next element regardless of size. Critical in embedded when working with register banks and DMA buffers.[^embeddedinterviewlab]

## Detailed explanation

TODO
