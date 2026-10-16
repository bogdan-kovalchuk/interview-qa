---
id: emb-cppfound-0096
title: "Trap: що не так?"
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
int **pp;
*pp = malloc(10*sizeof(int));
```

## Short answer

<span class="warn">Wild pointer – UB.</span> `int **pp;` – неініціалізований double pointer, містить garbage-адресу.

`*pp = malloc(...)` – розіменовує `pp` (UB!) і записує адресу виділеної пам'яті за невідомою адресою. Це може зіпсувати будь-яку область пам'яті.

Правильно:

```c
int *p = NULL;
int **pp = &p;
*pp = malloc(10*sizeof(int));
```

Завжди ініціалізуй вказівники перед використанням.[^embeddedinterviewlab]

## Detailed explanation

TODO
