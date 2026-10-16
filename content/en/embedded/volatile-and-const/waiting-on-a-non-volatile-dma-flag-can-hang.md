---
id: emb-volconst-0059
title: "Trap: what is wrong with this way of waiting for DMA?"
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

## Question code

```c
uint8_t dma_done = 0;

while (!dma_done) { }
```

## Short answer

<span class="warn">If `dma_done` is modified by an ISR or callback, an ordinary non-volatile flag does not reliably expose the change.</span>

An embedded compiler may keep a non-volatile value in a register or move the read out of the loop. DMA does not change a C variable directly; an ISR/callback notifies the CPU of completion.

Defense: use a volatile flag or atomic/RTOS mechanism compatible with the compiler and MCU; for an RTOS, prefer a semaphore/event notification over busy-wait.[^iso-c-n1570]

## Detailed explanation

TODO
