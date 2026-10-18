---
id: emb-cemb-0027
title: "Скільки байтів пам'яті займає вказівник?"
track: embedded
section: pointers-and-arrays
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

Залежить від архітектури процесора: **16-bit** -> 2 байти, **32-bit** -> 4 байти, **64-bit** -> 8 байтів. Тип вказівника не має значення: `char *`, `int *`, `struct Foo *` – всі займають однакову кількість байтів. В Embedded (ARM Cortex-M) – завжди 4 байти. Перевірити: `sizeof(void *)`.[^dou-embedded-interview]

## Detailed explanation

TODO
