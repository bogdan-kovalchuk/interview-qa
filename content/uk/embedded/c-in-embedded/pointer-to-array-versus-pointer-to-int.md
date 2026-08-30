---
id: emb-cppfound-0015
title: "Що таке <code>int (*p)[8]</code> і чим відрізняється від <code>int *p</code>?"
description: "How a pointer to an array differs from a pointer to an int."
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

<code>int *p</code> – вказівник на <code>int</code>. <code>p+1</code> -> +4 байти (один <code>int</code>).<br><br><code>int (*p)[8]</code> – <span class="key">вказівник на масив</span> з 8 <code>int</code>. <code>p+1</code> -> +32 байти (один масив із 8 елементів).<br><br>Використання: при роботі з 2D масивами: <code>int arr[3][8]; int (*p)[8] = arr;</code>. <code>p[1]</code> -> другий рядок; <code>p[1][3]</code> -> <code>arr[1][3]</code>;<br><br>Правило читання: <code>(*p)</code> -> "вказівник на" (дужки важливі через пріоритет операторів).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
