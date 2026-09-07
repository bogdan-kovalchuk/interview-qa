---
id: emb-structs-0033
title: "Як правильно виділити пам'ять для flexible array member?"
description: "Потрібно виділити sizeof(struct Packet) + len байтів."
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
struct Packet {
    uint16_t len;
    uint8_t data[];
};
```

## Short answer

Потрібно виділити `sizeof(struct Packet) + len` байтів.

Наприклад: `struct Packet *p = malloc(sizeof *p + len);`. Потім `p->len = len`, а payload лежить у `p->data[0..len-1]`. `sizeof *p` не включає гнучкий масив.

Embedded-правило: у bare-metal без heap такий layout часто використовують у statically allocated byte buffer з placement/offset discipline.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
