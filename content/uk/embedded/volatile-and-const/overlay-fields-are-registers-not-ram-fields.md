---
id: emb-volconst-0045
title: "Чому peripheral register struct fields оголошують як `volatile`?"
description: "Бо кожне поле struct overlay представляє hardware register, а не звичайне RAM-поле."
track: embedded
section: volatile-and-const
level: junior
type: concept
tags: []
status: published
updated: 2026-09-06
content_revision: 1
reconciled_with:
  en: 2
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

**Бо кожне поле struct overlay представляє hardware register, а не звичайне RAM-поле.**

Коли код пише `GPIOA->ODR` або читає `GPIOA->IDR`, це bus transaction до peripheral address. Компілятор не має права кешувати значення поля, об'єднувати записи або прибирати читання.

Правило: у CMSIS-style register overlay volatile має стояти на register fields або на типі доступу так, щоб кожен field access був volatile access.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
