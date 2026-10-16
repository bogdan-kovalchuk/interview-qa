---
id: emb-cppfound-0093
title: "Що виведе?"
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
int arr[4]={10,20,30,40};
printf("%d %d",*(arr+3), arr[3]);
```

## Short answer

Обидва виводять `40`.

`*(arr+3)` -> pointer arithmetic: зсув на 3 елементи, розіменування = `arr[3] = 40`. `arr[3]` -> subscript operator, за визначенням = `*(arr+3)`.

Вони **ідентичні за стандартом**. Компілятор генерує однаковий машинний код для обох варіантів.[^embeddedinterviewlab]

## Detailed explanation

TODO
