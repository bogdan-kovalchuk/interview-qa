---
id: emb-memlink-0008
title: "Що буде, якщо двічі викликати `free`?"
description: "Повторний `free` того самого блоку є double free і undefined behavior, що може пошкодити heap або спричинити аварію."
track: embedded
section: memory-and-linker
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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
    applicability: "Авторитетне джерело рівня секції для понять розділу memory-and-linker; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

Повторний `free(ptr)` для того самого виділеного блоку – це <span class="warn">double free</span> і undefined behavior.[^dou-embedded-interview] Наслідки можуть бути різні: crash, пошкодження heap metadata, випадкові помилки пізніше або security vulnerability.

Безпечний патерн: після звільнення обнулити вказівник – `free(ptr); ptr = NULL;`. Виклик `free(NULL)` дозволений і нічого не робить, тому обнулення зменшує ризик повторного звільнення. Але якщо є кілька копій одного вказівника, треба контролювати ownership, а не покладатися тільки на `NULL`.

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
