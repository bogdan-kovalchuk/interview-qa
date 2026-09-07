---
id: emb-macros-0011
title: "Trap: чому цей макрос ламає `if/else`?"
description: "Розгортається у if (err) a(); b(); else ok(); – else більше не має парного if -> compile error, або (з одним statement) b() викликається завжди."
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
#define RST() a(); b()

if (err)
    RST();
else
    ok();
```

<span class="warn">Розгортається у `if (err) a(); b(); else ok();`</span> – `else` більше не має парного `if` -> compile error, або (з одним statement) `b()` викликається завжди.

Тільки `a()` належить `if`; `b();` виконується безумовно, а `else` зависає.

Захист: `#define RST() do { a(); b(); } while(0)` – тоді весь блок прив'язаний до `if`.[^embeddedinterviewlab]

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
