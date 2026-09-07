---
id: emb-cemb-0029
title: "Для чого потрібне вирівнювання структур у C і як воно впливає на layout у пам'яті?"
description: "Alignment визначає адреси полів структури, а padding може змінити її фактичний memory layout і розмір."
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

**Alignment** змушує поля структури починатися з адрес, кратних вимогам їхніх типів або ABI. Компілятор може вставляти padding між полями й у кінці структури, тому фактичний layout не завжди дорівнює сумі розмірів полів.[^dou-embedded-interview] Для DMA, MMIO mirror-структур і binary protocol це критично: layout треба фіксувати явно або серіалізувати вручну.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
