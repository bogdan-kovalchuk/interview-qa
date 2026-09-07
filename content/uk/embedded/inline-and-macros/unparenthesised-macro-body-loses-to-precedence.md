---
id: emb-macros-0004
title: "Що насправді обчислить цей код?"
description: "r == 11, а не 25. Макрос – це текстова заміна без дужок, тому SQUARE(2 + 3) розгортається у 2 + 3 2 + 3."
track: embedded
section: inline-and-macros
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

```c
#define SQUARE(x) x * x
int r = SQUARE(2 + 3);
```

`r == 11`, а <span class="warn">не 25</span>.

Макрос – це текстова заміна без дужок, тому `SQUARE(2 + 3)` розгортається у `2 + 3 * 2 + 3`. За правилами precedence спершу `3 * 2 = 6`, потім `2 + 6 + 3 = 11`.

Захист: `#define SQUARE(x) ((x) * (x))` – тоді буде `((2 + 3) * (2 + 3)) = 25`.[^embeddedinterviewlab]

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
