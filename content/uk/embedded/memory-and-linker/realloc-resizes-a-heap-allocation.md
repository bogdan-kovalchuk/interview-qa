---
id: emb-memlink-0003
title: "Для чого використовують realloc?"
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

`realloc(ptr, new_size)` змінює розмір раніше виділеного heap-блоку[^dou-embedded-interview]: якщо поруч є місце, блок розширюється на місці; інакше виділяється новий блок, старі дані копіюються, а старий звільняється.

Типове використання – динамічні масиви, буфери вводу, рядки змінної довжини. Важливий патерн: `tmp = realloc(ptr, n); if (tmp) ptr = tmp;`, бо при помилці `realloc` повертає `NULL`, але старий `ptr` лишається валідним. `realloc(NULL, size)` працює як `malloc`, а на `realloc(ptr, 0)` portable code не повинен покладатися: на багатьох реалізаціях це поводиться як `free(ptr)`, але деталі залежать від стандарту/реалізації.

## Detailed explanation

TODO
