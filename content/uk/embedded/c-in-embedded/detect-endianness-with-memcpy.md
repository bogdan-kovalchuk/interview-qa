---
id: emb-cemb-0035
title: "Як визначити endianness системи без порушення strict aliasing?"
description: "Безпечне визначення endianness через копіювання object representation у масив байтів без type punning."
track: embedded
section: c-in-embedded
level: middle
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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
    applicability: "Авторитетне джерело рівня секції для понять розділу c-in-embedded; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

Безпечно записати integer і скопіювати його bytes через `memcpy` у `unsigned char` buffer, бо character types можуть представляти object representation. Наприклад, `uint32_t x=1`, `memcpy(b,&x,4)`, потім перевірити `b[0]`. Для portable protocol code краще не залежати від host endianness, а явно збирати/розбирати bytes.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
