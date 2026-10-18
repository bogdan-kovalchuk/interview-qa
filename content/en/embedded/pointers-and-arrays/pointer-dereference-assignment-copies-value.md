---
id: emb-cppfound-0027
title: "What does this print?"
track: embedded
section: pointers-and-arrays
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
int a=5, b=10;
int *p=&a, *q=&b;
*p=*q;
printf("%d %d",a,b);
```

## Short answer

`a=10, b=10`.

`*p = *q` copies the **value** of `*q` (that is, `b=10`) into `*p` (that is, into `a`). The pointers `p` and `q` themselves do not change.

If it were `p = q` (without *) – both pointers would point to `b`, and `a` would remain `5`.

Common mistake: confusing pointer assignment with value assignment.[^embeddedinterviewlab]

## Detailed explanation

TODO
