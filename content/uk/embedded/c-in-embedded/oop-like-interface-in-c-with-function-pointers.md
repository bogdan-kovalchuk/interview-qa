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

Публічний API оголошує opaque тип `typedef struct uart uart_t;`, а реалізація ховає поля struct у `.c`. Методи приймають `uart_t*`, а polymorphism можна зробити через table з function pointers: `read`, `write`, `ioctl`. Так driver API має інкапсуляцію без C++ ABI і без відкриття внутрішнього MMIO/стану.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

