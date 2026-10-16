---
id: emb-macros-0008
title: "Why is `static inline` considered the modern replacement for function-like macros?"
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

**`static inline`** combines internal linkage with the ability to be expanded inline.

It goes in a header, provides type safety and single evaluation of arguments, does not create an extra external symbol and does not conflict between translation units (TU): each TU gets its own internal definition or fully inlined code. The compiler chooses between expansion and a call based on optimization.

For small header helpers, `static inline` keeps function typing and call semantics while giving each translation unit internal linkage.[^iso-c-n1570]

## Detailed explanation

TODO
