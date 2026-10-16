---
id: emb-dtypes-0015
title: "What do `sizeof(\"hello\")` and `strlen(\"hello\")` print?"
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

`sizeof("hello")` gives **6** because the string literal is an array of five characters followed by a terminating `\0`. `strlen("hello")` gives **5** because it counts bytes up to, but not including, the first `\0`. Space for a copy of a C string must include the terminator.[^iso-c-n1570]

## Detailed explanation

TODO
