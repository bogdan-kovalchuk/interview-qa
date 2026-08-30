---
id: emb-cemb-0021
title: "Яка різниця між C-style приведенням типів і C++ приведенням?"
description: "C-style cast може приховати різні операції, тоді як окремі C++ casts явно показують тип і намір перетворення."
track: embedded
section: c-in-embedded
level: junior
type: comparison
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

<span class="key">C-style cast</span> виглядає як <code>(T)x</code> і може виконати одразу різні типи приведень: numeric conversion, зняття <code>const</code>, reinterpretation pointer-ів. Через це він короткий, але нечіткий і може приховати небезпечну операцію.[^dou-embedded-interview]

У C++ краще використовувати явні casts: <code>static_cast</code> для звичайних безпечніших перетворень, <code>const_cast</code> тільки для зміни cv-qualifier-ів, <code>reinterpret_cast</code> для низькорівневої переінтерпретації, <code>dynamic_cast</code> для runtime-перевірки в поліморфних класах. Вони довші, зате показують намір і легше знаходяться в коді.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
