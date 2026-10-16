---
id: emb-cppfound-0032
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
int arr[]={1,2,3,4,5};
int *p=arr+4;
int *q=arr+1;
printf("%td", p-q);
```

## Short answer

`3`.

Відняття вказівників (`p - q`) повертає тип `ptrdiff_t` – кількість **елементів між ними**, не байт: `(arr+4) - (arr+1) = 3` елементи.

`%td` – формат для `ptrdiff_t`. Результат може бути від'ємним якщо `q > p`.

Фізично: байтова різниця = `3 * sizeof(int) = 12` байт, але pointer subtraction ділить на `sizeof(int)`.[^embeddedinterviewlab]

## Detailed explanation

TODO
