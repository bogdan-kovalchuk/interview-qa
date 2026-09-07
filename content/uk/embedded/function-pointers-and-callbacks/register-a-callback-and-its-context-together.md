---
id: emb-fnptr-0006
title: "Як виглядає типовий embedded callback contract?"
description: "Типовий контракт: зареєструвати function pointer і context, а driver викликає їх при події."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: concept
tags: []
status: published
updated: 2026-09-06
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

Типовий контракт: зареєструвати function pointer і context, а driver викликає їх при події.

`typedef void (*uart_rx_cb_t)(void *ctx, uint8_t byte);` `int uart_set_rx_callback(Uart *u, uart_rx_cb_t cb, void *ctx);`

Driver не знає тип context. Він лише зберігає `ctx` і повертає його callback-у. Це дозволяє одному callback-коду працювати з різними об'єктами або буферами.

Правило: API має документувати коли викликається callback, з якого контексту, чи можна викликати blocking code, і скільки живе `ctx`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
