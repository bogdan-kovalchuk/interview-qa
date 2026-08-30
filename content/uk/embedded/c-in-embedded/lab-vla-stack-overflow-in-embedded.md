---
id: emb-cppfound-0074
title: "Чим небезпечний VLA (variable length array) у embedded?"
description: "Why variable-length arrays complicate stack guarantees and analysis."
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

<span class="key">VLA</span> (C99) – масив з розміром визначеним під час виконання: <code>void f(int n) { int arr[n]; }</code>.<br><br>Небезпеки у embedded:<br>1. <span class="warn">Stack overflow</span>: розмір не відомий на compile-time -> не можна гарантувати достатньо стека;<br>2. Нема compile-time <code>sizeof</code> – важко аналізувати stack usage;<br>3. MISRA C:2012 та C11 – VLA опціональний (removed from mandatory);<br>4. Clang/GCC: <code>-Wvla</code> для попереджень.<br><br>Замість VLA: static масив максимального розміру + runtime перевірка розміру.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
