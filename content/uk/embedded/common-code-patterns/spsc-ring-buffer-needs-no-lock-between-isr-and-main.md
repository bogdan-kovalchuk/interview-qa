---
id: emb-patterns-0007
title: "Що таке SPSC lock-free ring buffer і навіщо він?"
description: "SPSC (single-producer / single-consumer) кільцевий буфер, безпечний без вимкнення переривань за умови, що кожен індекс має одного writer-а і читається/пишеться атомарно для цієї MCU (microcontroller unit)."
track: embedded
section: common-code-patterns
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

**SPSC (single-producer / single-consumer) кільцевий буфер**, безпечний без вимкнення переривань за умови, що кожен індекс має одного writer-а і читається/пишеться атомарно для цієї MCU (microcontroller unit).

Типово: producer – ISR (interrupt service routine), наприклад UART RX (universal asynchronous receiver-transmitter receive), consumer – main loop. `head` і `tail` оновлюються кожен своєю стороною, тому спільного read-modify-write немає.

Правило: SPSC ring buffer – стандарт для UART RX/TX (receive/transmit), черг ADC (analog-to-digital converter) семплів і логування; завжди static allocation, без `malloc`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
