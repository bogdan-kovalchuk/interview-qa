---
id: emb-cppfound-0093
title: "Що виведе?<br><pre class=\"code-block\"><code><span class=\"code-type\">int</span> arr[<span class=\"code-num\">4</span>]={<span class=\"code-num\">10</span>,<span class=\"code-num\">20</span>,<span class=\"code-num\">30</span>,<span class=\"code-num\">40</span>};<br><span class=\"code-fn\">printf</span>(\"%d %d\",*(arr+<span class=\"code-num\">3</span>), arr[<span class=\"code-num\">3</span>]);</code></pre>"
description: "Why array subscripting and pointer arithmetic are equivalent in C."
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

Обидва виводять <code>40</code>.<br><br><code>*(arr+3)</code> -> pointer arithmetic: зсув на 3 елементи, розіменування = <code>arr[3] = 40</code>.<br><code>arr[3]</code> -> subscript operator, за визначенням = <code>*(arr+3)</code>.<br><br>Вони <span class="key">ідентичні за стандартом</span>. Компілятор генерує однаковий машинний код для обох варіантів.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

