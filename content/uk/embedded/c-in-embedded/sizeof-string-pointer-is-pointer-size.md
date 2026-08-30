---
id: emb-cppfound-0048
title: "Що поверне на 32-bit?<br><pre class=\"code-block\"><code>char *p = \"hello\";<br>printf(\"%zu\", sizeof(p));</code></pre>"
description: "Why sizeof on a string pointer returns the pointer size."
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

<span class="key">4</span> (на 64-bit – 8).<br><br><code>p</code> – вказівник типу <code>char*</code>. <code>sizeof(p) = sizeof(char*) = 4</code> на 32-bit. Не розмір рядка, не 6 (з '\0'), а лише розмір вказівника.<br><br>Для розміру рядка: <code>strlen(p) + 1</code> = 6 (з null-terminator) або <code>strlen(p)</code> = 5.<br><br>Порівняй: <code>char arr[] = "hello"; sizeof(arr) = 6</code> – тут масив, не вказівник.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
