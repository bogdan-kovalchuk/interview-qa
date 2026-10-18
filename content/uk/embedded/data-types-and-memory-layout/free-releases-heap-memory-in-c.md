---
id: emb-memlink-0001
title: "Як звільнити пам'ять в C?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
---

## Short answer

Функцією `free(ptr)` з `<stdlib.h>`.[^dou-embedded-interview] Після виклику всі вказівники на цей блок стають <span class="warn">dangling pointer</span>. Часто корисно обнулити конкретну змінну: `free(ptr); ptr = NULL;`.

Важливий нюанс: це допомагає тільки для цієї pointer variable. Інші копії тієї ж адреси все ще dangling, тому треба контролювати ownership; Правила: звільняти тільки те, що виділено через `malloc`/`calloc`/`realloc`; не робити double free; не звільняти stack/static об'єкти.

## Detailed explanation

TODO
