---
id: emb-volconst-0020
title: "How do you read the declaration `int * const p`?"
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

**`p` is a const pointer to `int`**.

`p = &other` is forbidden, but `*p = 5` is allowed if the object is not const. This is often confused with `const int *p`, where const applies to the data, not the address.

Embedded example: a pointer to a fixed RAM cell or writable register address that must not change after initialization.[^iso-c-n1570]

## Detailed explanation

TODO
