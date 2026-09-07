---
id: emb-macros-0033
title: "Як зробити compile-time перевірку без `static_assert` (старий C)?"
description: "Трюк із від'ємним розміром масиву: якщо умова хибна, оголошується масив розміру -1 -> compile error ще до запуску."
track: embedded
section: inline-and-macros
level: junior
type: mechanism
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

## Question code

```c
#define STATIC_ASSERT(c, name) \
  typedef char name[(c) ? 1 : -1]
```

## Short answer

**Трюк із від'ємним розміром масиву**: якщо умова хибна, оголошується масив розміру `-1` -> <span class="warn">compile error</span> ще до запуску.

Це класичний спосіб перевіряти layout: `STATIC_ASSERT(sizeof(Frame) == 8, frame_size)`.

Правило: у C11/C++11 використовуй вбудований `_Static_assert`/`static_assert` з нормальним повідомленням; macro-трюк – лише для старих toolchain.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
