---
id: emb-dtypes-0062
title: "Яка секція пам'яті є найдорожчою з точки зору boot time і чому?"
description: ".data найдорожча, бо startup code мусить скопіювати весь її вміст з Flash у RAM перед main()."
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
---

## Short answer

**.data** - найдорожча. Startup code мусить скопіювати весь `.data` з Flash (повільна, wait states) у RAM (швидка). Велика `.data` -> повільніший boot.

`.bss` - дешевша: тільки заповнення нулями у RAM.

`.rodata` і `.text` - нічого копіювати.

Оптимізація: замінюй ініціалізовані глобальні на `const` -> `.rodata` у Flash, без RAM копіювання.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
