---
id: emb-volconst-0048
title: "Trap: чому \"працює в debug, ламається в release\" часто натякає на missing `volatile`?"
description: "Бо debug build зазвичай має -O0, а release build вмикає оптимізації."
track: embedded
section: volatile-and-const
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
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

<span class="warn">Бо debug build зазвичай має `-O0`, а release build вмикає оптимізації.</span>

На `-O0` компілятор часто виконує кожне читання буквально, тому missing `volatile` може маскуватися. На `-O2` він кешує значення, прибирає redundant reads/writes і розкриває помилкове припущення, що hardware memory поводиться як звичайна RAM.

Захист: якщо peripheral polling або sensor read повертає stale data тільки в release, першими перевіряй register pointer types і volatile qualifiers.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
