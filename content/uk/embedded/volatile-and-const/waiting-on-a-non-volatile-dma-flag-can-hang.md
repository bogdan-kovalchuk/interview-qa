---
id: emb-volconst-0059
title: "Trap: що не так із таким очікуванням DMA?"
description: "Якщо dma_done змінює ISR або DMA callback, бракує volatile."
track: embedded
section: volatile-and-const
level: junior
type: pitfall
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

```c
uint8_t dma_done = 0;

while (!dma_done) { }
```

Якщо `dma_done` змінює ISR або DMA callback, бракує `volatile`.

Компілятор може прочитати `dma_done` один раз і залишитися в циклі назавжди. DMA hardware не змінює C-змінну напряму, але callback/ISR змінює її асинхронно відносно main loop.

Захист: `static volatile uint8_t dma_done;`. Для RTOS краще semaphore/event notification замість busy-wait.[^embeddedinterviewlab]

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
