---
id: emb-cemb-0032
title: "Для чого потрібні static, const, volatile і restrict у C, і які комбінації мають сенс?"
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
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу c-in-embedded; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

`static` керує linkage або storage duration, `const` забороняє зміну через цей lvalue, `volatile` змушує реально виконувати access, а `restrict` обіцяє відсутність aliasing для оптимізації. Для MMIO типовий pointer: `volatile uint32_t *`; для read-only register може бути `volatile const uint32_t *`. `static const` часто кладе таблиці у flash/rodata, а `restrict` доречний у DSP/buffer code, якщо контракт справді виконується.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

