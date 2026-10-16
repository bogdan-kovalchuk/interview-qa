---
id: emb-dtypes-0096
title: "Trap: what does malloc return? `char *p = malloc(0);`"
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

Under C11, `malloc(0)` has implementation-defined behavior: the implementation documents whether it returns `NULL` or a pointer that cannot be used to access an object.[^iso-c-n1570] Handle zero size explicitly and define what an empty buffer means; this does not by itself forbid passing a non-null result to `free`. Follow the documented contract of the target embedded allocator.

## Detailed explanation

TODO
