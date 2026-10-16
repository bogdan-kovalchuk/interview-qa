---
id: emb-macros-0018
title: "What does `##` before `__VA_ARGS__` mean in a variadic macro?"
track: embedded
section: inline-and-macros
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gcc-cpp-variadic-macros
    title: "GCC CPP: Variadic Macros"
    url: https://gcc.gnu.org/onlinedocs/cpp/Variadic-Macros.html
---

## Question code

```c
#define DBG(fmt, ...) printf(fmt, ##__VA_ARGS__)
```

## Short answer

**`##__VA_ARGS__` removes the trailing comma** when there are no variadic arguments.

With the GNU preprocessor, a call like `DBG("hi")` would leave a comma before the empty variadic argument without special handling; the GNU form removes that comma, producing `printf("hi")`.

This is a GNU extension, not portable standard syntax; C23 and C++20 provide `__VA_OPT__(,)`.[^gcc-cpp-variadic-macros]

## Detailed explanation

TODO
