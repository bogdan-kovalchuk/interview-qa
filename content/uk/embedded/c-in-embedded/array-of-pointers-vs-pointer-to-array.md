---
id: emb-cppfound-0042
title: "Яка різниця між масивом вказівників <code>int *arr[8]</code> і вказівником на масив <code>int (*arr)[8]</code>?"
description: "How array-of-pointers and pointer-to-array declarations differ."
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

<code>int *arr[8]</code> – <span class="key">масив із 8 вказівників</span> на int. Розмір: 8 × 4 = 32 байти. Кожен елемент – окрема адреса. Може вказувати на різні масиви різних розмірів.<br><br><code>int (*arr)[8]</code> – <span class="key">вказівник на масив</span> із 8 int. Розмір самого <code>arr</code> = 4 байти (вказівник). <code>arr+1</code> -> +32 байти (розмір масиву із 8 int).<br><br>Пріоритет операторів: <code>[]</code> сильніший ніж <code>*</code>, тому потрібні дужки.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

