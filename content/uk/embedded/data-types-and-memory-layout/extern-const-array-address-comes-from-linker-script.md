---
id: emb-dtypes-0093
title: "Де зберігається `extern const uint8_t image_data[]` визначена у linker script?"
description: "Масив лежить у Flash, а його адресу лінкер script присвоює через окремий символ секції."
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

У Flash, у секції `.rodata` або спеціальній секції визначеній у linker script.

`extern const` без ініціалізатора у C коді - тільки declaration. Linker script визначає symbol `image_data` з адресою у Flash:
`image_data = LOADADDR(.flash_resources);`

Типове використання: бінарні ресурси (зображення, сертифікати, таблиці), що вбудовані у firmware через `KEEP(*(.flash_data))` або `objcopy -I binary`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
