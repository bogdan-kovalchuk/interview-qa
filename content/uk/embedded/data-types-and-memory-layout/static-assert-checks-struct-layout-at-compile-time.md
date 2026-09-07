---
id: emb-dtypes-0099
title: "Навіщо потрібен `static_assert` при роботі зі структурами у embedded?"
description: "static_assert перевіряє sizeof і offsetof структур при компіляції, гарантуючи відповідність протоколу."
track: embedded
section: data-types-and-memory-layout
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
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Джерело питання і відповіді; відповідь не перевірена незалежно."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу data-types-and-memory-layout; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

`static_assert` (C11 `_Static_assert`, C++ `static_assert`) перевіряє умову **при компіляції** -> помилка якщо false.

Для embedded: `static_assert(sizeof(CanFrame) == 13, "Wrong CAN frame size");`
`static_assert(offsetof(UartPacket, crc) == 6, "CRC offset mismatch");`

Гарантує що struct layout відповідає протоколу / hardware register map незалежно від зміни компілятора, ABI, прапорців.

Найкраща практика: кожна структура протоколу повинна мати `static_assert` на `sizeof` і `offsetof`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
