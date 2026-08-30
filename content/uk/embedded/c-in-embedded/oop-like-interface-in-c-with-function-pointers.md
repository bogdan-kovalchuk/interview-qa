---
id: emb-cemb-0031
title: "Як реалізувати OOP-подібний інтерфейс у C через struct, function pointers і opaque handles?"
description: "Практичне питання про embedded-розробку та її обмеження."
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

Публічний API оголошує opaque тип <code>typedef struct uart uart_t;</code>, а реалізація ховає поля struct у <code>.c</code>. Методи приймають <code>uart_t*</code>, а polymorphism можна зробити через table з function pointers: <code>read</code>, <code>write</code>, <code>ioctl</code>. Так driver API має інкапсуляцію без C++ ABI і без відкриття внутрішнього MMIO/стану.[^dou-embedded-interview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

