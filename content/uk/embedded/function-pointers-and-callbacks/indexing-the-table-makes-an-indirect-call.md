---
id: emb-fnptr-0019
title: "Що виведе dispatch table?"
description: "Виведе 42. ops[1] – це pointer на dbl."
track: embedded
section: function-pointers-and-callbacks
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

```c
int inc(int x) { return x + 1; }
int dbl(int x) { return x * 2; }
int (*ops[])(int) = { inc, dbl };
printf("%d", ops[1](21));
```

Виведе `42`.

`ops[1]` – це pointer на `dbl`. Виклик `ops[1](21)` робить indirect call і повертає `21 * 2`.

Правило: масив function pointer-ів має містити функції з однаковою сумісною сигнатурою. Для різних сигнатур потрібні wrappers або variant dispatch.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
