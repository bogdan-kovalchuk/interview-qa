---
id: emb-cppfound-0078
title: "Що виведе?<br><pre class=\"code-block\"><code>int arr[]={5,10,15};<br>printf(\"%d\", 2[arr]);</code></pre>"
description: "Why the reversed subscript expression is valid C pointer arithmetic."
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

<code>15</code>.<br><br><code>2[arr]</code> -> за стандартом: <code>*(2 + arr)</code> – ідентично <code>arr[2]</code>. Subscript operator симетричний через комутативність додавання: <code>arr[2] == *(arr+2) == *(2+arr) == 2[arr]</code>.<br><br>Всі 4 форми дають однаковий код. <code>2[arr]</code> – валідний C, але нечитабельний. Зустрічається як питання на інтерв'ю для перевірки розуміння pointer arithmetic.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
