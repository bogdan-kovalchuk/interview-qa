---
id: emb-dtypes-0017
title: "How does a `static` local variable differ from a plain local one?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**Plain local** has automatic storage duration: it exists during its block, has an indeterminate value without initialization, and need not be stored on a stack.[^iso-c-n1570]

**Static local** has static storage duration: it exists for the program's execution and is zero-initialized if no explicit initializer is provided. It retains its value between entries to the block; `.bss` and `.data` are typical implementation sections, not language requirements.[^iso-c-n1570]

Shared mutable `static` state can break reentrancy or cause a data race, but the keyword alone does not make a function unsafe for threads.[^iso-c-n1570]

## Detailed explanation

TODO
