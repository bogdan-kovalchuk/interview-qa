---
id: emb-cppfound-0004
title: "What is the address-of operator and what does it return?"
track: embedded
section: pointers-and-arrays
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

The `&` operator (address-of) returns the **address of an object** in memory – a value of type "pointer to the object's type".

`int x = 5; int *p = &x;` – `p` now points to `x`.

You cannot take the address of:
- expressions without an lvalue (`&(a+b)` – error);
- `register` variables;
- bit-field members of a structure.

Types: `&int` -> `int*`, `&arr` -> `int(*)[N]` (pointer to array, not to element).[^embeddedinterviewlab]

## Detailed explanation

TODO
