---
id: emb-patterns-0006
title: "Чому в state machine обов'язково обробляти default/невалідний стан?"
description: "Невалідний стан або неочікувана подія мають оброблятися явно, а не тихо ігноруватися."
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

**Невалідний стан або неочікувана подія мають оброблятися явно, а не тихо ігноруватися.**

Memory corruption, баг чи зовнішній вхід можуть дати стан поза `enum`; без `default` handler це призведе до невизначеної поведінки або out-of-bounds у таблиці.

Правило: завжди май default-гілку/handler і bounds-перевірку індексу стану.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
