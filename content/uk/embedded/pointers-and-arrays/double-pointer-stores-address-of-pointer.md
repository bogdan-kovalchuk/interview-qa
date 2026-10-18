---
id: emb-cppfound-0021
title: "Що таке double pointer (`int **pp`) і навіщо він потрібен?"
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

## Short answer

**Double pointer** – вказівник, що зберігає адресу іншого вказівника.

Навіщо:
1. **Зміна pointer caller-а**: `void alloc(int **pp){ *pp = malloc(n); }` – без `**` caller не побачить нову адресу;
2. **2D масиви через масиви вказівників**;
3. Просування parse-cursor: `void parse(char **p){ (*p)++; }`.

Читання типу: `int **pp` – "вказівник на вказівник на int"; `*pp` -> вказівник, `**pp` -> значення int.[^embeddedinterviewlab]

## Detailed explanation

TODO
