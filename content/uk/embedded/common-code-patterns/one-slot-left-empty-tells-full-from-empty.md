---
id: emb-patterns-0010
title: "Як у ring buffer визначають full і empty без лічильника?"
description: "Empty: head == tail. Full: (head + 1) & MASK == tail (один слот завжди лишається порожнім)."
track: embedded
section: common-code-patterns
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

**Empty: `head == tail`. Full: `(head + 1) & MASK == tail`** (один слот завжди лишається порожнім).

Це уникає спільної змінної `count`, яка створює read-modify-write гонку між ISR (interrupt service routine) і main.

Правило: «жертвуємо» одним слотом, але отримуємо справжню lock-free безпеку без критичних секцій.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
