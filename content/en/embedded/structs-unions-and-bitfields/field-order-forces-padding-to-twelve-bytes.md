---
id: emb-structs-0003
title: "What is the typical size of `struct S` when `uint32_t` has 4-byte alignment?"
track: embedded
section: structs-unions-and-bitfields
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Question code

```c
struct S {
    uint8_t a;
    uint32_t b;
    uint8_t c;
};
```

## Short answer

On a common ABI where `uint8_t` has size and alignment 1 byte and `uint32_t` has size and alignment 4 bytes, `sizeof(struct S) == 12`.[^iso-c-n1570]

Under those assumptions, `a` is at offset 0, `b` at offset 4, and `c` at offset 8, with tail padding after `c`. C does not guarantee these offsets or this size for every 32-bit ABI.[^iso-c-n1570]

Field order affects the RAM/Flash footprint. For arrays of structs, padding repeats in every element.[^iso-c-n1570]

## Detailed explanation

TODO
