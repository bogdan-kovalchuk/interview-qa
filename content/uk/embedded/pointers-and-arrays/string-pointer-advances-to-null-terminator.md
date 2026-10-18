---
id: emb-cppfound-0037
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
char str[] = "hello";
char *p = str;
while(*p) p++;
printf("%td", p-str);
```

## Short answer

`5`.

`str` decay-ується до `char*`, тож цикл йде до `'\0'`: після `'h','e','l','l','o'` – `*p = '\0'` (false) -> стоп. `p` вказує на null-terminator.

`p - str` = 5 елементів = `strlen("hello")`. Це стандартний спосіб реалізації `strlen` через pointer arithmetic, `%td` для `ptrdiff_t`.[^embeddedinterviewlab]

## Detailed explanation

TODO
