---
id: emb-macros-0004
title: "What does this code actually compute?"
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
#define SQUARE(x) x * x
int r = SQUARE(2 + 3);
```

## Short answer

`r == 11`, not <span class="warn">25</span>.

A macro is text substitution without parentheses, so `SQUARE(2 + 3)` expands to `2 + 3 * 2 + 3`. By precedence rules, `3 * 2 = 6` is computed first, then `2 + 6 + 3 = 11`.

Fix: `#define SQUARE(x) ((x) * (x))` – then the result is `((2 + 3) * (2 + 3)) = 25`.[^iso-c-n1570]

## Detailed explanation

TODO
