---
id: emb-macros-0003
title: "Як виглядає коректний function-like макрос `MAX` і чому всі дужки обов'язкові?"
description: "Дужки навколо кожного параметра і навколо всього виразу захищають від проблем з operator precedence після підстановки."
track: embedded
section: inline-and-macros
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

```c
#define MAX(a, b) ((a) > (b) ? (a) : (b))
```

Дужки навколо кожного параметра і навколо всього виразу захищають від проблем з operator precedence після підстановки.

Без них вираз на кшталт `MAX(x & 1, y)` або `MAX(a, b) * 2` може розгорнутися з неправильним порядком операцій.

Правило: function-like макрос завжди пиши за схемою `((param)...)` – параметри в дужках, результат у дужках.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
