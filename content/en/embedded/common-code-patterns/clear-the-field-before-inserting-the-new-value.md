---
id: emb-patterns-0017
title: "How do you write a multi-bit field without disturbing the other bits?"
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
reg = (reg & ~PRESC_MASK)
    | ((value << PRESC_SHIFT) & PRESC_MASK);
```

## Short answer

**First clear the field bits (`& ~MASK`), then insert the new value (shifted and masked).**

Masking the shifted value limits the result to the field bits only when the shift itself is valid; check `value` before shifting.[^iso-c-n1570]

Clear the old field bits before inserting the new value so neighboring settings are preserved.[^iso-c-n1570]

## Detailed explanation

TODO
