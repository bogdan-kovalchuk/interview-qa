---
id: emb-fund-0016
title: "Що таке copy-on-write і де воно проявляється в Linux fork або memory mapping?"
description: "<span class=\"key\">Copy-on-write</span> дозволяє кільком mappings спільно читати одні physical pages, доки хтось не спробує записати."
track: embedded
section: fundamentals
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
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? fundamentals; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

<span class="key">Copy-on-write</span> дозволяє кільком mappings спільно читати одні physical pages, доки хтось не спробує записати. Після <code>fork</code> parent і child спочатку ділять pages, а при write kernel створює приватну копію сторінки. Це економить RAM і пришвидшує fork, але перший write може мати page fault latency.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

