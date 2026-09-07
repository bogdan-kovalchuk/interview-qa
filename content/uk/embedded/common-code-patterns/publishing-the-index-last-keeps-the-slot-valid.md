---
id: emb-patterns-0035
title: "Чому ISR пише дані у слот ДО оновлення `head` (порядок операцій)?"
description: "Щоб consumer ніколи не побачив просунутий head, який вказує на ще не записаний байт."
track: embedded
section: common-code-patterns
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
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

**Щоб consumer ніколи не побачив просунутий `head`, який вказує на ще не записаний байт.**

Якби спершу інкрементувати `head`, а потім писати дані, переривання/перепланування між цими кроками дало б consumer'у читання сміття. Оновлення індексу – завжди остання дія producer'а. ISR тут означає interrupt service routine.

Правило: producer: дані -> `head`; consumer: дані -> `tail` – індекс публікує запис лише після того, як дані готові.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
