---
id: emb-cppfound-0020
title: "Що виведе?"
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
int a=1,b=2,c=3;
int *arr[3]={&a,&b,&c};
printf("%d",*arr[1]);
```

## Short answer

`2`.

`int *arr[3]` – масив з 3 вказівників на `int`. `arr[1]` -> другий елемент = `&b`. `*arr[1]` -> розіменування `&b` -> значення `b = 2`.

Зберігання: `arr` – масив адрес (3 × 4 байти = 12 байт). Кожен елемент – окрема адреса; Зміна `*arr[1] = 99` -> змінить `b`.[^embeddedinterviewlab]

## Detailed explanation

TODO
