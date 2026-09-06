---
id: emb-align-0014
title: "Чому network byte order – це big-endian і як з ним працювати?"
description: "Мережеві протоколи стандартизовані на big-endian (network byte order)."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: concept
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

**Мережеві протоколи стандартизовані на big-endian (network byte order).**

POSIX (Portable Operating System Interface) дає конвертери host vs network: 

```c
uint32_t net = htonl(host); // to BE
uint32_t h   = ntohl(net);  // back to host
```

Для 16-бітних – `htons`/`ntohs`.

Правило: завжди конвертуй багатобайтові поля при відправці/прийомі по мережі.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
