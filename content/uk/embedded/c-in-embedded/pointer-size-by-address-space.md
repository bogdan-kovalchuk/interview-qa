---
id: emb-cemb-0027
title: "Скільки байтів пам'яті займає вказівник?"
description: "Розмір вказівника визначається адресним простором архітектури: зазвичай 2 байти для 16-bit, 4 для 32-bit і 8 для 64-bit."
track: embedded
section: c-in-embedded
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження цього питання й відповіді; текст відповіді не перевірений незалежно від оригінальної Anki-колоди спільноти."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу c-in-embedded; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

Залежить від архітектури процесора: **16-bit** -> 2 байти, **32-bit** -> 4 байти, **64-bit** -> 8 байтів. Тип вказівника не має значення: `char *`, `int *`, `struct Foo *` – всі займають однакову кількість байтів. В Embedded (ARM Cortex-M) – завжди 4 байти. Перевірити: `sizeof(void *)`.[^dou-embedded-interview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
