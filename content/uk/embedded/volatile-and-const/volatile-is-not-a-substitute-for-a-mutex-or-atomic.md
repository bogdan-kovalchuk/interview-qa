---
id: emb-volconst-0052
title: "Що означає `volatile` у multi-threaded C/C++ code: чи це заміна mutex/atomic?"
description: "Ні. volatile не замінює mutex, atomic або RTOS synchronization."
track: embedded
section: volatile-and-const
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

<span class="warn">Ні. `volatile` не замінює mutex, atomic або RTOS synchronization.</span>

Воно описує observable memory access, але не дає міжпотокової синхронізації, memory ordering або race-free інкрементів. У embedded RTOS задачі, які ділять змінні, потребують atomic primitives, mutex, queue, semaphore або critical section.

Правило: `volatile` для hardware/ISR/DMA visibility; synchronization primitives для concurrency correctness.[^embeddedinterviewlab]

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
