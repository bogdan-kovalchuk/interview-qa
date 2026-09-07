---
id: emb-fnptr-0036
title: "Trap: чи можна зробити callback звичайною nested function у стандартному C?"
description: "Ні. Standard C не має nested functions."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 1
reconciled_with:
  en: 2
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

<span class="warn">Ні. Standard C не має nested functions.</span>

GCC підтримує nested functions як extension, але вони можуть використовувати trampolines на stack і погано підходять для portable embedded code, MPU/NX memory і static analysis. Такий callback може зламатися при іншому compiler або security settings.

Захист: використовуй file-scope static function + `void *context`, або в C++ non-capturing lambda/static member wrapper.[^embeddedinterviewlab]

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
