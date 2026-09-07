---
id: emb-memlink-0005
title: "Чим відрізняється stack від heap?"
description: "Stack автоматично керує локальними змінними за принципом LIFO, а heap виділяється вручну через malloc/free і має ризик фрагментації."
track: embedded
section: memory-and-linker
level: junior
type: comparison
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

**Stack** – автоматична пам'ять: локальні змінні і адреси повернення функцій, керується компілятором/CPU за принципом LIFO.[^dou-embedded-interview] Швидкий доступ, обмежений розмір, звільнення автоматичне при виході з функції.

**Heap** – динамічна пам'ять: виділяється вручну через `malloc`/`free`. Більший обсяг, але повільніший доступ і ризик фрагментації; потребує явного звільнення.

В Embedded стараються уникати heap через недетермінованість: межі stack і heap задаються у linker script.

## Detailed explanation

TODO

## Comparison

TODO

## When to choose which

TODO

## Sources

<!-- generated from frontmatter -->
