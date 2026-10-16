---
id: emb-patterns-0016
title: "How do you read a multi-bit field (mask and shift)?"
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
#define PRESC_MASK  (0x7U << 4) // bits [6:4]
#define PRESC_SHIFT 4
uint8_t p = (reg & PRESC_MASK) >> PRESC_SHIFT;
```

## Short answer

**Apply the field mask, then shift down to position 0.**[^iso-c-n1570]

`reg & PRESC_MASK` keeps only bits [6:4], `>> PRESC_SHIFT` brings them to the value 0..7.

Rule: for each field define a MASK+SHIFT pair and use them consistently.[^embeddedinterviewlab]

## Detailed explanation

TODO
