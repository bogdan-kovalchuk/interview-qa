---
id: emb-cemb-0009
title: "Які є бітові операції?"
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

Основні побітові оператори: `&` AND, `|` OR, `^` XOR, `~` NOT, `<<` зсув вліво, `>>` зсув вправо.[^dou-embedded-interview]

Типові embedded-патерни: перевірити біт – `reg & (1u << n)`; встановити – `reg |= (1u << n)`; скинути – `reg &= ~(1u << n)`; перемкнути – `reg ^= (1u << n)`; створити маску – `(1u << width) - 1`. Для регістрів бажано використовувати unsigned типи, щоб уникати сюрпризів зі знаковими зсувами.

## Detailed explanation

TODO
