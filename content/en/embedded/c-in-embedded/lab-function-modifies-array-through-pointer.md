---
id: emb-cppfound-0063
title: "What does this function call print?"
track: embedded
section: c-in-embedded
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
void f(int *p, int n){
  p[0]=99;
} int a[3]={1,2,3};
f(a,3);
printf("%d",a[0]);
```

## Short answer

`99`. `a` decays to a pointer, so the function `f` receives `int*` – a pointer to the first element `a[0]`. `p[0] = 99` -> modifies `a[0]` in the caller. Arrays in C are passed by reference (through a pointer to the first element) – the function can modify the original data; if only reading is needed: `const int *p`.[^embeddedinterviewlab]

## Detailed explanation

TODO
