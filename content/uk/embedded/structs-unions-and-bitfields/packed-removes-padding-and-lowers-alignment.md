---
id: emb-structs-0011
title: "Що таке `packed` структура?"
description: "Packed structure просить компілятор не вставляти звичайний padding між полями або зменшити alignment структури."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: concept
tags: []
status: published
updated: 2026-09-06
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

## Short answer

**Packed structure** просить компілятор не вставляти звичайний padding між полями або зменшити alignment структури.

Це корисно для wire-format headers, on-flash records або точно заданого binary layout. Але packed може створити unaligned accesses: поле `uint32_t` може опинитися на offset 1, що на деяких MCU повільно або навіть fault.

Правило: packed застосовують на межі формату, а не як універсальний спосіб економити RAM. Для internal data краще переставити поля.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
