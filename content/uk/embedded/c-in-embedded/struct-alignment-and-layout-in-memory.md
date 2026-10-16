---
id: emb-cemb-0029
title: "Для чого потрібне вирівнювання структур у C і як воно впливає на layout у пам'яті?"
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

**Alignment** змушує поля структури починатися з адрес, кратних вимогам їхніх типів або ABI. Компілятор може вставляти padding між полями й у кінці структури, тому фактичний layout не завжди дорівнює сумі розмірів полів.[^dou-embedded-interview] Для DMA, MMIO mirror-структур і binary protocol це критично: layout треба фіксувати явно або серіалізувати вручну.

## Detailed explanation

TODO
