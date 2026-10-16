---
id: emb-cppfound-0058
title: "What address will `p+1` have if `p` points to a `uint32_t` at address `0x2000`?"
track: embedded
section: c-in-embedded
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

`p+1 = 0x2004`.

Pointer arithmetic for `uint32_t*`: step = `sizeof(uint32_t) = 4` bytes. `0x2000 + 1*4 = 0x2004`.

General formula: `p + n` -> address = `(uintptr_t)p + n * sizeof(*p)`.

Register bank: if `volatile uint32_t *reg = (volatile uint32_t*)0x40020000;` -> `reg+1` -> register at address `0x40020004`.[^embeddedinterviewlab]

## Detailed explanation

TODO
