---
id: emb-fnptr-0012
title: "Що таке callback?"
description: "Callback – це функція, адресу якої передають іншому коду, щоб той викликав її пізніше при певній події або умові."
track: embedded
section: function-pointers-and-callbacks
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

**Callback** – це функція, адресу якої передають іншому коду, щоб той викликав її пізніше при певній події або умові.

У C callback найчастіше реалізується function pointer-ом. Наприклад, driver UART викликає callback при отриманні байта, timer – при timeout, parser – коли знайшов frame, а `qsort` – коли треба порівняти два елементи.

Правило інтерв'ю: function pointer – механізм; callback – роль або pattern використання цього механізму.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
