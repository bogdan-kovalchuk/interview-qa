---
id: emb-structs-0030
title: "Що буде з незаданими полями?"
description: "parity і stop_bits будуть zero-initialized."
track: embedded
section: structs-unions-and-bitfields
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
struct Cfg {
    uint32_t baud;
    uint8_t parity;
    uint8_t stop_bits;
};

struct Cfg c = { .baud = 115200 };
```

**`parity` і `stop_bits` будуть zero-initialized.**

Aggregate initialization у C занулює поля, які не були явно ініціалізовані. Це зручно для config structs, де `0` є valid default.

Правило: designated initializers зменшують ризик переплутати positional fields, але default zero має бути семантично коректним. Якщо `0` небезпечний, потрібен factory/default function.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
