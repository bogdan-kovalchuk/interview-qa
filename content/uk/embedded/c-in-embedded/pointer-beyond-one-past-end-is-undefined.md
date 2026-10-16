---
id: emb-cppfound-0041
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
int arr[4]={0};
int *p=arr;
p+=5;
*p=1;
```

## Short answer

<span class="warn">Так, undefined behavior (UB)</span> (навіть без розіменування).

Формування вказівника `p += 5` виходить за межі масиву більш ніж на 1: `arr` має 4 елементи, тому валідні вказівники: `arr` до `arr+4` (включно "one-past-the-end"). `arr+5` -> UB вже при формуванні.

One-past-the-end (`arr+4`) – дозволено формувати, але <span class="warn">не розіменовувати</span>.[^embeddedinterviewlab]

## Detailed explanation

TODO
