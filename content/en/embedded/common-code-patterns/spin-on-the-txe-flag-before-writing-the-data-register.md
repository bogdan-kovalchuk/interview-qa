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
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
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

This works only with `volatile` fields (otherwise an infinite loop). `BIT(7)` is the TXE (transmit data register empty) mask; when the FIFO/TX (first-in, first-out / transmit) is ready, the bit is set by hardware.

Rule: poll -> check the ready flag -> act; for long waits add a timeout.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
