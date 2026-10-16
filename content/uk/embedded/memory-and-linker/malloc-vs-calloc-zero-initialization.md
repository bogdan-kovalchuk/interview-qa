---
id: emb-memlink-0004
title: "Чим відрізняється malloc від calloc?"
track: embedded
section: memory-and-linker
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
---

## Short answer

`malloc(size)` – виділяє `size` байтів і <span class="warn">не ініціалізує</span> їх[^dou-embedded-interview] (один аргумент), тоді як `calloc(n, size)` – виділяє `n * size` байтів і **ініціалізує їх нулями** (два аргументи; хороша реалізація також перевіряє overflow множення).

Приклад: `int *a = malloc(10 * sizeof(int));` – початкові значення невизначені; `int *b = calloc(10, sizeof(int));` – всі елементи = 0. Обидва повертають `NULL` при помилці.

## Detailed explanation

TODO
