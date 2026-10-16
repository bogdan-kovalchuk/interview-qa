---
id: emb-structs-0027
title: "What does an unnamed zero-width bit-field do?"
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
struct F {
    unsigned a : 3;
    unsigned   : 0;
    unsigned b : 5;
};
```

## Short answer

A **zero-width unnamed bit-field** forces the next bit-field to start at a new allocation unit.

This is a way to insert a boundary between groups of bit-fields. The actual size and alignment still depend on the underlying type and the compiler ABI.

Embedded rule: this can help with internal layout, but it does not make bit-field mapping portable for a hardware register manual.[^iso-c-n1570]

## Detailed explanation

TODO
