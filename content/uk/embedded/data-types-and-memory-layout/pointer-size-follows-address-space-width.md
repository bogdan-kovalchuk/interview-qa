---
id: emb-dtypes-0040
title: "Що поверне `sizeof(void*)` на 32-bit та 64-bit платформі?"
description: "Розмір вказівника визначається розрядністю адресного простору, а не типом, на який він вказує."
track: embedded
section: data-types-and-memory-layout
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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
    applicability: "Джерело питання і відповіді; відповідь не перевірена незалежно."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу data-types-and-memory-layout; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

32-bit (Cortex-M): `sizeof(void*) = 4` байти.
64-bit (x86-64, Cortex-A): `sizeof(void*) = 8` байтів.

Розмір вказівника визначається **розрядністю адресного простору**, а НЕ типом, на який він вказує: `sizeof(char*) == sizeof(int*) == sizeof(void*)` на одній платформі.

Перевіряй: `sizeof(void*)`. Не покладайся на конкретне значення у portable коді.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
