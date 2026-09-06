---
id: emb-structs-0027
title: "Що робить unnamed zero-width bit-field?"
description: "Zero-width unnamed bit-field змушує наступний bit-field початися з нового allocation unit."
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
struct F {
    unsigned a : 3;
    unsigned   : 0;
    unsigned b : 5;
};
```

**Zero-width unnamed bit-field** змушує наступний bit-field початися з нового allocation unit.

Це спосіб вставити boundary між групами bit-fields. Реальний розмір і alignment усе одно залежать від базового типу та ABI компілятора.

Embedded-правило: це може допомогти для internal layout, але не робить bit-field mapping portable для hardware register manual.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
