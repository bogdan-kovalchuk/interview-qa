---
id: emb-volconst-0019
title: "How do you read the declaration `const int *p`?"
track: embedded
section: volatile-and-const
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**`p` is a pointer to const `int`**.

`p` can be redirected to another `int`, but `*p = 5` is not allowed. Important: the object itself is not necessarily physically immutable; it is just read-only through this pointer.

Rule: read from the variable name right and left: `p` is pointer to const int.[^iso-c-n1570]

## Detailed explanation

TODO
