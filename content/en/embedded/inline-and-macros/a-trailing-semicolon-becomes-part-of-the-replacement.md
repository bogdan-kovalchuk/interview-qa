---
id: emb-macros-0029
title: "Trap: what is wrong with `#define SIZE 256;`?"
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

<span class="warn">The extra semicolon becomes part of the replacement text.</span>

`int a[SIZE];` expands to `int a[256;];`, which is syntactically invalid. In `x = SIZE + 1;`, it becomes `x = 256; + 1;`: the assignment sets `x` to 256, while `+ 1;` is a separate expression with no useful effect.[^iso-c-n1570]

Protection: do not put a semicolon in an object-like macro's replacement list: `#define SIZE 256`.[^iso-c-n1570]

## Detailed explanation

TODO
