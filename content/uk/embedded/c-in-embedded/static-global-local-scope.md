---
id: emb-cemb-0020
title: "Як `static` впливає на глобальні та локальні змінні?"
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

Для **локальної змінної** `static` змінює час життя: змінна створюється один раз, живе до завершення програми й зберігає значення між викликами функції. Область видимості при цьому лишається локальною для блоку.

Для **глобальної змінної** або функції `static` змінює linkage: ім'я видно тільки в поточному `.c`/`.cpp` файлі. Це називається internal linkage і допомагає уникати конфліктів імен між translation units.[^dou-embedded-interview]

## Detailed explanation

TODO
