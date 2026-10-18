---
id: emb-cppfound-0033
title: "What is `ptrdiff_t` and why is it needed?"
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

**ptrdiff_t** – a signed integer type for storing the result of subtracting two pointers, defined in `<stddef.h>`. Size: matches the platform width (32-bit -> 4B, 64-bit -> 8B).

Why: `p - q` gives the number of elements between the pointers. The result is signed (can be negative); storing it in `int` may be insufficient on 64-bit.

Format specifier: `%td` for `printf`.[^embeddedinterviewlab]

## Detailed explanation

TODO
