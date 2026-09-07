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
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу c-in-embedded; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

Залежно від контексту `static` робить три різні речі:[^dou-embedded-interview]

1. **Локальна змінна** – зберігає значення між викликами функції, живе весь час програми і не розміщується на стеку.
2. **Глобальна змінна або функція** – обмежує видимість поточним файлом (internal linkage) і захищає від конфліктів імен між `.c` файлами.
3. **Член класу C++** – має одну копію на весь клас, а не окрему копію для кожного об'єкта.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
