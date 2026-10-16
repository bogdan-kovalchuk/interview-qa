---
id: emb-volconst-0046
title: "Trap: what is wrong with this struct overlay?"
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
typedef struct {
    uint32_t MODER;
    uint32_t IDR;
} GPIO_TypeDef;

#define GPIOA ((GPIO_TypeDef *)0x40020000)
```

## Short answer

<span class="warn">The register overlay fields lack the `volatile` qualifier.</span>

`GPIOA->IDR` has the plain `uint32_t` type, so the C abstract machine does not require a separate volatile access on every read. For a register changed by hardware, this can produce a stale value.[^iso-c-n1570]

Protection: declare the fields as `volatile uint32_t MODER;`, `volatile uint32_t IDR;` or use vendor CMSIS headers where the qualifiers are already set.[^iso-c-n1570]

## Detailed explanation

TODO
