---
id: emb-memlink-0008
title: "Що буде, якщо двічі викликати `free`?"
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

Повторний `free(ptr)` для того самого виділеного блоку – це <span class="warn">double free</span> і undefined behavior.[^dou-embedded-interview] Наслідки можуть бути різні: crash, пошкодження heap metadata, випадкові помилки пізніше або security vulnerability.

Безпечний патерн: після звільнення обнулити вказівник – `free(ptr); ptr = NULL;`. Виклик `free(NULL)` дозволений і нічого не робить, тому обнулення зменшує ризик повторного звільнення. Але якщо є кілька копій одного вказівника, треба контролювати ownership, а не покладатися тільки на `NULL`.

## Detailed explanation

TODO
