---
id: emb-volconst-0041
title: "Why is `void f(uint8_t * const p)` a weak API contract?"
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

**Because `const` here is top-level and applies only to the local copy of the pointer parameter inside the function.**[^iso-c-n1570]

The caller sees no difference: the pointer value is already passed by value. The function cannot change the pointer at the caller side regardless of `const`. But it can still modify `p[0]` because the pointed-to data is not const.

Rule: if you want to promise that the buffer will not be modified through this pointer, write `void f(const uint8_t *p)`, not `uint8_t * const p`.[^iso-c-n1570]

## Detailed explanation

TODO
