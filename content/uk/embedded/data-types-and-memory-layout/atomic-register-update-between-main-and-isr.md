---
id: emb-dtypes-0104
title: "Як забезпечити atomic register update, якщо один регістр змінюють main code і ISR?"
description: "Якщо register має set/clear/toggle aliases або bit-banding, використовуй їх замість read-modify-write.Інакше захисти critical section: тимчасово disab…"
track: embedded
section: data-types-and-memory-layout
level: senior
type: pitfall
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
    applicability: "Авторитетне джерело рівня секції для понять розділу data-types-and-memory-layout; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

Якщо register має set/clear/toggle aliases або bit-banding, використовуй їх замість read-modify-write. Інакше захисти critical section: тимчасово disable relevant interrupt або використай atomic primitive, якщо architecture це підтримує. <span class="warn">Незахищений read-modify-write може загубити bit, змінений ISR між read і write.</span>[^dou-embedded-interview]

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
