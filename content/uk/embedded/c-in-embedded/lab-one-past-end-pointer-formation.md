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
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? c-in-embedded; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

<span class="key">One-past-the-end pointer</span> – вказівник на елемент одразу після останнього у масиві: <code>arr + N</code> для масиву з N елементів.<br><br>За стандартом C: формувати <span class="key">дозволено</span>, але <span class="warn">розіменовувати – UB</span>.<br><br>Використання: стандартний ідіом кінця: <code>int *end = arr + N; for(int *p=arr; p!=end; p++)</code>.<br><br>Вказівники далі (arr+N+1 і т.д.) – UB вже при формуванні. Тому: <span class="warn">тільки один елемент "після кінця"</span>.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
