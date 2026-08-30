---
id: emb-cemb-0019
title: "Яке призначення ключового слова `static`?"
description: "`static` змінює час життя локальної змінної, linkage глобальної змінної або функції та спосіб спільного використання члена класу C++."
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

Залежно від контексту <code>static</code> робить три різні речі:[^dou-embedded-interview]

1. <span class="key">Локальна змінна</span> – зберігає значення між викликами функції, живе весь час програми і не розміщується на стеку.
2. <span class="key">Глобальна змінна або функція</span> – обмежує видимість поточним файлом (internal linkage) і захищає від конфліктів імен між `.c` файлами.
3. <span class="key">Член класу C++</span> – має одну копію на весь клас, а не окрему копію для кожного об'єкта.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
