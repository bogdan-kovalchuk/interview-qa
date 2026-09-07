---
id: emb-fnptr-0011
title: "Trap: що не так із таким callback storage?"
description: "Callback може бути не зареєстрований або бути NULL."
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

## Question code

```c
static void (*rx_cb)(uint8_t);

void uart_isr(void) {
    rx_cb(0x55);
}
```

## Short answer

<span class="warn">Callback може бути не зареєстрований або бути `NULL`.</span>

Якщо ISR викличе `rx_cb` до реєстрації, буде undefined behavior і на MCU дуже ймовірний HardFault. У interrupt context це ще гірше: fault може виникнути асинхронно і важко відтворюватися.

Захист: ініціалізуй callback no-op функцією або перевіряй `if (rx_cb != NULL)`. Реєстрацію роби до enable interrupt.[^embeddedinterviewlab]

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
