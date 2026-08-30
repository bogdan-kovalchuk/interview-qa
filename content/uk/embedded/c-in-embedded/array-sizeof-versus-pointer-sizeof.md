---
id: emb-cppfound-0010
title: "Що поверне <code>sizeof(arr)</code> vs <code>sizeof(p)</code> якщо <code>int arr[8]; int *p = arr;</code>?"
description: "Why sizeof an array differs from sizeof a pointer."
track: embedded
section: c-in-embedded
level: junior
type: concept
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

<code>sizeof(arr)</code> -> <span class="key">32</span> (8 елементів × 4 байти = 32B). <code>sizeof</code> на справжньому масиві повертає загальний розмір у байтах.<br><br><code>sizeof(p)</code> -> <span class="key">4</span> (або 8 на 64-bit). Вказівник зберігає лише адресу – його розмір = розрядність архітектури.<br><br>Ключова відмінність: масив і вказівник мають однаковий тип елементів, але <code>sizeof</code> дає зовсім різні результати.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
