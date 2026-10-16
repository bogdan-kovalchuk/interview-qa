---
id: emb-cppfound-0056
title: "Cortex-M0 trap: what is the risk?"
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

## Question code

```c
uint8_t *p=(uint8_t*)0x40020000;
uint32_t val=*(uint32_t*)p;
```

## Short answer

`p` is `uint8_t*`: no alignment guarantees. Casting to `uint32_t*` and dereferencing:

If the address `0x40020000` is aligned to 4 -> OK. But if `p` points to `0x40020001` (misaligned) -> Cortex-M0: <span class="warn">HardFault</span>. Cortex-M3/M4: slow but no fault.

Safe approach: `uint32_t val; memcpy(&val, p, sizeof(val));` – the compiler optimizes to a single LDR if aligned.[^embeddedinterviewlab]

## Detailed explanation

TODO
