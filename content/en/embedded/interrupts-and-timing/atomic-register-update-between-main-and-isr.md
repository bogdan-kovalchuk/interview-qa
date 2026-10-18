---
id: emb-dtypes-0104
title: "How do you ensure an atomic register update when both main code and an ISR modify one register?"
track: embedded
section: interrupts-and-timing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: stm32g0-gpio-bsrr
    title: "STMicroelectronics STM32G0x0 Reference Manual, GPIO bit set/reset register"
    url: https://www.st.com/resource/en/reference_manual/dm00463896-stm32g0x0-advanced-armbased-32bit-mcus-stmicroelectronics.pdf
---

## Short answer

Prefer a peripheral set/clear register when its documentation guarantees that a write changes only the selected bits: for example, STM32G0 `GPIOx_BSRR` atomically changes the corresponding `GPIOx_ODR` bits.[^stm32g0-gpio-bsrr] Otherwise, on a single-core system, protect the read-modify-write with a critical section that temporarily masks the interrupt competing for that register. <span class="warn">`volatile` and an ordinary atomic primitive do not make an arbitrary peripheral read-modify-write safe.</span>[^iso-c-n1570]

## Detailed explanation

TODO
