---
id: emb-align-0020
title: "Trap: чому НЕ можна `memcpy`-їти сиру структуру між різними MCU?"
description: "Різні компілятори/архітектури дають різний padding і byte order для того самого коду."
track: embedded
section: memory-alignment-and-endianness
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

Різні компілятори/архітектури дають різний padding і byte order для того самого коду.

Одна сторона може мати інші зсуви полів і протилежну endianness, тож той самий `struct` у пам'яті виглядає по-різному. Сирий `memcpy` передасть несумісний layout.

Захист: завжди визначай явний wire-формат і серіалізуй поле за полем з явним byte order.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
