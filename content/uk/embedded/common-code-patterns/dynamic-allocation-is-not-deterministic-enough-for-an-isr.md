---
id: emb-patterns-0030
title: "Trap: чому для ring buffer не можна використовувати `malloc`?"
description: "Динамічна пам'ять недетермінована і фрагментується – неприйнятно для real-time/ISR-контексту."
track: embedded
section: common-code-patterns
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
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

<span class="warn">Динамічна пам'ять недетермінована і фрагментується</span> – неприйнятно для real-time/ISR-контексту.

Ring buffer часто живе весь час роботи системи й використовується з переривань, де `malloc` заборонений (non-reentrant, може блокувати). Розмір відомий заздалегідь.

Захист: завжди static allocation фіксованого степеня-двійки розміру.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
