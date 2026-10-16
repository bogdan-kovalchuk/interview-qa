---
id: emb-cemb-0019
title: "Яке призначення ключового слова `static`?"
track: embedded
section: c-in-embedded
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

Залежно від контексту `static` робить три різні речі:[^dou-embedded-interview]

1. **Локальна змінна** – зберігає значення між викликами функції, живе весь час програми і не розміщується на стеку.
2. **Глобальна змінна або функція** – обмежує видимість поточним файлом (internal linkage) і захищає від конфліктів імен між `.c` файлами.
3. **Член класу C++** – має одну копію на весь клас, а не окрему копію для кожного об'єкта.

## Detailed explanation

TODO
