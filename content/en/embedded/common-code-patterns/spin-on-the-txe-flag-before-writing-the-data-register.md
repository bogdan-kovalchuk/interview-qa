---
id: emb-patterns-0026
title: "How do you correctly wait for the TXE flag before writing to a UART?"
track: embedded
section: common-code-patterns
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: stm32f1-rm0008
    title: "RM0008 Reference manual: STM32F101xx, STM32F102xx, STM32F103xx, STM32F105xx and STM32F107xx advanced Arm-based 32-bit MCUs"
    url: https://www.st.com/content/ccc/resource/technical/document/reference_manual/59/b9/ba/7f/11/af/43/d5/CD00171190.pdf/files/CD00171190.pdf/jcr:content/translations/en.CD00171190.pdf
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Question code

```c
void usart1_send(uint8_t b) {
  while (!(USART1->SR & BIT(7))) // wait TXE
    ;
  USART1->DR = b;
}
```

## Short answer

**Spin on a bit test of the status register, then write to the data register.**

For the STM32F1 example, `BIT(7)` is the TXE mask: it means the data register can accept the next byte, not that the whole frame has finished transmitting.[^stm32f1-rm0008]

Register declarations must ensure repeated volatile accesses; add a timeout for long waits.[^iso-c-n1570]

## Detailed explanation

TODO
