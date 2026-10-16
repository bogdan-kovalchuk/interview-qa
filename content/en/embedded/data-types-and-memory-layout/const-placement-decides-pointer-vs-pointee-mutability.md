---
id: emb-dtypes-0059
title: "What does `const` mean in `const uint32_t *p` vs `uint32_t * const p`?"
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

`const uint32_t *p` is a pointer to a `uint32_t` that cannot be changed through `*p`, but `p` itself can be redirected.

`uint32_t * const p` is a pointer with a fixed address, but the value of `*p` can be changed.

`const uint32_t * const p` prevents changing either the address or the data through that expression.[^iso-c-n1570]

Reading the declaration helps identify which level `const` qualifies. For a register pointer, `volatile uint32_t * const REG` fixes the address while `volatile` qualifies accesses to the register.[^iso-c-n1570]

## Detailed explanation

TODO
