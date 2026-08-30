---
id: emb-fund-0013
title: "Чим блокуючі операції відрізняються від неблокуючих у драйверах і I/O API?"
description: "Blocking call засинає або чекає, поки data/resource стане доступним, наприклад <code>read</code> з порожнього device queue."
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

Blocking call засинає або чекає, поки data/resource стане доступним, наприклад <code>read</code> з порожнього device queue. Non-blocking call одразу повертає <code>EAGAIN</code>/<code>EWOULDBLOCK</code>, якщо операцію не можна виконати. У драйверах це впливає на wait queues, poll/select/epoll support, timeout-и й те, чи можна викликати API з конкретного context.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

