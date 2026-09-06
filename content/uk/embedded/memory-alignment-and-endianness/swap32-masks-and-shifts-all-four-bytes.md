---
id: emb-align-0018
title: "Як написати `swap32` для 32-бітного byte-swap?"
description: "Кожен байт переміщується у дзеркальну позицію, маски відсікають зайве."
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

```c
static inline uint32_t swap32(uint32_t v) {
  return ((v >> 24) & 0xFF)
       | ((v >>  8) & 0xFF00)
       | ((v <<  8) & 0xFF0000)
       | ((v << 24) & 0xFF000000);
}
```

Кожен байт переміщується у дзеркальну позицію, маски відсікають зайве.

Правило: GCC/Clang згортають це в одну інструкцію `REV` на ARM – швидко й портативно.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
