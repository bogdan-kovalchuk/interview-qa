---
id: emb-cppfound-0045
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
int x=10;
int *p=&x;
int **pp=&p;
**pp=20;
printf("%d",x);
```

## Short answer

`20`.

Chain: `pp` -> `&p` (address of pointer `p`), `*pp` -> dereference = the pointer `p` itself (address of `x`), `**pp` -> double dereference = the value of `x`.

`**pp = 20` -> writes 20 into `x` through the chain, so `x` becomes 20. All three: `x`, `*p`, `**pp` are now = 20.[^embeddedinterviewlab]

## Detailed explanation

TODO
