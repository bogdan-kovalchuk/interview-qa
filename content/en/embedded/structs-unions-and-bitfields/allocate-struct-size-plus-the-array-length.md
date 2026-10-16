---
id: emb-structs-0033
title: "How do you correctly allocate memory for a flexible array member?"
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
struct Packet {
    uint16_t len;
    uint8_t data[];
};
```

## Short answer

You need to allocate `sizeof(struct Packet) + len` bytes.

For example: `struct Packet *p = malloc(sizeof *p + len);`. Then `p->len = len`, and the payload sits in `p->data[0..len-1]`; `sizeof *p` does not include the flexible array.

Check for `size_t` overflow while adding the size, and check the result of `malloc` for `NULL`. Without a heap, a static byte buffer of the required size can be reserved.[^iso-c-n1570]

## Detailed explanation

TODO
