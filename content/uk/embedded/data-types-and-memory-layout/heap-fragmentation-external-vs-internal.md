---
id: emb-dtypes-0034
title: "Що таке heap fragmentation і чому це критично для embedded?"
description: "Heap fragmentation залишає вільну пам'ять розкиданою дрібними блоками, а MCU без MMU не може її дефрагментувати."
track: embedded
section: data-types-and-memory-layout
level: middle
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
    applicability: "Джерело питання і відповіді; відповідь не перевірена незалежно."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? data-types-and-memory-layout; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

Heap fragmentation виникає після множинних `malloc`/`free`: є вільні блоки, але не суцільний блок потрібного розміру -> `malloc` повертає NULL.

**Зовнішня**: багато малих вільних блоків. **Внутрішня**: виділений блок більший за запит (alignment/metadata).

У embedded (MCU без MMU) - <span class="warn">нема defragmentation</span>. Рішення: static allocation або memory pool (fixed-size blocks).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
