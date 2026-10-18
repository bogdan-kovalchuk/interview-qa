---
id: emb-cppfound-0026
title: "What is the difference between `const int *p` and `int * const p`?"
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

`const int *p` (or `int const *p`) – **a pointer to a constant int**:
- `*p = 5` – forbidden (the data is protected);
- `p = &y` – allowed (the address can be changed).

`int * const p` – **a constant pointer to int**:
- `*p = 5` – allowed;
- `p = &y` – forbidden (the address is fixed).

`const int * const p` – both the data and the address are immutable. Rule: read right to left.[^embeddedinterviewlab]

## Detailed explanation

TODO
