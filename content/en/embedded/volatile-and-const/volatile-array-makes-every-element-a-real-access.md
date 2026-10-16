---
id: emb-volconst-0058
title: "What does `volatile uint8_t rx_buf[64]` mean for a DMA receive buffer?"
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

**Elements of `volatile uint8_t rx_buf[64]` have a volatile-qualified type**, so their accesses are handled under the particular C implementation's rules.

This can be needed if DMA modifies bytes outside the CPU control flow. But it does not solve cache coherency, does not guarantee that DMA has already finished writing, and does not make multi-byte parsing atomic.

Rule: a volatile buffer can be part of a DMA protocol, but completion flags, barriers/cache maintenance, and ownership discipline are also needed.[^iso-c-n1570]

## Detailed explanation

TODO
