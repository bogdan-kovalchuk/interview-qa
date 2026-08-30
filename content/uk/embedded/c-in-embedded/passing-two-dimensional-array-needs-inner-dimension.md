---
id: emb-cppfound-0029
title: "Як правильно передати 2D масив у функцію та звернутись до елемента <code>[2][3]</code>?"
description: "Why a two-dimensional array parameter needs its inner dimension."
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

Для статично розмірного масиву потрібно вказати <span class="key">розмір внутрішнього виміру</span>:<br><code>void f(int arr[][4], int rows) { arr[2][3] = 99; }</code><br>або еквівалентно:<br><code>void f(int (*arr)[4], int rows) { ... }</code><br><br>Без розміру компілятор не знає крок рядка (stride). <code>arr[i][j]</code> -> <code>*(*(arr+i)+j)</code> -> в пам'яті: <code>arr + i*4*sizeof(int) + j*sizeof(int)</code>.<br><br>Для динамічного: передавай як <code>int *</code> і обчислюй offset вручну.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
