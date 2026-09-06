---
id: emb-volconst-0054
title: "Який тип краще для ISR flag: `volatile bool` чи `bool`?"
description: "Для flag, який пише ISR і читає main loop, потрібен volatile: наприклад static volatile bool button_pressed;."
track: embedded
section: volatile-and-const
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

Для flag, який пише ISR і читає main loop, потрібен `volatile`: наприклад `static volatile bool button_pressed;`.

Без `volatile` main loop може не перечитувати flag з пам'яті. Але сам тип також має бути таким, що читається і пишеться атомарно на цільовій платформі. Для простих Cortex-M byte/word flags це зазвичай нормально, але залежить від доступу й вирівнювання.

Правило: simple ISR flag = volatile + простий атомарний тип; складний стан = critical section або queue/event mechanism.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
