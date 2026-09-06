---
id: emb-patterns-0015
title: "Trap: чому в бітових зсувах треба unsigned literal, а не `1`?"
description: "1 << 31 – undefined behavior: літерал 1 має тип signed int, і зсув у знаковий розряд переповнює його."
track: embedded
section: common-code-patterns
level: junior
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
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання і відповіді; відповідь незалежно не перевірена."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
---

## Short answer

`1 << 31` – undefined behavior: літерал `1` має тип signed `int`, і зсув у знаковий розряд переповнює його.

`1U << 31` визначено лише якщо `unsigned int` має ширину більше 31 біта. На 16-bit `unsigned int` це теж некоректно, бо shift count завеликий.

Захист: для 32-bit масок пиши `UINT32_C(1) << n`; для register-width масок підбирай literal потрібної ширини.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
