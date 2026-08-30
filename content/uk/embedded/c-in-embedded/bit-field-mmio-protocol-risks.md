---
id: emb-cemb-0036
title: "Що таке bit-field у C і чому його небезпечно використовувати для MMIO-регістрів або протоколів?"
description: "Bit-field має implementation-defined layout, тому не є надійним переносимим представленням MMIO чи wire protocol."
track: embedded
section: c-in-embedded
level: middle
type: pitfall
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

<span class="key">Bit-field</span> – поле struct із заданою кількістю бітів, наприклад <code>unsigned mode:3</code>. Його порядок бітів, allocation unit, padding і навіть signedness деяких форм залежать від implementation. <span class="warn">Для MMIO і wire protocols це небезпечно</span>: краще використовувати masks/shifts над <code>uint32_t</code>.[^dou-embedded-interview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
