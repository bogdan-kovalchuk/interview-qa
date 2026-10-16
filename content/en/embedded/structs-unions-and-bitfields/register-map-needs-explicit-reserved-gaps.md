---
id: emb-structs-0009
title: "Trap: what is wrong with this register map?"
track: embedded
section: structs-unions-and-bitfields
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
typedef struct {
    volatile uint32_t CR;
    volatile uint32_t SR;
    volatile uint32_t DR;
} UART_TypeDef;
```

## Short answer

<span class="warn">Reserved gaps between registers may be missing.</span>

A hardware register map often has address gaps. If the manual says `DR` is at offset `0x10` but the struct places it at offset `0x08`, all accesses after the gap will be wrong. `volatile` does not fix an incorrect layout.

Defense: add reserved fields of the correct size, for example `uint32_t RESERVED0[2]`, and verify with `offsetof`.[^iso-c-n1570]

## Detailed explanation

TODO
