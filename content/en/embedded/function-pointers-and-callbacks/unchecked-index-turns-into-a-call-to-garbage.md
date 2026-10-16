---
id: emb-fnptr-0020
title: "Trap: what is wrong with a dispatch table without an index check?"
track: embedded
section: function-pointers-and-callbacks
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
typedef void (*handler_t)(void);
static handler_t table[4];

table[opcode]();
```

## Short answer

<span class="warn">If `opcode >= 4`, subscripting is outside the array and the program has undefined behavior; the call target is not necessarily random.</span>

On Cortex-M the result could be a HardFault, an incorrect branch, or another failure, but the C standard guarantees no particular outcome.

Defense: check the index first, then check that the selected handler is not a null pointer; see the C rules for subscripting and calls.[^iso-c-n1570]

## Detailed explanation

TODO
