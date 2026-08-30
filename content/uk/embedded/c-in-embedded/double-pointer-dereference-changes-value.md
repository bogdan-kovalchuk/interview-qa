---
id: emb-cppfound-0045
title: "Що виведе?<br><pre class=\"code-block\"><code>int x=10;<br>int *p=&amp;x;<br>int **pp=&amp;p;<br>**pp=20;<br>printf(\"%d\",x);</code></pre>"
description: "How double dereferencing changes an object through a pointer chain."
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

<code>20</code>.<br><br>Ланцюжок: <code>pp</code> -> <code>&amp;p</code> (адреса вказівника <code>p</code>). <code>*pp</code> -> розіменування = сам вказівник <code>p</code> (адреса <code>x</code>). <code>**pp</code> -> подвійне розіменування = значення <code>x</code>.<br><br><code>**pp = 20</code> -> запис 20 у <code>x</code> через ланцюжок. <code>x</code> стає 20. Всі три: <code>x</code>, <code>*p</code>, <code>**pp</code> тепер = 20.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
