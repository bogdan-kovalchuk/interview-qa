---
id: emb-dtypes-0072
title: "Яка різниця між `.rodata` у Flash і `.data` у RAM з точки зору ресурсів?"
description: ".rodata читається прямо з Flash без витрат RAM, а .data подвійно платить і Flash, і RAM."
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

**.rodata** - тільки Flash: CPU читає константи прямо звідти (з wait states), RAM не витрачається.

**.data** - і Flash і RAM: значення у Flash (LMA) + копія у RAM (VMA). Тобто <span class="warn">подвійна витрата</span>: Flash для ініціалізаційних значень + RAM для runtime.

Практика на MCU з 20KB RAM: велика lookup table -> `const` -> `.rodata` -> тільки Flash. Економія RAM критична.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
