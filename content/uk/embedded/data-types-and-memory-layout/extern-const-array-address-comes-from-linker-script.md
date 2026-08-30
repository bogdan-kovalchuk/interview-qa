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
