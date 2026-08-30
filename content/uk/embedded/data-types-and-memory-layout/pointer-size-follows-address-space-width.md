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
    applicability: "Джерело питання і відповіді; відповідь не перевірена незалежно."
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
