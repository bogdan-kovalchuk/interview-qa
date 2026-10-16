---
id: emb-macros-0005
title: "Trap: what is wrong with the call `MAX(++x, y)`?"
track: embedded
section: inline-and-macros
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
#define MAX(a, b) ((a) > (b) ? (a) : (b))
```

## Short answer

<span class="warn">Double evaluation</span>: the parameter `a` appears twice in the body, so `++x` executes twice when the condition is true.

Expansion: `((++x) > (y) ? (++x) : (y))` – `x` is incremented a second time in the true branch. Any argument with a side effect (`++`, `--`, a function call, reading a volatile register) produces an unexpected result.

Fix: use a `static inline` function – it evaluates its argument exactly once.[^iso-c-n1570]

## Detailed explanation

TODO
