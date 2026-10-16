---
id: emb-structs-0022
title: "Trap: why is a one-bit signed bit-field almost always a trap?"
track: embedded
section: structs-unions-and-bitfields
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
struct F {
    signed int flag : 1;
};
```

## Short answer

<span class="warn">In two's complement, a 1-bit signed field has only the values `0` and `-1`, so it is not a boolean `0/1`.</span>

On a typical two's complement implementation, storing `1` yields `-1`, so `flag == 1` fails. Conversion of an unrepresentable value depends on C's rules and the implementation.[^iso-c-n1570]

For a flag, use `_Bool` (or `bool` from `<stdbool.h>` in C versions before C23) when you need logical `0/1` values; an `unsigned int` bit-field can be used when a one-bit unsigned representation is intended.[^iso-c-n1570]

## Detailed explanation

TODO
