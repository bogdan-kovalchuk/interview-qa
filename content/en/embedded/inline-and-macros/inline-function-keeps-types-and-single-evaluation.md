---
id: emb-macros-0007
title: "What is an `inline` function and why is it better than a function-like macro?"
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

**`inline`** is a real function that the compiler may expand at the call site; the keyword does not guarantee this transformation.[^iso-c-n1570]

Unlike a macro, it preserves type checking and scope and evaluates an argument once for a function call. The compiler decides whether to inline it or emit a regular call.[^iso-c-n1570]

Rule: anything that looks like a function, make it `inline`/`static inline`, not a function-like macro.[^embeddedinterviewlab]

## Detailed explanation

TODO
