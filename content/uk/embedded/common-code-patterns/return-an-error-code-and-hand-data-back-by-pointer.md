---
id: emb-patterns-0018
title: "Як виглядає патерн error handling через return codes?"
description: "Функція повертає err_t, а дані віддає через output-pointer."
track: embedded
section: common-code-patterns
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
typedef enum {
  ERR_OK = 0, ERR_TIMEOUT, ERR_CRC, ERR_BUSY, ERR_PARAM
} err_t;

err_t sensor_read(uint8_t a, uint16_t *out);
```

## Short answer

**Функція повертає `err_t`, а дані віддає через output-pointer.**

`ERR_OK = 0` завжди нуль, тож `if (result) { /* error */ }` читабельний. Кожна гілка помилки повертає конкретний код.

Правило: return codes – дефолтний патерн, бо змушує викликача перевіряти результат.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
