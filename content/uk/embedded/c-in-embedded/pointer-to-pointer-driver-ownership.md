---
id: emb-cemb-0038
title: "Для чого використовують pointer-to-pointer у драйверах, API виділення ресурсів і linked structures?"
description: "Pointer-to-pointer дозволяє API змінити pointer у caller-а, повернути handle або оновити head/tail структури."
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

<code>T **</code> потрібен, коли функція має змінити pointer у caller-а: видати handle, додати node в list head або повернути buffer із pool. У драйверах це часто виглядає як <code>driver_open(dev_t **out)</code> або queue API, що оновлює head/tail. Важливо документувати ownership: хто після цього звільняє або повертає ресурс.[^dou-embedded-interview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
