---
id: emb-macros-0007
title: "Що таке `inline` функція і чим вона краща за function-like макрос?"
description: "inline – це справжня функція, яку компілятор може розгорнути у місці виклику, прибравши overhead виклику."
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

**inline** – це справжня функція, яку компілятор може розгорнути у місці виклику, прибравши overhead виклику.

На відміну від макроса, вона зберігає type checking, scope, обчислює аргументи рівно один раз і доступна дебагеру (breakpoints, step-into). При цьому компілятор сам вирішує – inline-ити чи зробити звичайний call.

Правило: усе, що схоже на функцію, роби `inline`/`static inline`, а не function-like макросом.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
