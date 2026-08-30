---
id: emb-cppfound-0085
title: "Що робить <code>void(*isr_table[16])(void)</code> і як викликати ISR за індексом?"
description: "How an indexed table of function pointers dispatches interrupt handlers."
track: embedded
section: c-in-embedded
level: junior
type: mechanism
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
    applicability: "Source question and answer; answer not independently verified."
---

## Short answer

<code>void(*isr_table[16])(void)</code> – масив із 16 function pointers: кожен вказує на функцію без аргументів що повертає void.<br><br>Ініціалізація: <code>isr_table[0] = nmi_handler; isr_table[1] = hardfault_handler;</code><br><br>Виклик: <code>isr_table[irq_num]();</code> або <code>(*isr_table[irq_num])();</code><br><br>Це паттерн software interrupt controller або event dispatcher. Cortex-M Vector Table у Flash – апаратний аналог: масив адрес обробників переривань.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

