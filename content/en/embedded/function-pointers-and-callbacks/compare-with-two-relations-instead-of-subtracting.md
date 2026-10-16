---
id: emb-fnptr-0034
title: "What is a safer way to write a `qsort` comparator for `int`?"
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

Like this:

`return (x > y) - (x < y);`

Full fragment: `const int x = *(const int *)a; const int y = *(const int *)b;`. Such a comparator returns `1`, `0` or `-1` without signed overflow.

Rule: a comparator must determine ordering consistently for the same values; qsort uses the result sign to distinguish less, equal, and greater.[^iso-c-n1570]

## Detailed explanation

TODO
