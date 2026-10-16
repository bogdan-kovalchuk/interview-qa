---
id: emb-volconst-0017
title: "What does `uint8_t * const buf` mean in a parameter or a local variable?"
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

**`buf` is a const pointer to mutable `uint8_t`**.

You cannot assign `buf = other`, but you can modify `buf[0]`. In a function parameter, top-level `const` on the pointer itself is rarely part of the API, because the parameter is already a copy of the pointer value.

Embedded use case: a local alias for a fixed address or register pointer that must not be accidentally reassigned.[^iso-c-n1570]

## Detailed explanation

TODO
