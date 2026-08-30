---
id: emb-dtypes-0004
title: "Що таке секція `.bss` і чим вона відрізняється від `.data`?"
description: ".bss тримає неініціалізовані/нульові глобальні без байтів у Flash, .data - ініціалізовані з копією значень."
track: embedded
section: data-types-and-memory-layout
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
    applicability: "Джерело питання і відповіді; відповідь не перевірена незалежно."
---

## Short answer

**.bss** (Block Started by Symbol) - секція для глобальних і static змінних без ініціалізатора або з `= 0`.

На відміну від `.data`, `.bss` **не зберігає байти у Flash** - тільки розмір. Startup code заповнює її нулями перед `main()`. Це економить Flash: замість зберігання нулів - просто обнуляємо область у RAM.

`.data` потребує ініціалізаційних значень у Flash + копіювання у RAM.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
