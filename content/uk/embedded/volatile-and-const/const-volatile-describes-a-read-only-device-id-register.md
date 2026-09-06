---
id: emb-volconst-0047
title: "Що означає `const volatile` для memory-mapped device ID register?"
description: "Firmware не має права записувати register, але повинна читати його як volatile hardware value."
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

**Firmware не має права записувати register, але повинна читати його як volatile hardware value.**

Device ID може бути read-only з точки зору CPU, але фізично на шині це hardware register, а не звичайна константа в Flash. Навіть якщо значення практично не змінюється, тип `const volatile` описує правильний ownership: hardware owns, firmware observes.

Правило: read-only hardware register не слід описувати як просто `const`, бо компілятор може поводитися з ним як зі звичайними read-only data.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
