---
id: emb-macros-0025
title: "When do you choose `static inline` and when a function-like macro?"
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

## Short answer

**`static inline`** is for everything that resembles a function: small helpers, type-safe bit manipulation, computations with arguments (exactly one evaluation of each).

A macro is only for what cannot be a function: working with tokens/names (`#`, `##`), conditional compilation, register address definitions, X-macros, `STATIC_ASSERT`.

Rule: default to `static inline`; a macro is an exception that requires justification.[^iso-c-n1570]

## Detailed explanation

TODO
