---
id: emb-cemb-0037
title: "Як задається ширина bit-field і від чого залежить його layout у пам'яті?"
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

Ширина задається після двокрапки: `unsigned field : 5;`. Layout залежить від compiler ABI: порядок розміщення, alignment allocation unit, padding і packing rules не є універсальними. Тому bit-fields годяться для локального компактного state, але не як переносимий binary layout.[^dou-embedded-interview]

## Detailed explanation

TODO
