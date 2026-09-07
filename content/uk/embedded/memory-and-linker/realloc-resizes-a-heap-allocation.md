---
id: emb-memlink-0003
title: "Для чого використовують realloc?"
description: "realloc змінює розмір раніше виділеного heap-блоку, копіюючи дані в новий блок за потреби, і при помилці лишає старий вказівник валідним."
track: embedded
section: memory-and-linker
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 3
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження цього питання й відповіді; текст відповіді не перевірений незалежно від оригінальної Anki-колоди спільноти."
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
    accessed: 2026-09-06
    kind: official
    version: "2.47"
    applicability: "Авторитетне джерело рівня секції для понять розділу memory-and-linker; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

`realloc(ptr, new_size)` змінює розмір раніше виділеного heap-блоку[^dou-embedded-interview]: якщо поруч є місце, блок розширюється на місці; інакше виділяється новий блок, старі дані копіюються, а старий звільняється.

Типове використання – динамічні масиви, буфери вводу, рядки змінної довжини. Важливий патерн: `tmp = realloc(ptr, n); if (tmp) ptr = tmp;`, бо при помилці `realloc` повертає `NULL`, але старий `ptr` лишається валідним. `realloc(NULL, size)` працює як `malloc`, а на `realloc(ptr, 0)` portable code не повинен покладатися: на багатьох реалізаціях це поводиться як `free(ptr)`, але деталі залежать від стандарту/реалізації.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
