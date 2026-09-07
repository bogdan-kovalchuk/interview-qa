---
id: emb-macros-0005
title: "Trap: що не так із викликом `MAX(++x, y)`?"
description: "Double evaluation: параметр a зустрічається у тілі двічі, тому ++x виконається двічі, якщо умова істинна."
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
#define MAX(a, b) ((a) > (b) ? (a) : (b))
```

<span class="warn">Double evaluation</span>: параметр `a` зустрічається у тілі двічі, тому `++x` виконається двічі, якщо умова істинна.

Розгортання: `((++x) > (y) ? (++x) : (y))` – `x` інкрементується вдруге у true-гілці. Будь-який аргумент із side effect (`++`, `--`, виклик функції, читання volatile регістра) дає неочікуваний результат.

Захист: використовуй `static inline` функцію – вона обчислює аргумент рівно один раз.[^embeddedinterviewlab]

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
