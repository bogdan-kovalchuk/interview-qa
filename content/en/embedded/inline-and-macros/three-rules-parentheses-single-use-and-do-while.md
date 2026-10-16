---
id: emb-macros-0006
title: "What are the three rules of a safe function-like macro?"
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

1. **Parentheses around every use of a parameter**: `(x)`;
2. **Parentheses around the whole expression**: `((x) + (y))`;
3. **Wrap a statement macro in `do { ... } while(0)`** so it behaves correctly with `if/else` and requires a `;`.

Rule: these three points eliminate most classic macro bugs – precedence, truncated expressions and broken control flow.[^iso-c-n1570]

## Detailed explanation

TODO
