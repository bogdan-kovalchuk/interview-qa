---
id: emb-structs-0036
title: "Чому incomplete struct не можна створити як object у header?"
description: "Неможливо, бо compiler не знає розмір Driver."
track: embedded
section: structs-unions-and-bitfields
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

## Short answer

```c
typedef struct Driver Driver;

Driver d;
```

<span class="warn">Неможливо, бо compiler не знає розмір `Driver`.</span>

Forward declaration створює incomplete type. Можна оголошувати pointer-и на нього, бо розмір pointer відомий, але не можна виділити object by value або звертатися до полів.

Захист: opaque API повертає `Driver *` або приймає caller-provided storage через окремий API, який знає потрібний розмір/вирівнювання.[^embeddedinterviewlab]

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
