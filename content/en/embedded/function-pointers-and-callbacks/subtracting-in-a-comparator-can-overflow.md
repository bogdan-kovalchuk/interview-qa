---
id: emb-fnptr-0033
title: "Trap: what is wrong with this `qsort` comparator?"
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

## Question code

```c
int cmp(const void *a, const void *b) {
    return *(const int *)a - *(const int *)b;
}
```

## Short answer

<span class="warn">Subtracting two `int` values can overflow the result; signed overflow is undefined behavior in C.</span>

If one element is `INT_MIN` and the other is `INT_MAX`, the mathematical difference is not representable in `int`; the C standard defines signed overflow as undefined behavior. The comparator must return ordering, not necessarily an arithmetic difference.[^iso-c-n1570]

Protection: use `return (x > y) - (x < y);` after reading `x` and `y`.[^iso-c-n1570]

## Detailed explanation

TODO
