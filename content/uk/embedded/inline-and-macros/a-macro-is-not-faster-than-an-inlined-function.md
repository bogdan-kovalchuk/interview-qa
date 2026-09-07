---
id: emb-macros-0026
title: "Trap: чи правда, що макрос завжди швидший за функцію?"
description: "Ні – це застарілий міф."
track: embedded
section: inline-and-macros
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

<span class="warn">Ні – це застарілий міф.</span>

Сучасні компілятори inline-ять дрібні `static inline` функції так само, як розгортається макрос, і при цьому додають constant folding, dead-code elimination та інші оптимізації, недоступні вже підставленому препроцесором тексту.

Захист: на інтерв'ю не кажи «макрос швидший»; кажи «`static inline` дає ту саму швидкість плюс type safety і однократне обчислення аргументів».[^embeddedinterviewlab]

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
