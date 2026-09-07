---
id: emb-fnptr-0009
title: "Trap: що станеться при виклику null function pointer?"
description: "Undefined behavior. На Cortex-M це часто спроба перейти за адресою 0 або іншою invalid address, що може закінчитись HardFault."
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

## Question code

```c
void (*cb)(void) = NULL;
cb();
```

## Short answer

<span class="warn">Undefined behavior.</span>

На Cortex-M це часто спроба перейти за адресою 0 або іншою invalid address, що може закінчитись HardFault. Але стандарт C не гарантує жодного конкретного результату: це просто неправильний виклик.

Захист: перед optional callback завжди перевіряй `if (cb != NULL) { cb(); }`, або реєструй default no-op callback.[^embeddedinterviewlab]

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
