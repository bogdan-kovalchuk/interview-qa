---
id: emb-dtypes-0088
title: "Як виглядає у пам'яті? `struct { uint32_t flags:1; uint32_t mode:3; uint32_t value:28; }`"
description: "Три бітові поля пакуються в один uint32_t, але порядок пакування бітів implementation-defined."
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

Bitfield layout: один `uint32_t` (1+3+28=32 біти). Розмір: **4 байти**.

На ARM GCC (від LSB): bits `[0]` -> `flags`, bits `[3:1]` -> `mode`, bits `[31:4]` -> `value`.

<span class="warn">Але</span>: порядок пакування бітів - implementation-defined! Для hardware registers безпечніше: явні маски + зсуви над `uint32_t` або перевірка layout через `static_assert`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
