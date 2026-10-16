---
id: emb-cemb-0037
title: "How is bit-field width specified, and what determines its memory layout?"
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

The width is specified after a colon: `unsigned field : 5;`. The layout depends on the compiler ABI: placement order, alignment allocation unit, padding, and packing rules are not universal. Therefore bit-fields are suitable for local compact state, but not as a portable binary layout.[^dou-embedded-interview]

## Detailed explanation

TODO
