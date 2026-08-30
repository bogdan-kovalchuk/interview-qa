---
id: emb-cppfound-0097
title: "Що таке array of function pointers і де використовується у embedded?"
description: "How function-pointer arrays implement constant-time dispatch tables."
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

<code>void (*handlers[8])(void)</code> – масив із 8 function pointers.<br><br>Використання:<br>• <span class="key">Software interrupt router</span>: <code>handlers[irq_id]();</code>;<br>• <span class="key">State machine</span>: <code>state_fn[current_state]();</code>;<br>• <span class="key">Protocol parser</span>: <code>cmd_handlers[cmd_id](payload);</code>;<br>• <span class="key">Bootloader jump</span>: таблиця точок входу у Flash.<br><br>Переваги: O(1) dispatch, легко розширювати через зміну таблиці. Cortex-M Vector Table – апаратна реалізація цього паттерну.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->


