---
id: emb-macros-0031
title: "Trap: why can `inline` without `static` produce a linker error in C?"
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

In C99+, a definition of a function with external linkage declared simply `inline` is an inline definition, not an external definition; by itself, it does not guarantee an external symbol for the linker.[^iso-c-n1570]

If a call needs an external definition but no translation unit provides one, the linker may report a missing symbol. The compiler is not required to inline the call.[^iso-c-n1570]

For a function defined in a header separately in each translation unit, a common choice is `static inline`, which gives it internal linkage in each translation unit.[^iso-c-n1570]

## Detailed explanation

TODO
