---
id: emb-dtypes-0096
title: "Trap: що поверне malloc? `char *p = malloc(0);`"
description: "malloc(0) може повернути NULL або унікальний ненульовий вказівник - поведінка implementation-defined."
track: embedded
section: data-types-and-memory-layout
level: middle
type: pitfall
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

<span class="warn">Поведінка implementation-defined</span> за стандартом C (§7.22.3): реалізація може повернути або `NULL`, або унікальний ненульовий вказівник.

В обох випадках `*p` -> undefined behavior.
glibc: повертає ненульовий unique pointer. Embedded heap: може повернути `NULL`.

Практичне правило: <span class="warn">ніколи не викликай `malloc(0)`</span> - нема сенсу і поведінка непортабельна. Завжди перевіряй `size > 0` перед виділенням.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
