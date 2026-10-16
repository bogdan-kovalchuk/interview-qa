---
id: emb-cemb-0028
title: "What bitwise operations exist?"
track: embedded
section: c-in-embedded
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

`&` AND – clear a bit: `reg &= ~(1<<n)` `|` OR – set a bit: `reg |= (1<<n)` `^` XOR – toggle: `reg ^= (1<<n)` `~` NOT – bitwise inversion `<<` left shift: `x << 3` = x × 8 `>>` right shift: `x >> 1` = x / 2.

Typical patterns in Embedded: Test a bit: `if (reg & (1<<n))` Set: `reg |= (1<<n)` Clear: `reg &= ~(1<<n)` Toggle: `reg ^= (1<<n)`.[^dou-embedded-interview]

## Detailed explanation

TODO
