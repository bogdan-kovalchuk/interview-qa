---
id: emb-volconst-0061
title: "Як `const` допомагає компілятору ловити помилки?"
description: "const перетворює випадковий запис у compile-time error, якщо доступ іде через const-qualified type."
track: embedded
section: volatile-and-const
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

**`const` перетворює випадковий запис у compile-time error**, якщо доступ іде через const-qualified type.

Наприклад, parser з параметром `const uint8_t *frame` не зможе випадково змінити input packet. Це особливо важливо, коли input може бути у Flash, у shared communication buffer або у memory region з MPU read-only permissions.

Правило: const-correctness дешевша за debug випадкових side effects у driver або protocol stack.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
