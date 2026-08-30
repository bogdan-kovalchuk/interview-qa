---
id: emb-cemb-0002
title: "Як працювати з `void`?"
description: "`void` означає відсутність типу і використовується для функції без повернення, функції без параметрів і як узагальнений вказівник `void *`."
track: embedded
section: c-in-embedded
level: junior
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

`void` означає «відсутність типу». Три використання:[^dou-embedded-interview]

- **Функція без повернення**: `void init(void);`
- **Функція без параметрів**: `int get(void);` – у C `int f()` і `int f(void)` різняться!
- **Узагальнений вказівник**: `void *ptr` – вказівник на будь-який object type; його не можна напряму розіменувати або робити над ним стандартну pointer arithmetic.

У C `void *` неявно конвертується в object pointer, але перед доступом треба мати конкретний тип: `int *p = ptr;`. У C++ таке перетворення потребує явного cast.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
