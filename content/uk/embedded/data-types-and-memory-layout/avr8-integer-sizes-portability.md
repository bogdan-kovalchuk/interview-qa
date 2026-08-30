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

На типовому AVR-GCC для AVR8: <code>char</code> 8 біт, <code>int</code> 16 біт, <code>long</code> 32 біти, pointer часто 16 біт для data address space. На 32-bit MCU <code>int</code> зазвичай 32 біти, тому overflow, printf format і struct layout можуть змінитися. <span class="warn">У portable firmware краще використовувати <code>stdint.h</code>: <code>uint8_t</code>, <code>uint16_t</code>, <code>uint32_t</code></span>.[^dou-embedded-interview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
