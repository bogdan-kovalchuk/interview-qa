---
id: emb-memlink-0005
title: "Чим відрізняється stack від heap?"
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

**Stack** – автоматична пам'ять: локальні змінні і адреси повернення функцій, керується компілятором/CPU за принципом LIFO.[^dou-embedded-interview] Швидкий доступ, обмежений розмір, звільнення автоматичне при виході з функції.

**Heap** – динамічна пам'ять: виділяється вручну через `malloc`/`free`. Більший обсяг, але повільніший доступ і ризик фрагментації; потребує явного звільнення.

В Embedded стараються уникати heap через недетермінованість: межі stack і heap задаються у linker script.

## Detailed explanation

TODO
