---
id: emb-cppfound-0043
title: "Яке значення повертає <code>&amp;arr</code> і як відрізняється від <code>arr</code> якщо <code>int arr[8]</code>?"
description: "Why <code>arr</code> and <code>&amp;arr</code> share an address but have different pointer types."
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

Обидва вирази дають <span class="key">однакову числову адресу</span> (адресу першого елемента масиву), але мають різні <span class="key">типи</span>:<br><br><code>arr</code> -> decay до <code>int*</code>. <code>arr+1</code> -> +4 байти (один int).<br><code>&amp;arr</code> -> <code>int(*)[8]</code> (вказівник на масив). <code>&amp;arr+1</code> -> +32 байти (один масив).<br><br>Практично: <code>&amp;arr</code> використовується для передачі у функцію що очікує <code>int(*)[8]</code> – зберігає розмір масиву у типі.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

