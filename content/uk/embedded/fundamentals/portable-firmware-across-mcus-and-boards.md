---
id: emb-fund-0020
title: "Як підтримувати один codebase для різних MCU, плат і peripheral configurations?"
description: "Розділяй portable core, MCU-specific drivers, board support package і configuration data.Hardware differences описуй через target-specific build optio…"
track: embedded
section: fundamentals
level: senior
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
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? fundamentals; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

Розділяй <span class="key">portable core</span>, MCU-specific drivers, board support package і configuration data.<br>Hardware differences описуй через target-specific build options, linker scripts, pin/clock tables і devicetree-like конфігурацію, а не через хаотичні <code>#ifdef</code> по всій логіці.<br>CI має збирати ключові variants, щоб divergence ловився рано.[^dou-embedded-interview]
## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
