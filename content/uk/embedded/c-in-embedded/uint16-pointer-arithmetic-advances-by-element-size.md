---
id: emb-cppfound-0022
title: "Яку адресу матиме <code>p</code> після: <code>uint16_t arr[4]; uint16_t *p = arr; p += 2;</code>?"
description: "How typed pointer arithmetic determines the resulting address."
track: embedded
section: c-in-embedded
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
    applicability: "Source question and answer; answer not independently verified."
---

## Short answer

Якщо <code>arr</code> за адресою <code>0x2000</code> -> <code>p = 0x2000 + 2 * sizeof(uint16_t) = 0x2000 + 4 = 0x2004</code>.<br><br>Крок pointer arithmetic для <code>uint16_t*</code> = 2 байти. <code>p += 2</code> -> зсув на 2 елементи × 2 байти = 4 байти.<br><br>Тепер <code>p</code> вказує на <code>arr[2]</code>. Зважай: кроки завжди у "елементах типу", не у байтах.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
