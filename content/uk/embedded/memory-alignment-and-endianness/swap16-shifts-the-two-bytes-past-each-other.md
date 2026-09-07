---
id: emb-align-0017
title: "Як написати `swap16` для зміни порядку байтів?"
description: "Старший байт зсувається вниз, молодший – вгору, і вони об'єднуються через |."
track: embedded
section: memory-alignment-and-endianness
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
static inline uint16_t swap16(uint16_t v) {
  return (v << 8) | (v >> 8);
}
```

## Short answer

**Старший байт зсувається вниз, молодший – вгору, і вони об'єднуються через `|`.**

Для `0xAABB` -> `0xBBAA`. GCC/Clang розпізнають цей патерн і генерують одну інструкцію `REV16` на ARM.

Правило: пиши byte-swap читабельним C – inline asm зазвичай не потрібен.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
