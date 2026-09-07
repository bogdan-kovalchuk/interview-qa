---
id: emb-macros-0015
title: "Що таке include guard і яку проблему він вирішує?"
description: "Include guard запобігає повторному включенню header у той самий translation unit."
track: embedded
section: inline-and-macros
level: junior
type: concept
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
#ifndef SENSOR_H
#define SENSOR_H
/* вміст header */
#endif
```

## Short answer

**Include guard запобігає повторному включенню header** у той самий translation unit.

Без нього подвійний `#include` призведе до <span class="warn">redefinition</span> типів, `struct`, прототипів. При першому проході `SENSOR_H` ще не визначений -> вміст обробляється і guard визначається; наступні рази вміст пропускається.

Правило: кожен header має guard з унікальним ім'ям, або `#pragma once`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
