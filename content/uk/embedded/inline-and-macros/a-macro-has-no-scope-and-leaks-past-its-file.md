---
id: emb-macros-0035
title: "Trap: чому макрос може «зламати» нібито непов'язаний код у іншому файлі?"
description: "Макрос не має scope – після #define він замінює кожне входження ідентифікатора у всіх наступних рядках і включених файлах."
track: embedded
section: inline-and-macros
level: junior
type: pitfall
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

Макрос не має scope – після `#define` він замінює кожне входження ідентифікатора у всіх наступних рядках і включених файлах.

Класика: `#define max(a,b) ...` у header ламає `std::max`, поле `obj.max` чи локальну змінну `max` у будь-якому коді, що включив цей header (типова біда з `min`/`max` у Windows-заголовках).

Захист: для макросів – UPPER_CASE імена з префіксом проєкту; уникай імен, схожих на звичайні ідентифікатори; за потреби `#undef`.[^embeddedinterviewlab]

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
