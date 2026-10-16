---
id: emb-memlink-0011
title: "Яка різниця між `calloc` і `malloc`?"
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

`malloc(size)` виділяє блок пам'яті заданого розміру, але <span class="warn">не ініціалізує</span> його: там можуть бути старі байти. `calloc(n, size)` виділяє пам'ять під `n` елементів по `size` байтів і заповнює її нулями.

Ще одна практична різниця: якісна реалізація `calloc` може перевіряти overflow множення `n * size`, тоді як у ручному `malloc(n * size)` цю перевірку легко забути. Обидві функції повертають `NULL` при помилці й пам'ять треба звільняти через `free`.[^dou-embedded-interview]

## Detailed explanation

TODO
