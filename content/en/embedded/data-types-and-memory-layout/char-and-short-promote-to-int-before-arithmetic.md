---
id: emb-dtypes-0077
title: "What is the promotion rule, and how does C handle expressions with `char` and `short`?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**Integer promotion** converts narrow integer operands before operations for which the standard requires promotions: a value becomes `int` if it can represent every value of the original type, and otherwise `unsigned int`.[^iso-c-n1570] Thus `uint8_t`, when that optional typedef is available, commonly promotes to `int`, but the result of bitwise `~` has type `int`, not `uint8_t`. Converting the result back to `uint8_t` narrows it; do not rely on a particular representation of negative `int` in a portable example.[^iso-c-n1570]

## Detailed explanation

TODO
