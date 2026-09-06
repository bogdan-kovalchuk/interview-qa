---
id: emb-patterns-0024
title: "Чому регістри периферії мають бути `volatile`?"
description: "Статусний регістр змінюється апаратурою асинхронно, а не кодом."
track: embedded
section: common-code-patterns
level: junior
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

**Статусний регістр змінюється апаратурою асинхронно, а не кодом.**

Без `volatile` компілятор припускає, що пам'ять змінюється лише записами програми: він може прочитати регістр один раз, закешувати в CPU (central processing unit) регістрі й більше не перечитувати. `volatile` змушує кожне читання/запис іти у реальну пам'ять.

Правило: будь-який memory-mapped регістр – `volatile`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
