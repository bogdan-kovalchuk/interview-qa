---
id: emb-cppfound-0031
title: "Як пов'язані <code>arr[i]</code> і <code>*(arr+i)</code> за стандартом C?"
description: "Why array subscripting is defined through pointer arithmetic."
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

За стандартом C (§6.5.2.1): <span class="key"><code>arr[i]</code> визначається як <code>*(arr+i)</code></span>. Це не синтаксичний цукор – це точне визначення subscript operator.<br><br>Наслідки:<br>• <code>arr[2] == *(arr+2) == *(2+arr) == 2[arr]</code> – всі еквівалентні;<br>• Індексування – просто pointer arithmetic + dereference;<br>• Від'ємні індекси (<code>arr[-1]</code>) формально дозволені якщо вказівник вже зсунутий і результат вказує у межах масиву.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
