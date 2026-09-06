---
id: emb-fnptr-0034
title: "Як безпечніше написати `qsort` comparator для `int`?"
description: "Так: return (x > y) - (x < y); Повний фрагмент: const int x = (const int )a; const int y = (const int )b;."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: mechanism
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

Так:

`return (x > y) - (x < y);`

Повний фрагмент: `const int x = *(const int *)a; const int y = *(const int *)b;`. Такий comparator повертає `1`, `0` або `-1` без signed overflow.

Правило: comparator має бути strict і стабільний за логікою ordering; не покладайся на overflow arithmetic.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
