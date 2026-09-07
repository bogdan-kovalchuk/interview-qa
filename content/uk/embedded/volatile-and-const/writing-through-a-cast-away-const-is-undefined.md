---
id: emb-volconst-0032
title: "Trap: чи безпечно прибрати `const` cast-ом?"
description: "Ні: якщо початковий об'єкт був оголошений const, спроба змінити його через non-const lvalue має undefined behavior."
track: embedded
section: volatile-and-const
level: junior
type: pitfall
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
const uint32_t cfg = 10;
uint32_t *p = (uint32_t *)&cfg;
*p = 20;
```

## Short answer

<span class="warn">Ні: якщо початковий об'єкт був оголошений `const`, спроба змінити його через non-const lvalue має undefined behavior.</span>

На MCU `cfg` може лежати у Flash/`.rodata`, і запис через `p` може спричинити BusFault/HardFault або просто не змінити дані. Навіть якщо адреса в RAM, оптимізатор може припускати, що `cfg` не змінюється.

Захист: не cast-away `const` для запису. Якщо дані мають змінюватися, вони не повинні бути `const`.[^embeddedinterviewlab]

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
