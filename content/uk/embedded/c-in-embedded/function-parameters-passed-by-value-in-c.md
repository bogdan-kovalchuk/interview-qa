---
id: emb-cemb-0007
title: "Як відбувається передача параметрів у функцію?"
description: "У C параметри передаються за значенням як копія; щоб змінити оригінал або уникнути копіювання, передають адресу або, у C++, посилання."
track: embedded
section: c-in-embedded
level: junior
type: mechanism
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

У C параметри передаються **за значенням**: функція отримує копію аргументу.[^dou-embedded-interview] Якщо передати `int x`, зміна параметра всередині функції не змінить змінну caller-а.

Щоб функція могла змінити об'єкт або не копіювати великий об'єкт, передають адресу: `void f(int *p)` або `void g(struct Big *s)`. Масиви в параметрах фактично перетворюються на вказівник на перший елемент, тому розмір масиву окремо треба передавати явно. У C++ додатково є references: `T&` і `const T&`.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
