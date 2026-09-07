---
id: emb-fnptr-0025
title: "Trap: чому не можна просто привести будь-яку адресу до function pointer і викликати?"
description: "Адреса може не бути валідною entry address для функції з потрібною ABI-сигнатурою."
track: embedded
section: function-pointers-and-callbacks
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

## Short answer

<span class="warn">Адреса може не бути валідною entry address для функції з потрібною ABI-сигнатурою.</span>

На Cortex-M function addresses мають Thumb-state bit semantics; виклик невірної адреси може дати HardFault. Також адреса може вказувати на data memory, padding, bootloader table або функцію з іншою calling convention.

Захист: викликай тільки валідні function entry points з правильною сигнатурою. Для bootloader jump використовуй documented sequence: deinit, set MSP, set VTOR, jump to Reset_Handler.[^embeddedinterviewlab]

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
