---
id: emb-cemb-0030
title: "Що таке padding у структурі і чому порядок полів може змінити її розмір?"
description: "Padding – це байти, які компілятор додає для alignment; порядок полів від більших alignment-вимог до менших часто зменшує розмір структури."
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

<span class="key">Padding</span> – невикористані байти, які компілятор додає для alignment наступного поля або всієї структури. Якщо розташувати поля від більших alignment-вимог до менших, padding часто зменшується. <span class="warn">Не можна покладатися на padding bytes як на стабільні дані</span>: вони можуть бути неініціалізовані й не підходять для прямого порівняння чи передачі по шині.[^dou-embedded-interview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
