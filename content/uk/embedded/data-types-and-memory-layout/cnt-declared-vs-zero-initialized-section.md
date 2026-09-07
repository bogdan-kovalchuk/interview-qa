---
id: emb-dtypes-0055
title: "Що буде у `.bss` vs `.data` для: `uint32_t cnt;` та `uint32_t cnt = 0;` (глобальні)?"
description: "uint32_t cnt; явно потрапляє у .bss, а uint32_t cnt = 0; залежить від того, чи компілятор розпізнає нульову ініціалізацію."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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
    applicability: "Авторитетне джерело рівня секції для понять розділу data-types-and-memory-layout; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

`uint32_t cnt;` -> **.bss**: не займає Flash, zeroed by startup code.

`uint32_t cnt = 0;` -> залежить від компілятора: може бути `.data` (явний ініціалізатор, значення 0 у Flash) або `.bss` (компілятор розпізнає zero-init).

Стандарт C гарантує обидва = 0, але Flash/RAM usage може відрізнятись. Перевіряй: `arm-none-eabi-nm --print-size firmware.elf`. Пиши `uint32_t cnt;` для явного `.bss`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
