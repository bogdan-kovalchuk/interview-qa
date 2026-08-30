---
id: emb-cppfound-0032
title: "Що виведе?<br><pre class=\"code-block\"><code><span class=\"code-type\">int</span> arr[]={<span class=\"code-num\">1</span>,<span class=\"code-num\">2</span>,<span class=\"code-num\">3</span>,<span class=\"code-num\">4</span>,<span class=\"code-num\">5</span>};<br><span class=\"code-type\">int</span> *p=arr+<span class=\"code-num\">4</span>;<br><span class=\"code-type\">int</span> *q=arr+<span class=\"code-num\">1</span>;<br><span class=\"code-fn\">printf</span>(\"%td\", p-q);</code></pre>"
description: "How pointer subtraction reports the number of elements between pointers."
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

<code>3</code>.<br><br>Відняття вказівників (<code>p - q</code>) повертає тип <code>ptrdiff_t</code> – кількість <span class="key">елементів між ними</span>, не байт: <code>(arr+4) - (arr+1) = 3</code> елементи.<br><br><code>%td</code> – формат для <code>ptrdiff_t</code>. Результат може бути від'ємним якщо <code>q > p</code>.<br><br>Фізично: байтова різниця = <code>3 * sizeof(int) = 12</code> байт, але pointer subtraction ділить на <code>sizeof(int)</code>.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
