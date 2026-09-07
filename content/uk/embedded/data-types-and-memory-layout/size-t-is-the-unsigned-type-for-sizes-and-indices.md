---
id: emb-dtypes-0087
title: "Що таке `size_t` і чому він кращий за `int` для розмірів і індексів?"
description: "size_t беззнаковий і завжди достатнього розміру для об'єкта на платформі, на відміну від int."
track: embedded
section: data-types-and-memory-layout
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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
    applicability: "Джерело питання і відповіді; відповідь не перевірена незалежно."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу data-types-and-memory-layout; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

**size_t** - беззнаковий тип, достатній для представлення розміру будь-якого об'єкта у пам'яті. На 32-bit = `uint32_t`, на 64-bit = `uint64_t`. Визначений у `<stddef.h>`.

Переваги:
- Не може бути від'ємним (логічно для розміру);
- Правильний розмір для платформи;
- Уникає sign-comparison warnings.

`sizeof`, `strlen`, `malloc` - використовують і повертають `size_t`. `int` може бути 16-bit (недостатньо для великих об'єктів).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
