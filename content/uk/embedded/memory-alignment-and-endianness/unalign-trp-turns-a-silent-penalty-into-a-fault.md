---
id: emb-align-0008
title: "Як поводиться misaligned access на Cortex-M3/M4 і що таке `UNALIGN_TRP`?"
description: "M3/M4/M7 часто дозволяють звичайні unaligned halfword/word доступи, але зі штрафом у bus cycles; деякі інструкції на кшталт LDM/STM (load/store multiple), LDRD/STRD (load/store doubleword) все одно вимагають вирівнювання."
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

**M3/M4/M7 часто дозволяють звичайні unaligned halfword/word доступи, але зі штрафом у bus cycles**; деякі інструкції на кшталт `LDM`/`STM` (load/store multiple), `LDRD`/`STRD` (load/store doubleword) все одно вимагають вирівнювання.

Біт `UNALIGN_TRP` у регістрі `SCB->CCR` (System Control Block -> Configuration and Control Register) вмикає trap для unaligned word/halfword доступів, які інакше могли б тихо спрацювати повільніше. Це перетворює приховану проблему на явний fault.

Правило: вмикай `UNALIGN_TRP` під час розробки, щоб ловити misaligned-баги, але не покладайся на unaligned typed-pointer доступ у C – він усе одно може бути UB (undefined behavior) на рівні мови.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
