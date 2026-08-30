---
id: emb-build-0008
title: "Як відрізняються статична і динамічна бібліотека на етапах build та link?"
description: "Практичне питання про embedded-розробку та її обмеження."
track: embedded
section: toolchain-and-build
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

<span class="key">Static library</span> (<code>.a</code>/<code>.lib</code>) копіюється linker-ом у firmware або executable тільки потрібними object files. <span class="key">Dynamic library</span> (<code>.so</code>/<code>.dll</code>) підвантажується loader-ом у runtime і лишається окремим артефактом. Для bare-metal MCU зазвичай використовують static linking; Embedded Linux часто підтримує обидва варіанти.[^dou-embedded-interview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

