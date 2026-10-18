---
id: emb-cemb-0009
title: "What bitwise operations are there?"
track: embedded
section: common-code-patterns
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

The main bitwise operators: `&` AND, `|` OR, `^` XOR, `~` NOT, `<<` left shift, `>>` right shift.[^dou-embedded-interview]

Common embedded patterns: test a bit – `reg & (1u << n)`; set – `reg |= (1u << n)`; clear – `reg &= ~(1u << n)`; toggle – `reg ^= (1u << n)`; build a mask – `(1u << width) - 1`. For registers, prefer unsigned types to avoid surprises with signed shifts.

## Detailed explanation

TODO
