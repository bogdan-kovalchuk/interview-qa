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
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 2
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
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу c-in-embedded; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

**Bit-field** – поле struct із заданою кількістю бітів, наприклад `unsigned mode:3`. Його порядок бітів, allocation unit, padding і навіть signedness деяких форм залежать від implementation. <span class="warn">Для MMIO і wire protocols це небезпечно</span>: краще використовувати masks/shifts над `uint32_t`.[^dou-embedded-interview]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
