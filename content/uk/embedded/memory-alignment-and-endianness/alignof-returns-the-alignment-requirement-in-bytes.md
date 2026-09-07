---
id: emb-align-0025
title: "Що повертає `_Alignof(T)` (C11) / `alignof(T)`?"
description: "Вимогу вирівнювання типу в байтах."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: concept
tags: []
status: published
updated: 2026-09-06
content_revision: 1
reconciled_with:
  en: 3
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

**Вимогу вирівнювання типу в байтах.**

`_Alignof(uint32_t)` -> 4, `_Alignof(double)` -> зазвичай 8. Це compile-time значення, корисне для перевірок layout і власних аллокаторів.

Правило: у C11 – `_Alignof` (макрос `alignof` у `<stdalign.h>`); у C++ – `alignof` вбудований.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
