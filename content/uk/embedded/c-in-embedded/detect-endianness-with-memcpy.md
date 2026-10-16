---
id: emb-cemb-0035
title: "Як визначити endianness системи без порушення strict aliasing?"
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

Безпечно записати integer і скопіювати його bytes через `memcpy` у `unsigned char` buffer, бо character types можуть представляти object representation. Наприклад, `uint32_t x=1`, `memcpy(b,&x,4)`, потім перевірити `b[0]`. Для portable protocol code краще не залежати від host endianness, а явно збирати/розбирати bytes.[^dou-embedded-interview]

## Detailed explanation

TODO
