---
id: emb-align-0010
title: "Який рекомендований патерн роботи з packed wire-форматом?"
description: "Тримай дві структури: packed для дроту і звичайну вирівняну для обробки."
track: embedded
section: memory-alignment-and-endianness
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

**Тримай дві структури: packed для дроту і звичайну вирівняну для обробки.** 

```c
typedef struct {
  uint32_t ts; uint16_t val; uint8_t id;
} __attribute__((packed)) wire_t;

typedef struct {
  uint32_t ts; uint16_t val; uint8_t id;
} reading_t; // aligned
```

Копіюй з packed у aligned (поле за полем) і працюй уже з вирівняною копією.

Правило: не звертайся напряму до полів packed-структури в гарячому коді.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
