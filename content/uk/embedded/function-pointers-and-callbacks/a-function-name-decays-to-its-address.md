---
id: emb-fnptr-0007
title: "Що виведе цей код?"
description: "Виведе 42. Ім'я функції add1 у більшості виразів неявно перетворюється на pointer to function."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: mechanism
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
int add1(int x) { return x + 1; }
int (*op)(int) = add1;
printf("%d", op(41));
```

## Short answer

Виведе `42`.

Ім'я функції `add1` у більшості виразів неявно перетворюється на pointer to function. Тому `op = add1` еквівалентно `op = &add1`. Виклик `op(41)` виконує indirect call через адресу функції.

Правило: для function pointer можна писати і `op(41)`, і `(*op)(41)`; перший запис читабельніший.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
