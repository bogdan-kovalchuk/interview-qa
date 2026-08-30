---
id: emb-cppfound-0071
title: "Trap: UB?<br><pre class=\"code-block\"><code>int arr[3]={1,2,3};<br>int *p=arr;<br>p--;<br>printf(\"%d\",*p);</code></pre>"
description: "Why decrementing a pointer at the beginning of an array is undefined."
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

<span class="warn">Так, UB.</span> <code>p = arr</code> -> вказівник на <code>arr[0]</code>. <code>p--</code> -> <code>arr-1</code>, що знаходиться <span class="warn">поза масивом</span>.<br><br>Допустимі вказівники для <code>arr[3]</code>: <code>arr</code> (=arr+0) до <code>arr+3</code> (one-past-the-end). <code>arr-1</code> – UB вже при формуванні, не тільки при розіменуванні.<br><br>Компілятор може припустити що UB не відбувається -> непередбачувані оптимізації. Отже, arr-1 формувати не можна.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
