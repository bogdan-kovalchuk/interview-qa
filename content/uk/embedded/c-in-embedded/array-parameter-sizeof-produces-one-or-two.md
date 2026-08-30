---
id: emb-cppfound-0016
title: "Trap: <code>void f(int arr[]) { int n = sizeof(arr)/sizeof(arr[0]); }</code> – яке значення <code>n</code>?"
description: "Why the array-length idiom fails for an array parameter."
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

<code>n = 1</code> (на 32-bit) або <code>n = 2</code> (на 64-bit).<br><br>У параметрі функції <code>int arr[]</code> ≡ <code>int *arr</code> – decay до вказівника. <code>sizeof(arr) = sizeof(int*) = 4</code> (або 8). <code>sizeof(arr[0]) = sizeof(int) = 4</code>. Тому <code>4/4 = 1</code>.<br><br><span class="warn">Не 8, не 256, не розмір масиву</span> – лише 1 або 2.<br><br>Завжди передавай розмір явно: <code>void f(int *arr, size_t n)</code>. Захист: <code>_Static_assert</code> у caller.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
