---
id: emb-macros-0049
title: "How does `inline` affect code size in embedded?"
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

**Inline removes call overhead but duplicates the function body at every call site.**

Inlining can remove call overhead, but the optimizer decides whether to do it; repeating a body often increases code, while final size and speed depend on the compiler and target.

Rule: do not treat `inline` as a guarantee of speed or smaller code; inspect image size and measure on the target.[^iso-c-n1570]

## Detailed explanation

TODO
