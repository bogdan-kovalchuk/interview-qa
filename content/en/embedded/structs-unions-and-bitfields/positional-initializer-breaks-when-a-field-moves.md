---
id: emb-structs-0031
title: "Trap: why is a positional initializer fragile?"
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
struct Cfg { uint32_t baud; uint8_t parity; uint8_t stop; };
struct Cfg c = { 115200, 0, 1 };
```

## Short answer

<span class="warn">Values are bound to field order, not to field names.</span>

If someone inserts a new field between `baud` and `parity`, the initializer may remain syntactically valid, but the values will land in the wrong fields. In driver configs this creates silent runtime bugs.

Defence: for non-trivial structs use designated initializers: `{ .baud = 115200, .parity = 0, .stop = 1 }`.[^iso-c-n1570]

## Detailed explanation

TODO
