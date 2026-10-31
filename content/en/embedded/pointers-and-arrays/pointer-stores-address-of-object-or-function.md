---
id: emb-cppfound-0001
title: "What is a pointer in C and what does it store?"
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

A **pointer** is a variable that stores the **address** of another object or function in memory. It does not store the value itself, only the location.

Two fundamental operations:
- `&x` – address-of: returns the address of object `x`;
- `*p` – dereference: reads/writes the value at address `p`.

They are inverse: `*(&x) == x` always. In embedded, pointers are critical for accessing hardware registers, DMA buffers and callback functions.[^embeddedinterviewlab]

## Detailed explanation

TODO
