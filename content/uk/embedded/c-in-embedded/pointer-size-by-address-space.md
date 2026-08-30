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
updated: 2026-09-06
content_revision: 1
reconciled_with:
  en: 1
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
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? c-in-embedded; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

Залежить від архітектури процесора: <span class="key">16-bit</span> -> 2 байти, <span class="key">32-bit</span> -> 4 байти, <span class="key">64-bit</span> -> 8 байтів. Тип вказівника не має значення: <code>char *</code>, <code>int *</code>, <code>struct Foo *</code> – всі займають однакову кількість байтів. В Embedded (ARM Cortex-M) – завжди 4 байти. Перевірити: <code>sizeof(void *)</code>.[^dou-embedded-interview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
