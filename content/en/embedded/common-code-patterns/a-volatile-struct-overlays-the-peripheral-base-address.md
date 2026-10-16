---
id: emb-patterns-0023
title: "How do you describe a peripheral register block with a struct?"
track: embedded
section: common-code-patterns
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
typedef struct {
  volatile uint32_t CR;  // control
  volatile uint32_t SR;  // status
  volatile uint32_t DR;  // data
} USART_t;
#define USART1 ((USART_t *)0x40011000U)
```

## Short answer

**A struct with `volatile` fields overlaid on the peripheral base address.**

Fields follow a register-compatible order, but their required offsets must be checked against the datasheet: C permits padding between structure members. Access looks like `USART1->DR = b;`.[^iso-c-n1570]

Rule: lock down the layout with `offsetof` asserts so the match with the datasheet does not break.[^embeddedinterviewlab]

## Detailed explanation

TODO
