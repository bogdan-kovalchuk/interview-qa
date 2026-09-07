---
id: emb-patterns-0020
title: "Що таке error struct патерн і коли він кращий за простий код?"
description: "Зберігає не лише код, а й контекст: рядок збою і час."
track: embedded
section: common-code-patterns
level: junior
type: mechanism
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
typedef struct {
  err_t    code;
  uint16_t line;      // __LINE__
  uint32_t timestamp; // tick
} err_info_t;
```

## Short answer

**Зберігає не лише код, а й контекст: рядок збою і час.**

Корисно для діагностики: `record_error(code, __LINE__)` у глобальний `last_error` дає мінімальний overhead і змогу зрозуміти, де саме сталася помилка.

Правило: context-rich error info – для діагностики складних/рідкісних збоїв.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
