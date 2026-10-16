---
id: emb-macros-0010
title: "Why is a statement macro wrapped in `do { ... } while(0)`?"
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
#define LOG_ERR(m) do { \
    uart_puts("[ERR] "); \
    uart_puts(m); \
} while (0)
```

## Short answer

**So that a multi-statement macro behaves as a single statement** and works correctly with `if/else` and a semicolon.

`do { ... } while(0)` forms a single block that requires a `;` at the call site, so `if (c) LOG_ERR(x); else ...` compiles correctly.

For a multi-action statement macro, this idiom preserves the expected `if/else` structure; a trailing backslash continues the preprocessor directive onto the next line.[^iso-c-n1570]

## Detailed explanation

TODO
