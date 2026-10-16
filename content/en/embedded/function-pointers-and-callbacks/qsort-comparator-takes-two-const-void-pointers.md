---
id: emb-fnptr-0032
title: "What does a callback for `qsort` look like in C?"
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

The comparator signature is: `int cmp(const void *a, const void *b)`.[^iso-c-n1570]

It returns a negative, zero or positive value to say whether the first element is less than, equal to or greater than the second. Inside the callback you must cast `a` and `b` to pointers to the actual element type.

Rule: `qsort` does not know the element type; the function pointer callback gives it type-specific comparison logic.[^iso-c-n1570]

## Detailed explanation

TODO
