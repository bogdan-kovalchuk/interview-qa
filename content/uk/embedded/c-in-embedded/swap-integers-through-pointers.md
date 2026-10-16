---
id: emb-cppfound-0055
title: "Як реалізувати swap двох int через вказівники?"
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

## Short answer

```c
void swap(int *a, int *b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
}
```

Виклик: `int x=5, y=10; swap(&x, &y);` -> `x=10, y=5`.

Без tmp через XOR: `*a^=*b; *b^=*a; *a^=*b;` – але <span class="warn">якщо `a == b`, значення обнулиться</span> (обидва вказівники на один об’єкт, а `x ^ x == 0`). Передавай завжди адреси (через `&` у caller), не значення.[^embeddedinterviewlab]

## Detailed explanation

TODO
