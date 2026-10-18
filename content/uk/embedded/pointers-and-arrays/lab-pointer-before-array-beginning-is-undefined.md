---
id: emb-cppfound-0071
title: "Trap: UB?"
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
int arr[3]={1,2,3};
int *p=arr;
p--;
printf("%d",*p);
```

## Short answer

<span class="warn">Так, undefined behavior (UB).</span> `p = arr` -> вказівник на `arr[0]`. `p--` -> `arr-1`, що знаходиться <span class="warn">поза масивом</span>.

Допустимі вказівники для `arr[3]`: `arr` (=arr+0) до `arr+3` (one-past-the-end). `arr-1` – UB вже при формуванні, не тільки при розіменуванні.

Компілятор може припустити що UB не відбувається -> непередбачувані оптимізації; Отже, arr-1 формувати не можна.[^embeddedinterviewlab]

## Detailed explanation

TODO
