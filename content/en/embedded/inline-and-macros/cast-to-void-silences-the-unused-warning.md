---
id: emb-macros-0034
title: "What is the `UNUSED(x)` macro for and what does it look like?"
track: embedded
section: inline-and-macros
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gcc-warning-options-unused
    title: "GCC: Warning Options – unused diagnostics"
    url: https://gcc.gnu.org/onlinedocs/gcc/Warning-Options.html
---

## Question code

```c
#define UNUSED(x) ((void)(x))
```

## Short answer

**Casting an expression to `void` explicitly discards its value**; GCC documents this for `-Wunused-value` and unused locals, while diagnostics depend on compiler and flags.[^gcc-warning-options-unused]

The `UNUSED(x)` macro in the code snippet applies that cast to a parameter, for example `UNUSED(ctx)` in a callback. The expression `x` is still evaluated: casting to `void` does not remove its side effects.[^gcc-warning-options-unused]

This does not silence every parameter warning; GCC documents the `unused` attribute for `-Wunused-parameter`. Suppress locally only when the non-use is intentional.[^gcc-warning-options-unused]

## Detailed explanation

TODO
