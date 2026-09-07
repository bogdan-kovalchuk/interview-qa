---
id: emb-dtypes-0102
title: "Які розміри integer-типів на AVR8 і чому не можна переносити припущення з 32-bit MCU?"
description: "На типовому AVR8 int має 16 біт, на 32-bit MCU зазвичай 32, тому для portable firmware слід використовувати fixed-width типи."
track: embedded
section: data-types-and-memory-layout
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
    applicability: "Авторитетне джерело рівня секції для понять розділу data-types-and-memory-layout; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

На типовому AVR-GCC для AVR8: `char` 8 біт, `int` 16 біт, `long` 32 біти, pointer часто 16 біт для data address space. На 32-bit MCU `int` зазвичай 32 біти, тому overflow, printf format і struct layout можуть змінитися. <span class="warn">У portable firmware краще використовувати `stdint.h`: `uint8_t`, `uint16_t`, `uint32_t`</span>.[^dou-embedded-interview]

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
