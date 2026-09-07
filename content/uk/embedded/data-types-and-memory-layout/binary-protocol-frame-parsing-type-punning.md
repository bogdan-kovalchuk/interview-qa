---
id: emb-dtypes-0108
title: "Як безпечно парсити binary protocol frame без невалідного type punning і проблем alignment?"
description: "Перевірити довжину frame, потім читати кожне поле з uint8_t буфера через memcpy або byte shifts. Для multi-byte полів явно застосувати le16toh/ntohs. Не кастити wire-format buffer у struct."
track: embedded
section: data-types-and-memory-layout
level: middle
type: pitfall
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
    applicability: "Авторитетне джерело рівня секції для понять розділу data-types-and-memory-layout; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

Перевірити довжину frame, потім читати кожне поле з `uint8_t` буфера через `memcpy` або byte shifts. Для multi-byte полів явно застосувати `le16toh`/`ntohs` або власну конверсію. <span class="warn">Не кастити wire-format buffer у struct</span>, якщо layout, packing, alignment і endianness не зафіксовані та не перевірені.[^dou-embedded-interview]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
