---
id: emb-fnptr-0053
title: "Trap: чому weak hooks гірші за explicit callback для кількох інстансів driver-а?"
description: "Weak function має одне глобальне ім'я і не несе per-instance context."
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

<span class="warn">Weak function має одне глобальне ім'я і не несе per-instance context.</span>

Якщо є два UART-и або два timer-и, один weak hook не знає, до якого об'єкта належить подія, якщо це не передано окремо. Також weak override прихований на рівні linker-а, що ускладнює тестування і dependency tracking.

Захист: для reusable drivers використовуй explicit registration `cb + ctx`; weak hooks залишай для startup defaults або board-level extension points.[^embeddedinterviewlab]

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
