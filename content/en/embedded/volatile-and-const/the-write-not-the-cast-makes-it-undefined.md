---
id: emb-volconst-0033
title: "When is casting `const` away not UB, and when does it become UB?"
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

**Casting away `const` is not UB by itself; UB occurs when writing to an object that was actually declared `const`.**

If there is a mutable object `uint32_t x`, then `const uint32_t *cp = &x`, you can technically get back `uint32_t *p = (uint32_t *)cp` and modify `x`. But this is a poor API signal. If the object was `const uint32_t cfg`, writing through the cast has undefined behavior.[^iso-c-n1570]

Rule: do not use a cast to bypass the type contract; fix the signature or ownership model instead.[^iso-c-n1570]

## Detailed explanation

TODO
