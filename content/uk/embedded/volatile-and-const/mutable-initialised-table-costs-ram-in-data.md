---
id: emb-volconst-0026
title: "В яку секцію зазвичай потрапить не-`const` таблиця?"
description: "У .data: initialized mutable global/static data."
track: embedded
section: volatile-and-const
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
uint16_t sine_lut[256] = { 0, 402, 804 };
```

## Short answer

У `.data`: initialized mutable global/static data.

Початкові значення лежать у Flash як load image, але перед `main()` startup code копіює їх у RAM, бо масив можна змінювати. Це коштує і Flash, і RAM, і часу boot copy.

Захист: якщо table не змінюється runtime, зроби її `const`, щоб вона стала кандидатом на `.rodata` у Flash.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
