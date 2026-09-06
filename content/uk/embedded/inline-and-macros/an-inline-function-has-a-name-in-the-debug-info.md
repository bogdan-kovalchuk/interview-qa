---
id: emb-macros-0009
title: "Чому `static inline` функцію легше дебажити, ніж макрос?"
description: "Inline-функція має символьне ім'я і реальний код у debug info, тому в неї можна поставити breakpoint, зробити step-into і побачити її у backtrace."
track: embedded
section: inline-and-macros
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

**Inline-функція має символьне ім'я і реальний код у debug info**, тому в неї можна поставити breakpoint, зробити step-into і побачити її у backtrace.

Макрос розгортається ще до компіляції, тож дебагер бачить лише inline-підставлений код у місці виклику. Повідомлення про помилку також вказує на розгорнутий код, а не на рядок `#define`.

Правило: складну логіку, яку доведеться дебажити, не ховай у макрос.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
