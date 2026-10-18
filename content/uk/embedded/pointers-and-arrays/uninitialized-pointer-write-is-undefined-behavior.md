---
id: emb-cppfound-0003
title: "Trap: що відбудеться?"
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
int *p;
*p = 5;
```

## Short answer

`p` – <span class="warn">wild pointer</span>: неініціалізований вказівник містить garbage-адресу (випадкове значення зі стека).

Запис `*p = 5` -> undefined behavior: може перезаписати випадкову область пам'яті, іншу змінну, або спричинити <span class="warn">HardFault</span> на Cortex-M (якщо адреса поза RAM).

Захист: завжди ініціалізуй вказівники: `int *p = NULL;` або одразу `int *p = &x;`[^embeddedinterviewlab]

## Detailed explanation

TODO
