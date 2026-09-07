---
id: emb-structs-0003
title: "Яким буде типовий розмір на 32-bit ABI?"
description: "Типово sizeof(struct S) == 12."
track: embedded
section: structs-unions-and-bitfields
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
struct S {
    uint8_t a;
    uint32_t b;
    uint8_t c;
};
```

## Short answer

Типово `sizeof(struct S) == 12`.

Layout: `a` займає offset 0, потім 3 байти padding, `b` на offset 4, `c` на offset 8, потім 3 байти tail padding. Tail padding потрібен, щоб наступний елемент у масиві `struct S arr[]` знову мав `b` на 4-byte aligned offset.

Правило: порядок полів впливає на RAM/Flash footprint. Для масивів структур padding множиться на кількість елементів.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
