---
id: emb-dtypes-0063
title: "Яке значення матиме? `uint8_t result = (uint8_t)(200 + 100)`"
description: "Явний cast усікає результат так само, як і неявне присвоєння, тож result дорівнює 44."
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

`result = 44`.

`200 + 100` обчислюється як `int` (integer promotion): `300`. Явний cast `(uint8_t)` усікає до 8 біт: `300 & 0xFF = 0x2C = 44`.

Відмінність від implicit: явний cast показує усвідомлення truncation. Але результат однаковий - 44.

Для portable коду: перевіряй що значення вміщується у цільовий тип перед звуженням.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
