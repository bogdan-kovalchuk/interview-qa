---
id: emb-cppfound-0075
title: "Реалізуйте функцію пошуку максимуму масиву через pointer traversal."
description: "A pointer-traversal implementation for finding the maximum array element."
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
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? c-in-embedded; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

<code>int find_max(const int *arr, size_t n) {<br>&nbsp;&nbsp;if(arr == NULL || n == 0) return INT_MIN;<br>&nbsp;&nbsp;const int *p = arr;<br>&nbsp;&nbsp;const int *end = arr + n;<br>&nbsp;&nbsp;int max = *p++;<br>&nbsp;&nbsp;while(p != end) {<br>&nbsp;&nbsp;&nbsp;&nbsp;if(*p &gt; max) max = *p;<br>&nbsp;&nbsp;&nbsp;&nbsp;p++;<br>&nbsp;&nbsp;}<br>&nbsp;&nbsp;return max;<br>}</code><br><br>Ключові моменти: <code>const int*</code> – читання без зміни, <code>size_t n</code> – розмір явно, <code>arr + n</code> – one-past-the-end як sentinel. <code>INT_MIN</code> потребує <code>&lt;limits.h&gt;</code>; у real API краще повертати status окремо від значення.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
