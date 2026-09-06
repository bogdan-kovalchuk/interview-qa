---
id: emb-structs-0037
title: "Що таке self-referential struct і чому для неї потрібен pointer?"
description: "Self-referential struct містить pointer на об'єкт свого ж типу, наприклад linked list node."
track: embedded
section: structs-unions-and-bitfields
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

**Self-referential struct** містить pointer на об'єкт свого ж типу, наприклад linked list node.

`struct Node { int value; struct Node *next; };` валідна, бо `next` має розмір pointer. А `struct Node next;` всередині самого `Node` неможлива: це вимагало б нескінченного розміру структури.

Embedded-use case: intrusive lists для RTOS queues, driver registries, free lists і memory pools.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
