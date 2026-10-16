---
id: emb-volconst-0037
title: "Why can a read-modify-write on a volatile register be unsafe?"
track: embedded
section: volatile-and-const
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: stm32-bsrr
    title: "STMicroelectronics STM32L1 reference manual, GPIO bitwise handling"
    url: https://www.st.com/resource/en/reference_manual/cd00240193.pdf
---

## Question code

```c
GPIOA_ODR |= (1u << pin);
```

## Short answer

The operation is <span class="warn">not atomic</span>: it reads, modifies in the CPU, then writes back.

If hardware or an ISR changes bits between the read and write, the final write can overwrite them. For example, STM32 GPIO has BSRR, which changes selected ODR bits with one write; this is a property of that specific peripheral, not every register.[^stm32-bsrr]

Protection: use documented set/clear registers where available; otherwise protect the RMW from concurrent access, for example with a critical section for an ISR. `volatile` does not make the sequence atomic.[^stm32-bsrr]

## Detailed explanation

TODO
