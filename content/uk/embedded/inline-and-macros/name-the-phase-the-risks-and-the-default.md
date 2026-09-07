---
id: emb-macros-0047
title: "Що має сказати кандидат, коли його просять обрати між макросом і `inline`?"
description: "Розрізнити фазу, перелічити ризики макроса і дефолтити в static inline."
track: embedded
section: inline-and-macros
level: junior
type: concept
tags: []
status: published
updated: 2026-09-06
content_revision: 1
reconciled_with:
  en: 3
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

**Розрізнити фазу, перелічити ризики макроса і дефолтити в `static inline`.**

Сильна відповідь: препроцесинг ≠ компіляція; макрос – текст без типів/scope з ризиком double evaluation і precedence-багів; `static inline` дає ту саму швидкість плюс type safety, однократне обчислення і дебаг. Макроси лишаю для register defs, conditional compilation, `#`/`##`, X-macros, `STATIC_ASSERT`, і згадую MISRA C (Motor Industry Software Reliability Association C) 4.9/20.7.

Правило: не зупиняйся на синтаксисі – поясни чому і коли.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
