---
id: emb-structs-0045
title: "Trap: why can overlaying a struct on a raw buffer break alignment?"
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
uint8_t buf[8];
struct Header *h = (struct Header *)buf;
```

## Short answer

<span class="warn">The address of `buf` is not guaranteed to meet the alignment of `struct Header`.</span> Converting a misaligned pointer to a pointer to a more strictly aligned type already has undefined behavior in C; dereferencing it is unsafe as well.[^iso-c-n1570]

An array of `uint8_t` does not become a `struct Header` through a cast; reading through `h` may violate effective type rules.

It is safer to parse the bytes explicitly or copy them into a real local `struct Header` with `memcpy`, after checking the length, fields, endianness, and protocol binary layout.[^iso-c-n1570]

## Detailed explanation

TODO
