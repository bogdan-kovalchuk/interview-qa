---
id: emb-cppfound-0095
title: "Що виведе?<br><pre class=\"code-block\"><code><span class=\"code-type\">int</span> x=<span class=\"code-num\">5</span>;<br><span class=\"code-kw\">const</span> <span class=\"code-type\">int</span> *p=&amp;x;<br>x=<span class=\"code-num\">10</span>;<br><span class=\"code-fn\">printf</span>(\"%d\",*p);</code></pre>"
description: "Why a pointer to const cannot write while still observing direct changes to a non-const object."
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

<code>10</code>.<br><br><code>const int *p = &amp;x</code> – вказівник на const int: забороняє змінювати <code>*p</code> (через цей вказівник). Але <code>x</code> – не const! Зміна <code>x = 10</code> через пряме ім'я – легальна.<br><br><code>*p</code> читає значення <code>x</code> = 10. <code>const</code> захищає від запису через <code>p</code>, але не робить <code>x</code> незмінним.<br><br>Це важлива відмінність: <code>const int *p</code> vs <code>const int x</code>.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
