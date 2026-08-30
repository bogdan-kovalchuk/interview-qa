---
id: emb-cppfound-0059
title: "Чи можна порівнювати вказівники (<code>&lt;</code>, <code>&gt;</code>) і коли це визначена поведінка?"
description: "When relational pointer comparisons are defined."
track: embedded
section: c-in-embedded
level: junior
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
    applicability: "Source question and answer; answer not independently verified."
---

## Short answer

Порівняння <code>==</code> та <code>!=</code> – завжди <span class="key">визначено</span> між будь-якими двома вказівниками одного типу.<br><br>Порівняння <code>&lt;</code>, <code>&gt;</code>, <code>&lt;=</code>, <code>&gt;=</code> – <span class="key">визначено лише</span> якщо обидва вказівники вказують на <span class="key">один і той самий масив</span> (або структуру). Порівняння вказівників різних об'єктів -> <span class="warn">UB за стандартом</span>.<br><br>Практика: більшість платформ дають коректну відповідь навіть для різних об'єктів, але не покладайся на це у portable коді.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

