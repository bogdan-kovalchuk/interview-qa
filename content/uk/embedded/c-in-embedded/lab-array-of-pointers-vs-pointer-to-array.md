---
id: emb-cppfound-0065
title: "Яка різниця між <code>int *arr[5]</code> і <code>int (*arr)[5]</code> у пам'яті?"
description: "How an array of pointers differs from a pointer to an array."
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

<code>int *arr[5]</code> – масив із 5 вказівників. Розмір: <code>5 × sizeof(int*) = 20 байт</code>. Кожен з 5 елементів – адреса якогось int. Можуть вказувати у різні місця пам'яті.<br><br><code>int (*arr)[5]</code> – один вказівник на масив із 5 int. Розмір <code>arr</code> = <code>sizeof(int*) = 4</code> байти. <code>arr+1</code> -> зміщення на <code>5 × sizeof(int) = 20</code> байт.<br><br>Читай: дужки навколо <code>*arr</code> – "вказівник на".[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
