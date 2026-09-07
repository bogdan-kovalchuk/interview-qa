---
id: emb-fnptr-0015
title: "Що означає параметр функції `void cb(int)` у декларації?"
description: "У параметрах функції це adjust-иться до function pointer: майже еквівалентно void register_cb(void (cb)(int));."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: concept
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
void register_cb(void cb(int));
```

## Short answer

У параметрах функції це adjust-иться до function pointer: майже еквівалентно `void register_cb(void (*cb)(int));`.

Функції не передаються by value. Параметр function type у function prototype автоматично перетворюється на pointer to function. Це схоже на array parameter, який перетворюється на pointer.

Правило: для ясності в callback API краще писати pointer syntax або typedef.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
