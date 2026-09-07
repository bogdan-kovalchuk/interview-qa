---
id: emb-macros-0029
title: "Trap: що не так із `#define SIZE 256;`?"
description: "Зайва крапка з комою стає частиною тексту заміни."
track: embedded
section: inline-and-macros
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
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

<span class="warn">Зайва крапка з комою стає частиною тексту заміни.</span>

`int a[SIZE];` розгорнеться у `int a[256;];` -> синтаксична помилка. А в `x = SIZE + 1;` вийде `x = 256; + 1;`, що компілюється, але робить не те.

Захист: object-like макрос ніколи не закінчуй крапкою з комою: `#define SIZE 256`.[^embeddedinterviewlab]

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
