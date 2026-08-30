---
id: emb-dtypes-0097
title: "Що таке memory region і як він задається у linker script?"
description: "Memory region - іменована ділянка адресного простору, задана атрибутами і межами у блоці MEMORY."
track: embedded
section: data-types-and-memory-layout
level: middle
type: concept
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

**Memory region** - іменована ділянка адресного простору. Задається у блоці `MEMORY` linker script:

`MEMORY {
  FLASH (rx)   : ORIGIN = 0x08000000, LENGTH = 512K
  RAM   (rwx)  : ORIGIN = 0x20000000, LENGTH = 128K
  CCMRAM (rwx) : ORIGIN = 0x10000000, LENGTH = 64K
}`

Атрибути: `r` - read, `w` - write, `x` - execute. Секції прив'язуються через `> REGION` у блоці `SECTIONS`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
