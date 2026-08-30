---
id: emb-cemb-0037
title: "Як задається ширина bit-field і від чого залежить його layout у пам'яті?"
description: "Ширина bit-field задається після двокрапки, але його фактичний layout залежить від ABI та компілятора."
track: embedded
section: c-in-embedded
level: middle
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
---

## Short answer

Ширина задається після двокрапки: <code>unsigned field : 5;</code>. Layout залежить від compiler ABI: порядок розміщення, alignment allocation unit, padding і packing rules не є універсальними. Тому bit-fields годяться для локального компактного state, але не як переносимий binary layout.[^dou-embedded-interview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
