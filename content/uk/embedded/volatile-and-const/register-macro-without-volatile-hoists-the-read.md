---
id: emb-volconst-0007
title: "Trap: що не так із таким polling-кодом?"
description: "Бракує volatile у доступі до hardware register."
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

## Question code

```c
#define UART_SR (*( uint32_t *)0x40011000)

while ((UART_SR & 0x20) == 0) { }
```

## Short answer

<span class="warn">Бракує `volatile` у доступі до hardware register.</span>

`UART_SR` розіменовує звичайний `uint32_t *`, тож компілятор може закешувати перше прочитане значення status register і не перечитувати периферію. У release build polling може зависнути або бачити stale state.

Захист: `#define UART_SR (*(volatile uint32_t *)0x40011000u)`. Для vendor headers кожне register field у struct overlay має бути volatile-qualified.[^embeddedinterviewlab]

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
