---
id: emb-structs-0015
title: "Яким буде типовий розмір union?"
description: "Типово sizeof(union U) == 4, якщо uint32_t має розмір 4 і найбільший alignment також не збільшує розмір понад 4."
track: embedded
section: structs-unions-and-bitfields
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
union U {
    uint8_t  b;
    uint16_t h;
    uint32_t w;
};
```

## Short answer

Типово `sizeof(union U) == 4`, якщо `uint32_t` має розмір 4 і найбільший alignment також не збільшує розмір понад 4.

Усі поля починаються на offset 0. `b` використовує перший byte storage, `h` перші 2 bytes, `w` усі 4 bytes. Реальне тлумачення bytes залежить від endianness і правил доступу.

Правило: union size визначається найбільшим member-ом, а не сумою member-ів.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
