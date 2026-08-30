---
id: emb-memlink-0001
title: "Як звільнити пам'ять в C?"
description: "Пам'ять, виділену malloc/calloc/realloc, звільняє free(ptr); усі вказівники на блок після цього стають dangling, тож варто одразу обнуляти ptr."
track: embedded
section: memory-and-linker
level: junior
type: concept
tags: []
status: published
updated: 2026-09-06
content_revision: 1
reconciled_with:
  en: 1
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
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? memory-and-linker; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

Функцією `free(ptr)` з `<stdlib.h>`.[^dou-embedded-interview] Після виклику всі вказівники на цей блок стають <span class="warn">dangling pointer</span>. Часто корисно обнулити конкретну змінну: `free(ptr); ptr = NULL;`.

Важливий нюанс: це допомагає тільки для цієї pointer variable. Інші копії тієї ж адреси все ще dangling, тому треба контролювати ownership; Правила: звільняти тільки те, що виділено через `malloc`/`calloc`/`realloc`; не робити double free; не звільняти stack/static об'єкти.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
