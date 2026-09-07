---
id: emb-patterns-0012
title: "Чому розмір ring buffer роблять степенем двійки?"
description: "(index + 1) & MASK – одна інструкція AND, а (index + 1) % SIZE вимагає ділення."
track: embedded
section: common-code-patterns
level: junior
type: concept
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

## Question code

```c
#define RB_SIZE 64
#define RB_MASK (RB_SIZE - 1)
```

## Short answer

**`(index + 1) & MASK` – одна інструкція AND, а `(index + 1) % SIZE` вимагає ділення.**

На Cortex-M0 немає апаратного дільника, тож modulo <span class="warn">у 10–20 разів повільніше</span>. Степінь двійки дозволяє замінити `%` на бітову маску.

Правило: розмір кільцевого буфера = степінь 2, wrap через `& (SIZE-1)`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
