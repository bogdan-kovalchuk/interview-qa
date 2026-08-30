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

Безпечно записати integer і скопіювати його bytes через <code>memcpy</code> у <code>unsigned char</code> buffer, бо character types можуть представляти object representation. Наприклад, <code>uint32_t x=1</code>, <code>memcpy(b,&amp;x,4)</code>, потім перевірити <code>b[0]</code>. Для portable protocol code краще не залежати від host endianness, а явно збирати/розбирати bytes.[^dou-embedded-interview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
