---
id: emb-cppfound-0098
title: "What does this hardware-register code do?"
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
uint32_t reg=*((volatile uint32_t*)0x40020010);
reg|=(1<<5);
*((volatile uint32_t*)0x40020010)=reg;
```

## Short answer

A Read-Modify-Write (RMW) operation on a hardware register: **Read** reads the current register value from address `0x40020010`, **Modify** sets bit 5 (`|= (1<<5)`) without changing other bits, **Write** writes back to the register.

<span class="warn">Risk</span>: between read and write another thread or ISR may change the register -> race condition, so for atomic RMW use STM32 BSRR (GPIO) or disable IRQ around the RMW.[^embeddedinterviewlab]

## Detailed explanation

TODO
