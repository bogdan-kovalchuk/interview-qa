---
id: emb-align-0038
title: "Як перевірити layout структури на етапі компіляції?"
description: "Через _Static_assert + sizeof/offsetof – будь-яка зміна padding чи порядку полів зламає збірку, а не runtime."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
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

## Question code

```c
_Static_assert(sizeof(wire_t) == 7, "layout");
_Static_assert(offsetof(wire_t, id) == 6, "offset");
```

## Short answer

**Через `_Static_assert` + `sizeof`/`offsetof`** – будь-яка зміна padding чи порядку полів зламає збірку, а не runtime.

Це критично для packed wire-форматів і register map, де точний layout – частина контракту.

Правило: фіксуй очікувані `sizeof` і `offsetof` асертами поруч із визначенням структури.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
