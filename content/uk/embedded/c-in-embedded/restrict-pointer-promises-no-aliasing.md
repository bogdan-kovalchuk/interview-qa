---
id: emb-cppfound-0028
title: "Що таке <code>restrict</code> і навіщо він потрібен у embedded?"
description: "How restrict communicates non-aliasing to the compiler."
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

<code>restrict</code> (C99) – кваліфікатор вказівника, що гарантує компілятору: через цей вказівник і через жоден інший вказівник у цій функції <span class="key">не відбувається aliasing</span> (перекриття областей пам'яті).<br><br>Приклад: <code>void add(int * restrict dst, const int * restrict src, int n)</code>.<br><br>Дає компілятору дозвіл на агресивну оптимізацію (векторизація, підкачка у регістри). Важливо для DSP, crypto, memcpy-like функцій. Якщо aliasing все ж є – UB.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
