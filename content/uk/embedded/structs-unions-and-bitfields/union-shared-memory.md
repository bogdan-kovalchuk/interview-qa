---
id: emb-cemb-0024
title: "Що таке `union`?"
track: embedded
section: structs-unions-and-bitfields
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

`union` – тип, у якому всі поля ділять одну й ту саму область пам'яті. У кожен момент логічно активним є одне поле, а запис в одне поле перезаписує байти, які могли використовуватись іншими полями.

Приклад: `union U { uint32_t word; uint8_t bytes[4]; };`. Використовується для економії пам'яті, варіантних даних, низькорівневого доступу до представлення байтів. Треба бути обережним із type punning, endianness, alignment і правилами активного member-а, особливо в C++.[^dou-embedded-interview]

## Detailed explanation

TODO
