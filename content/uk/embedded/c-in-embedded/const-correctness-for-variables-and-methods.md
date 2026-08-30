---
id: emb-cemb-0015
title: "Як опрацьовується константність змінних?"
description: "Константність – частина типу, яку компілятор перевіряє при доступі; const можна зняти касту, але запис у реально const-об'єкт – undefined behavior."
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

Константність – це частина типу, яку компілятор враховує під час перевірки доступу.[^dou-embedded-interview] Якщо об'єкт або параметр оголошений `const`, запис через цей шлях заборонений: `void f(const int *p)` може читати `*p`, але не змінювати його.

У C++ `const` також використовується для методів: `int get() const` означає, що метод не змінює логічний стан об'єкта. Можна зняти const через cast, але якщо початковий об'єкт був реально const, запис призводить до undefined behavior. Добра практика: ставити `const` на вхідні дані, які функція не змінює.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
