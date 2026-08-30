---
id: emb-cppfound-0050
title: "Що виведе?<br><pre class=\"code-block\"><code>int arr[5]={1,2,3,4,5};<br>int *p=arr;<br>printf(\"%d %d\", *p++, *p);</code></pre>"
description: "Why modifying and reading a pointer in one printf call is undefined behavior."
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

<span class="warn">Undefined behavior</span> – порядок обчислення аргументів <code>printf</code> не визначений стандартом.<br><br><code>p++</code> – post-increment: повертає поточне значення і збільшує. Але між обчисленням <code>*p++</code> і <code>*p</code> в межах одного виклику функції немає sequence point. Компілятор може обчислити аргументи у будь-якому порядку.<br><br>Результат залежить від компілятора/платформи. Краще: <code>printf("%d %d", arr[0], arr[1]);</code>[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

