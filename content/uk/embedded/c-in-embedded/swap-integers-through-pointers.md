---
id: emb-cppfound-0055
title: "Як реалізувати swap двох int через вказівники?"
description: "How to swap two integers through pointer parameters."
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

<code>void swap(int *a, int *b) {<br>&nbsp;&nbsp;int tmp = *a;<br>&nbsp;&nbsp;*a = *b;<br>&nbsp;&nbsp;*b = tmp;<br>}</code><br><br>Виклик: <code>int x=5, y=10; swap(&amp;x, &amp;y);</code> -> <code>x=10, y=5</code>.<br><br>Без tmp через XOR: <code>*a^=*b; *b^=*a; *a^=*b;</code> – але <span class="warn">UB якщо <code>a == b</code></span> (aliasing той самий об'єкт). Передавай завжди адреси (через <code>&amp;</code> у caller), не значення.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
