---
id: emb-structs-0036
title: "Why can an incomplete struct not be created as an object in a header?"
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
typedef struct Driver Driver;

Driver d;
```

## Short answer

<span class="warn">Impossible, because the compiler does not know the size of `Driver`.</span>

A forward declaration creates an incomplete type. You can declare pointers to it because the pointer size is known, but you cannot allocate an object by value or access its fields.

Defence: an opaque API returns a `Driver *` or accepts caller-provided storage through a separate API that knows the required size and alignment.[^iso-c-n1570]

## Detailed explanation

TODO
