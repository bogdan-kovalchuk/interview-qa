---
id: emb-fnptr-0020
title: "Trap: що не так із dispatch table без перевірки індексу?"
description: "Якщо opcode >= 4, буде out-of-bounds read і indirect call за випадковою адресою."
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
typedef void (*handler_t)(void);
static handler_t table[4];

table[opcode]();
```

## Short answer

<span class="warn">Якщо `opcode >= 4`, буде out-of-bounds read і indirect call за випадковою адресою.</span>

На Cortex-M це може стати HardFault або, гірше, перейти у валідну, але неправильну адресу коду. Dispatch tables особливо чутливі до input validation, бо дані одразу стають control flow.

Захист: перевіряй `if (opcode < ARRAY_SIZE(table) && table[opcode])`, інакше викликай default error handler.[^embeddedinterviewlab]

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
