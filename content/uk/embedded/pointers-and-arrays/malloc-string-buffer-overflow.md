---
id: emb-cppfound-0100
title: "Trap: де помилка?"
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
char *p = malloc(5);
strcpy(p, "hello");
p[5] = '\0';
```

## Short answer

<span class="warn">Buffer overflow.</span> `malloc(5)` – 5 байт, а `"hello"` = `{'h','e','l','l','o','\0'}` – 6 байт включно з null-terminator.

`strcpy(p, "hello")` вже переповнює буфер (6 байт у 5-байтний), і `p[5] = '\0'` – шостий запис за межами.

Правильно: `malloc(strlen("hello") + 1)` = `malloc(6)`, або `strncpy(p, "hello", 5); p[4]='\0';` – обрізати якщо треба.[^embeddedinterviewlab]

## Detailed explanation

TODO
