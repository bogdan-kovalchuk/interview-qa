---
id: emb-macros-0014
title: "Trap: чому `STR(__LINE__)` дає `\"__LINE__\"`, а не номер рядка?"
description: "Оператор # стрінгіфікує текст аргументу до його розгортання, тому потрібен проміжний рівень – two-level stringification idiom."
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

<span class="warn">`#` стрінгіфікує текст аргументу до його розгортання</span>, тому вбудований макрос `__LINE__` не встигає перетворитися на число.

Захист: додай проміжний рівень – спершу розгорни, потім стрінгіфікуй:

```c
#define STR(x) #x
#define XSTR(x) STR(x)
// XSTR(__LINE__) -> "42"
```

Це класичний two-level stringification idiom.[^embeddedinterviewlab]

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
