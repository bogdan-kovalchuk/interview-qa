---
id: emb-cppfound-0089
title: "Яка різниця між `memcpy` і pointer cast для копіювання між типами?"
description: "Why memcpy avoids aliasing and alignment problems during type punning."
track: embedded
section: c-in-embedded
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу c-in-embedded; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

**Pointer cast + dereference**: `uint32_t x = *(uint32_t*)bytes;` – потенційний UB (strict aliasing, misalignment). Компілятор може оптимізувати "неправильно".

**memcpy**: `uint32_t x; memcpy(&x, bytes, 4);` – завжди коректно: не порушує aliasing, компілятор оптимізує до одного LDR якщо вирівняно.

Правило: для type punning використовуй `memcpy` (або `union` у C). Pointer cast безпечний лише для `char*`/`unsigned char*`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
