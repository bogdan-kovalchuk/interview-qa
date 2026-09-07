---
id: emb-macros-0025
title: "Коли обирати `static inline`, а коли function-like макрос?"
description: "static inline – для всього, що схоже на функцію: дрібні хелпери, type-safe bit-маніпуляції, обчислення з аргументами (рівно одне обчислення кожного)."
track: embedded
section: inline-and-macros
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

**static inline** – для всього, що схоже на функцію: дрібні хелпери, type-safe bit-маніпуляції, обчислення з аргументами (рівно одне обчислення кожного).

Макрос – лише для того, що функцією бути не може: робота з токенами/іменами (`#`, `##`), conditional compilation, register address defs, X-macros, `STATIC_ASSERT`.

Правило: за замовчуванням – `static inline`; макрос – це виняток із обґрунтуванням.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
