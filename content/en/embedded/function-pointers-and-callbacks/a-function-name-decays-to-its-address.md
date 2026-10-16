---
id: emb-fnptr-0007
title: "What does this code print?"
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
int add1(int x) { return x + 1; }
int (*op)(int) = add1;
printf("%d", op(41));
```

## Short answer

Prints `42` if the snippet is surrounded by the required declarations and `printf` is available.

In this assignment, the function name `add1` is converted to a pointer to function, so `op = add1` is equivalent to `op = &add1`. The call `op(41)` calls the function through the pointer; in C, both `op(41)` and `(*op)(41)` are permitted forms.[^iso-c-n1570]

## Detailed explanation

TODO
