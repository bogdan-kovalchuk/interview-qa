---
id: emb-dtypes-0060
title: "How does `calloc` differ from `malloc` when it comes to initializing memory?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

`malloc(size)` allocates `size` bytes without initializing them, while `calloc(n, size)` allocates an array of `n` elements of `size` bytes each and sets all bytes to zero; zero bytes are not necessarily the semantic zero for every type.[^iso-c-n1570]

Both functions return `NULL` if allocation fails. Check the result before using it, and explicitly initialize elements to the values the program requires.[^iso-c-n1570]

## Detailed explanation

TODO
