---
id: emb-cemb-0034
title: "Чим вказівник відрізняється від масиву у виразах, параметрах функцій і sizeof?"
description: "Практичне питання про embedded-розробку та її обмеження."
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

Масив – це об'єкт із N елементів; у більшості виразів він decay-иться до pointer на перший елемент. У параметрі функції <code>int a[]</code> фактично є <code>int *a</code>, тому довжина не передається автоматично. <code>sizeof array</code> у тій самій scope дає весь розмір масиву, а <code>sizeof pointer</code> – лише розмір адреси.[^dou-embedded-interview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

