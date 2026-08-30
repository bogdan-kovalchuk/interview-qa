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
---

## Short answer

Якщо register має set/clear/toggle aliases або bit-banding, використовуй їх замість read-modify-write.<br>Інакше захисти critical section: тимчасово disable relevant interrupt або використай atomic primitive, якщо architecture це підтримує.<br><span class="warn">Незахищений read-modify-write може загубити bit, змінений ISR між read і write.</span>[^dou-embedded-interview]
## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
