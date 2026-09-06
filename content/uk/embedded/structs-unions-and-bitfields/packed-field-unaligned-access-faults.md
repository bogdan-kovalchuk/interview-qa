---
id: emb-structs-0012
title: "Trap: чому `__attribute__((packed))` може спричинити HardFault?"
description: "Бо multi-byte поле може стати невирівняним."
track: embedded
section: structs-unions-and-bitfields
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

Бо multi-byte поле може стати невирівняним.

Якщо `uint32_t value` у packed struct лежить на offset 1, доступ до нього може згенерувати unaligned load/store. На Cortex-M це залежить від ядра, налаштувань і типу інструкції: іноді працює повільніше, іноді дає UsageFault/HardFault, особливо для певних halfword/word або peripheral accesses.

Захист: для packed protocol data читай поля через `memcpy` у вирівняну локальну змінну або парсь байти явно.[^embeddedinterviewlab]

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
