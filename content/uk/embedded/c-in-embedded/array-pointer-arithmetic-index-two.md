---
id: emb-cppfound-0008
title: "Що виведе?<br><pre class=\"code-block\"><code>int arr[5] = {10,20,30,40,50};<br>int *p = arr;<br>printf(\"%d\", *(p+2));</code></pre>"
description: "How pointer arithmetic accesses the third array element."
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

<code>30</code>.<br><br><code>arr</code> decay-ується до вказівника на перший елемент. <code>p = arr</code> -> <code>p</code> вказує на <code>arr[0]</code>.<br><br><code>p+2</code> -> вказівник на <code>arr[2]</code> (кроком <code>2 * sizeof(int) = 8</code> байт на 32-bit).<br><code>*(p+2)</code> -> розіменування -> <code>arr[2] = 30</code>.<br><br>За стандартом: <code>arr[i] ≡ *(arr+i) ≡ *(i+arr) ≡ i[arr]</code> – всі чотири форми еквівалентні.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
