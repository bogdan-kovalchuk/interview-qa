---
id: emb-volconst-0029
title: "Що означає MISRA-підхід до `const` для pointer parameters?"
description: "Pointer parameter має вказувати на const-qualified type, якщо функція не змінює pointed-to object."
track: embedded
section: volatile-and-const
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

**Pointer parameter має вказувати на const-qualified type, якщо функція не змінює pointed-to object.**

Ідея не в стилі, а в контракті: static analyzer може відрізнити read-only input buffer від output buffer. Це запобігає випадковим записам у Flash tables, string literals або DMA descriptors, які мають бути immutable для цієї функції.

Практичне правило: `void parse(const uint8_t *frame, size_t len)` краще за `void parse(uint8_t *frame, size_t len)`, якщо parser не модифікує frame.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
