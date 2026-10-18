---
id: emb-cppfound-0088
title: "What is printed?"
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
int a=1,b=2;
int *p=&a,*q=&b;
printf("%d", p<q);
```

## Short answer

<span class="warn">Undefined behavior per the C standard</span>. Relational comparison (`<`, `>`) of pointers from different objects is not defined by the standard.

In practice (most platforms, flat memory): the result depends on variable placement in memory (stack order is compiler-dependent). Not portable;

Allowed: `p == q`, `p != q` – equality comparison between any pointers. Relational comparisons – only within a single array.[^embeddedinterviewlab]

## Detailed explanation

TODO
