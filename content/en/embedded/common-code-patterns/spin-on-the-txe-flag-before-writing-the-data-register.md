---
id: emb-patterns-0026
title: "How do you correctly wait for the TXE flag before writing to a UART?"
description: "Spin on a bit test of the status register then write to the data register"
track: embedded
section: common-code-patterns
level: junior
type: mechanism
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
  - source_id: stm32f1-rm0008
    title: "RM0008 Reference manual: STM32F101xx, STM32F102xx, STM32F103xx, STM32F105xx and STM32F107xx advanced Arm-based 32-bit MCUs"
    url: https://www.st.com/content/ccc/resource/technical/document/reference_manual/59/b9/ba/7f/11/af/43/d5/CD00171190.pdf/files/CD00171190.pdf/jcr:content/translations/en.CD00171190.pdf
    accessed: 2026-10-04
    kind: official
    version: "RM0008"
    applicability: "Defines TXE as readiness for the USART data register to accept the next data and distinguishes it from TC; applies only to the listed STM32F1 devices."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
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

## Sources

<!-- generated from frontmatter -->
