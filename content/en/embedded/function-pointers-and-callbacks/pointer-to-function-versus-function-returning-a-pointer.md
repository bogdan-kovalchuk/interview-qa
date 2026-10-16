---
id: emb-fnptr-0003
title: "Trap: how do `void (*f)(void)` and `void *f(void)` differ?"
track: embedded
section: function-pointers-and-callbacks
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

<span class="warn">These are completely different types.</span>

`void (*f)(void)` – variable `f` is a pointer to function returning void. `void *f(void)` – function `f` that takes nothing and returns `void *`.

To distinguish them, start reading the declaration at the name and move outward through its parentheses.[^iso-c-n1570]

## Detailed explanation

TODO
