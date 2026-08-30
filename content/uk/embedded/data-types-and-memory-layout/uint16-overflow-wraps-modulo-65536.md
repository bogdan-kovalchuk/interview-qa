---
id: emb-dtypes-0030
title: "Що поверне? `uint16_t x = 60000; x += 10000;`"
description: "Unsigned переповнення визначене стандартом як modular arithmetic, тому 60000+10000 дає 4464, а не undefined behavior."
track: embedded
section: data-types-and-memory-layout
level: middle
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

`x = 4464`.

`uint16_t` має діапазон `0..65535`. `60000 + 10000 = 70000` - виходить за межі.

Unsigned overflow **визначений стандартом** як modular arithmetic: `70000 mod 65536 = 4464`. Це НЕ undefined behavior (на відміну від signed overflow).

Але якщо очікувалось `70000` - баг від неправильного вибору типу. Використовуй `uint32_t`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
