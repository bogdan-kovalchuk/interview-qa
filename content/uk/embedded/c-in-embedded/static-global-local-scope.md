---
id: emb-cemb-0020
title: "Як `static` впливає на глобальні та локальні змінні?"
description: "У локальної змінної `static` змінює час життя, а у глобальної змінної або функції обмежує linkage поточним файлом."
track: embedded
section: c-in-embedded
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
---

## Short answer

Для <span class="key">локальної змінної</span> <code>static</code> змінює час життя: змінна створюється один раз, живе до завершення програми й зберігає значення між викликами функції. Область видимості при цьому лишається локальною для блоку.[^dou-embedded-interview]

Для <span class="key">глобальної змінної</span> або функції <code>static</code> змінює linkage: ім'я видно тільки в поточному <code>.c</code>/<code>.cpp</code> файлі. Це називається internal linkage і допомагає уникати конфліктів імен між translation units.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
