---
id: emb-dtypes-0074
title: "Що таке ABI і як він впливає на розміри типів?"
description: "ABI фіксує розміри типів, calling convention і вирівнювання structs для сумісності скомпільованих модулів."
track: embedded
section: data-types-and-memory-layout
level: middle
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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
    applicability: "Джерело питання і відповіді; відповідь не перевірена незалежно."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу data-types-and-memory-layout; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

**ABI** (Application Binary Interface) - правила взаємодії між скомпільованими модулями: розміри типів, calling convention, struct alignment, register usage.

ARM AAPCS (Cortex-M):
- `int` = 32 біти
- `long` = 32 біти (не 64!)
- `long long` = 64 біти
- `float` = 32 біти
- `double` = 64 біти
- `pointer` = 32 біти

ABI - причина чому `sizeof(int)` на Cortex-M = 4. Зміна ABI (cross-compile) ламає бінарну сумісність.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
