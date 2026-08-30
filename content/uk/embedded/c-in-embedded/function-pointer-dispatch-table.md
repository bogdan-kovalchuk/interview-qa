---
id: emb-cppfound-0057
title: "Що таке dispatch table і як реалізувати через function pointers?"
description: "How function-pointer dispatch tables select handlers."
track: embedded
section: c-in-embedded
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
    applicability: "Source question and answer; answer not independently verified."
---

## Short answer

<span class="key">Dispatch table</span> – масив function pointers для вибору обробника за індексом. Замінює великі <code>switch</code>-конструкції.<br><br><code>typedef void (*handler_t)(void);<br>handler_t table[16] = {<br>&nbsp;&nbsp;isr0, isr1, isr2, ...<br>};<br>// Виклик:<br>table[irq_num]();</code><br><br>Переваги: O(1) dispatch, легко розширити, підходить для RTOS task tables, state machines, protocol demultiplexers. У embedded: Cortex-M Vector Table – вбудований dispatch table у Flash.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

