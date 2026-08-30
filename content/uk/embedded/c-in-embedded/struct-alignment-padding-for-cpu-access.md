---
id: emb-cemb-0010
title: "Що таке вирівнювання в структурах?"
description: "Вирівнювання розміщує поля структури за адресами, кратними їхнім alignment-вимогам; компілятор додає padding, щоб доступ CPU був швидким і коректним."
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

**Вирівнювання** означає, що поля структури розміщуються за адресами, кратними їхнім alignment-вимогам.[^dou-embedded-interview] Наприклад, `uint32_t` часто хоче адресу, кратну 4. Компілятор вставляє невикористані байти padding, щоб доступ був швидким і коректним для CPU.

Це важливо в embedded: misaligned access на деяких MCU повільний або викликає fault, а register/protocol layout може вимагати точних offset-ів. Розмір можна зменшити перестановкою полів від більших до менших, але для binary protocol або hardware registers краще явно серіалізувати дані або перевіряти layout через `static_assert` і `offsetof`.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
