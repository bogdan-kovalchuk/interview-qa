---
id: emb-cppfound-0090
title: "Знайдіть помилку: чи переміститься зовнішній pointer?"
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
void advance(char *p, int n){
  p += n;
}
```

## Short answer

<span class="warn">НІ.</span> У C параметри передаються **за значенням**. Функція отримує копію вказівника `p`. `p += n` змінює локальну копію, але не оригінальний вказівник у caller-і.

Для зміни caller-ського pointer: потрібен double pointer: `void advance(char **p, int n){ *p += n; }` Виклик: `advance(&cursor, 5);`

Класична помилка при реалізації парсерів і потокових обробників.[^embeddedinterviewlab]

## Detailed explanation

TODO
