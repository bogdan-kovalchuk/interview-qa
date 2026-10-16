---
id: emb-macros-0042
title: "What is a variadic macro and what is `__VA_ARGS__` for?"
track: embedded
section: inline-and-macros
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gcc-variadic-macros
    title: "GCC: Variadic Macros"
    url: https://gcc.gnu.org/onlinedocs/gcc-8.1.0/cpp/Variadic-Macros.html
---

## Question code

```c
#define LOG(fmt, ...) \
  printf("[%lu] " fmt, tick(), __VA_ARGS__)
```

## Short answer

**A variadic macro accepts a variable number of arguments** via `...`, and `__VA_ARGS__` substitutes them into the body.

This allows building wrappers around `printf`-like functions, adding prefixes (timestamp, log level) and forwarding the remaining arguments.

In standard C, `__VA_OPT__` is available in C23; `##__VA_ARGS__` to remove the comma is a GNU extension, not a portable C rule.[^gcc-variadic-macros]

## Detailed explanation

TODO
