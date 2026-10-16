---
id: emb-align-0026
title: "What does `_Alignas` / `alignas` do and what for?"
track: embedded
section: memory-alignment-and-endianness
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: stm32-an4839
    title: "STMicroelectronics AN4839: Level 1 cache on STM32F7 and STM32H7 Series"
    url: https://www.st.com/resource/en/application_note/an4839-level-1-cache-on-stm32f7-series-and-stm32h7-series-stmicroelectronics.pdf
---

## Question code

```c
_Alignas(32) uint8_t dma_buf[256];
```

## Short answer

**Sets an alignment requirement for a declared object.**

Use it when an ABI or hardware contract requires a particular address. Support for a requested value is implementation-dependent; alignment alone does not provide DMA cache coherency.

Rule: for DMA, consider device requirements, accessible memory, and cache maintenance separately from `_Alignas`.[^iso-c-n1570]

## Detailed explanation

TODO
