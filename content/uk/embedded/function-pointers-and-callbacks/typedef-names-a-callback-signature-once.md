---
id: emb-fnptr-0004
title: "Що означає такий typedef?"
description: "timer_cb_t – це тип pointer to function, яка приймає void ctx і повертає void."
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
typedef void (*timer_cb_t)(void *ctx);
```

**`timer_cb_t`** – це тип pointer to function, яка приймає `void *ctx` і повертає `void`.

Після цього можна писати `timer_cb_t cb;`, `void timer_start(timer_cb_t cb, void *ctx);`. Такий typedef різко зменшує шум у driver APIs і робить callback contract видимим.

Embedded-правило: callback type краще оголошувати один раз у header, а не дублювати raw function pointer syntax у кожній функції.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
