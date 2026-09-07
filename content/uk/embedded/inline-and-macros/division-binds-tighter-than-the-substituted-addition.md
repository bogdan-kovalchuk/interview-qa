---
id: emb-macros-0036
title: "Що виведе цей код?"
description: "Виведе 3, а не 2. Розгортання: 2 + 2 / 2."
track: embedded
section: inline-and-macros
level: junior
type: mechanism
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

## Question code

```c
#define HALF(x) x / 2
printf("%d", HALF(2 + 2));
```

## Short answer

Виведе `3`, а <span class="warn">не 2</span>.

Розгортання: `2 + 2 / 2`. Через precedence спершу `2 / 2 = 1`, потім `2 + 1 = 3`. Очікувалося `(2 + 2) / 2 = 2`, але відсутні дужки змінюють порядок операцій.

Захист: `#define HALF(x) ((x) / 2)` -> розгортається у `((2 + 2) / 2) = 2`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
