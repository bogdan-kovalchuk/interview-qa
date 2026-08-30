---
id: emb-cppfound-0020
title: "Що виведе?<br><pre class=\"code-block\"><code>int a=1,b=2,c=3;<br>int *arr[3]={&amp;a,&amp;b,&amp;c};<br>printf(\"%d\",*arr[1]);</code></pre>"
description: "How dereferencing an element of an array of pointers accesses its value."
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

<code>2</code>.<br><br><code>int *arr[3]</code> – масив з 3 вказівників на <code>int</code>. <code>arr[1]</code> -> другий елемент = <code>&amp;b</code>. <code>*arr[1]</code> -> розіменування <code>&amp;b</code> -> значення <code>b = 2</code>.<br><br>Зберігання: <code>arr</code> – масив адрес (3 × 4 байти = 12 байт). Кожен елемент – окрема адреса. Зміна <code>*arr[1] = 99</code> -> змінить <code>b</code>.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
