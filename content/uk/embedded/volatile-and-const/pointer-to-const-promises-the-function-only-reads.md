---
id: emb-volconst-0016
title: "Що означає `const uint8_t *buf` у параметрі функції?"
description: "Функція отримує pointer to const uint8_t: вона може пересувати pointer, але не може змінювати байти буфера через buf."
track: embedded
section: volatile-and-const
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

**Функція отримує pointer to const `uint8_t`**: вона може пересувати pointer, але не може змінювати байти буфера через `buf`.

Наприклад, `void uart_write(const uint8_t *buf, size_t len)` документує, що переданий buffer буде лише прочитаний. Це дозволяє передавати як mutable RAM buffer, так і read-only flash table.

Правило: якщо функція не змінює pointed-to data, параметр має бути `const T *`. Це підтримує const-correctness і відповідає MISRA-підходу.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
