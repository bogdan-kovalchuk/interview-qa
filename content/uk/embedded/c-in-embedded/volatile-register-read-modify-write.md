---
id: emb-cppfound-0098
title: "Що зробить?"
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

Read-Modify-Write (RMW) операція над hardware register: **Read** читає поточне значення регістру з адреси `0x40020010`, **Modify** встановлює біт 5 (`|= (1<<5)`) не змінюючи інші біти, **Write** записує назад у регістр.

<span class="warn">Ризик</span>: між read і write інший потік або ISR може змінити регістр -> race condition, тож для атомарного RMW використовуй STM32 BSRR (GPIO) або disable IRQ навколо RMW.[^embeddedinterviewlab]

## Detailed explanation

TODO
