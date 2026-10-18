---
id: emb-cemb-0028
title: "Які існують бітові операції?"
track: embedded
section: common-code-patterns
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

`&` AND – скидання біта: `reg &= ~(1<<n)` `|` OR – встановлення біта: `reg |= (1<<n)` `^` XOR – інвертування: `reg ^= (1<<n)` `~` NOT – побітова інверсія `<<` зсув вліво: `x << 3` = x × 8 `>>` зсув вправо: `x >> 1` = x / 2.

Типові патерни в Embedded: Перевірити біт: `if (reg & (1<<n))` Встановити: `reg |= (1<<n)` Скинути: `reg &= ~(1<<n)` Перемкнути: `reg ^= (1<<n)`.[^dou-embedded-interview]

## Detailed explanation

TODO
