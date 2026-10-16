---
id: emb-dtypes-0056
title: "Trap: what happens? `free(ptr); free(ptr);`"
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

**Double free** has undefined behavior: the C standard does not define its consequences. An implementation may terminate or corrupt allocator state, but a particular failure or exploit is not guaranteed.[^iso-c-n1570]

After `free(ptr)`, the saved pointer value is invalid for another deallocation; `free(NULL)` is allowed and does nothing. Setting `ptr = NULL` helps only for that particular pointer and does not fix its copies.[^iso-c-n1570]

## Detailed explanation

TODO
