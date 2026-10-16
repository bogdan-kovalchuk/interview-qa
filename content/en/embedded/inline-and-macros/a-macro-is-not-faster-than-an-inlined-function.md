---
id: emb-macros-0026
title: "Trap: is it true that a macro is always faster than a function?"
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

<span class="warn">No – this is an outdated myth.</span>

Modern compilers inline small `static inline` functions the same way a macro expands, and additionally apply constant folding, dead-code elimination, and other optimizations unavailable to already-substituted preprocessor text.

Protection: at an interview do not say 'a macro is faster'; say '`static inline` gives the same speed plus type safety and single evaluation of arguments'.[^iso-c-n1570]

## Detailed explanation

TODO
