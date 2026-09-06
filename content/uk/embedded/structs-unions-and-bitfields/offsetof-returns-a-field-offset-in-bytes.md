---
id: emb-structs-0007
title: "Що таке `offsetof` і навіщо він потрібен?"
description: "offsetof(T, field) повертає offset поля всередині структури в байтах."
track: embedded
section: structs-unions-and-bitfields
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

**`offsetof(T, field)`** повертає offset поля всередині структури в байтах.

Це стандартний спосіб перевірити layout без ручних припущень. У embedded його використовують для static assertions register maps, protocol headers, Flash records і DMA descriptors.

Правило: якщо hardware manual каже, що `STATUS` має бути на offset `0x10`, перевір це через `_Static_assert(offsetof(Type, STATUS) == 0x10, "...")`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
