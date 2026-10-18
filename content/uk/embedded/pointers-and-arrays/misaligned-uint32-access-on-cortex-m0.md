---
id: emb-cppfound-0056
title: "Trap на Cortex-M0 – ризик?"
track: embedded
section: pointers-and-arrays
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

`p` – `uint8_t*`: гарантій вирівнювання нема. Cast до `uint32_t*` і розіменування:

Якщо адреса `0x40020000` вирівняна на 4 -> ОК. Але якщо `p` вказує на `0x40020001` (misaligned) -> Cortex-M0: <span class="warn">HardFault</span>. Cortex-M3/M4: повільно але без fault.

Безпечно: `uint32_t val; memcpy(&val, p, sizeof(val));` – компілятор оптимізує до одного LDR якщо вирівняно.[^embeddedinterviewlab]

## Detailed explanation

TODO
