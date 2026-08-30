---
id: emb-cppfound-0051
title: "Trap: UB?<br><pre class=\"code-block\"><code>int arr[4]={1,2,3,4};<br>int *p=arr;<br>int *q=arr+5;</code></pre>"
description: "Why forming arr+5 is undefined for a four-element array."
track: embedded
section: c-in-embedded
level: junior
type: pitfall
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

<span class="warn">Так, UB вже при формуванні <code>arr+5</code></span>.<br><br>Для масиву <code>arr[4]</code> (4 елементи) допустимі вказівники: <code>arr</code> до <code>arr+4</code> включно (one-past-the-end). <code>arr+5</code> виходить за one-past-the-end -> <span class="warn">UB навіть без розіменування</span>.<br><br>Компілятор може використовувати це припущення для оптимізації, що призводить до непередбачуваної поведінки. GCC з <code>-fsanitize=undefined</code> виявить це.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

