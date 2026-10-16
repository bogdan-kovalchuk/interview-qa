---
id: emb-cppfound-0051
title: "Trap: UB?"
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
int arr[4]={1,2,3,4};
int *p=arr;
int *q=arr+5;
```

## Short answer

<span class="warn">Так, undefined behavior (UB) вже при формуванні `arr+5`</span>.

Для масиву `arr[4]` (4 елементи) допустимі вказівники: `arr` до `arr+4` включно (one-past-the-end). `arr+5` виходить за one-past-the-end -> <span class="warn">UB навіть без розіменування</span>.

Компілятор може використовувати це припущення для оптимізації, що призводить до непередбачуваної поведінки. GCC з `-fsanitize=undefined` виявить це.[^embeddedinterviewlab]

## Detailed explanation

TODO
