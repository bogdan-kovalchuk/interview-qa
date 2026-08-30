---
id: emb-dtypes-0048
title: "Для яких секцій потрібна Flash-to-RAM копія при завантаженні, а для яких - ні?"
description: ".data копіюється з Flash у RAM при старті, а .rodata і .bss копії не потребують."
track: embedded
section: data-types-and-memory-layout
level: middle
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

**Потребує копіювання:** `.data` - ініціалізовані глобальні/static (значення зберігаються у Flash LMA, копіюються у RAM VMA).

**НЕ потребує:**
- `.rodata` - CPU читає прямо з Flash;
- `.bss` - обнуляється startup code (нема що копіювати);
- `.text` - виконується з Flash (XIP).

<span class="warn">Велика `.data` -> повільніший boot</span>. Оптимізація: переносити дані у `const` -> `.rodata`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
