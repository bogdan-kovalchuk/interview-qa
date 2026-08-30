---
id: emb-cppfound-0024
title: "Що виведе?<br><pre class=\"code-block\"><code><span class=\"code-type\">int</span> arr[<span class=\"code-num\">3</span>][<span class=\"code-num\">4</span>];<br><span class=\"code-fn\">printf</span>(\"%zu\", <span class=\"code-kw\">sizeof</span>(arr));</code></pre>"
description: "How sizeof reports the size of a two-dimensional array."
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

<span class="key">48</span> байт.<br><br><code>arr</code> – 2D масив: 3 рядки × 4 стовпці × <code>sizeof(int) = 4</code> байти = 48B.<br><br><code>sizeof(arr[0])</code> = <code>sizeof(int[4])</code> = 16B (один рядок).<br><code>sizeof(arr[0][0])</code> = <code>sizeof(int)</code> = 4B.<br><br>Кількість рядків: <code>sizeof(arr)/sizeof(arr[0]) = 48/16 = 3</code>. Цей трюк працює лише у тому ж scope де оголошений масив.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
