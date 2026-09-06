---
id: emb-fnptr-0046
title: "Чи можна мати масив функцій у C?"
description: "Ні, масив функцій неможливий; можна мати масив вказівників на функції."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: pitfall
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

Ні, масив функцій неможливий; можна мати масив вказівників на функції.

`void handlers[4](void);` – некоректна ідея, бо функції не є object-ами, які можна зберігати в масиві. Правильно: `void (*handlers[4])(void);` або typedef `handler_t handlers[4];`.

Правило: функцію не копіюють і не зберігають by value; зберігають адресу функції.[^embeddedinterviewlab]

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
