---
id: emb-align-0015
title: "Що повертає `htonl()` на big-endian хості?"
description: "Те саме значення без змін – це no-op."
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

**Те саме значення без змін – це no-op.**

На big-endian host = network order, тому конвертувати нема чого. На little-endian host `htonl`/`ntohl` міняють байти місцями. Найважливіше: код не мусить знати, який це випадок – пиши `htonl` завжди, і він зробить правильне на будь-якій платформі.

Правило: ніколи не роби byte swap «вручну за умовою платформи», якщо є `hton*`/`ntoh*`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
