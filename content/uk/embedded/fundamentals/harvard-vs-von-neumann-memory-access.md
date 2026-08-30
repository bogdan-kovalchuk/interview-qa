---
id: emb-fund-0017
title: "Чим архітектура Harvard відрізняється від von Neumann і як це впливає на доступ до Flash/RAM?"
description: "У von Neumann code і data ділять один address space/bus. У Harvard instruction і data memories/buses розділені, тому Flash і RAM можуть мати різні пра…"
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

У <span class="key">von Neumann</span> code і data ділять один address space/bus. У <span class="key">Harvard</span> instruction і data memories/buses розділені, тому Flash і RAM можуть мати різні правила доступу. На деяких MCU читання constants із program memory потребує спеціальних instructions/API, а self-programming Flash має обмеження по erase/write і timing.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

