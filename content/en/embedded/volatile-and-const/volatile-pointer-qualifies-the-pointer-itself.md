---
id: emb-volconst-0010
title: "What does the declaration `uint32_t * volatile p` mean?"
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

**`p` is a volatile pointer to a plain `uint32_t`**.

Here volatile applies to the pointer variable itself, not to the data at the address. Access to `p` is volatile, but `*p` designates an ordinary `uint32_t`, not volatile hardware data.[^iso-c-n1570]

For volatile data at the address, use `volatile uint32_t *p`; for both properties, use `volatile uint32_t * volatile p`.[^iso-c-n1570]

## Detailed explanation

TODO
