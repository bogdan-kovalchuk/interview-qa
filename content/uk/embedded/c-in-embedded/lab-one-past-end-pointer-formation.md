---
id: emb-cppfound-0067
title: "Що таке \"pointer past the end\" і коли його можна формувати?"
description: "How the one-past-the-end pointer is formed and used safely."
track: embedded
section: c-in-embedded
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 2
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
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу c-in-embedded; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

**One-past-the-end pointer** – вказівник на елемент одразу після останнього у масиві: `arr + N` для масиву з N елементів.

За стандартом C: формувати **дозволено**, але <span class="warn">розіменовувати – UB</span>.

Використання: стандартний ідіом кінця: `int *end = arr + N; for(int *p=arr; p!=end; p++)`.

Вказівники далі (arr+N+1 і т.д.) – UB вже при формуванні. Тому: <span class="warn">тільки один елемент "після кінця"</span>.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
