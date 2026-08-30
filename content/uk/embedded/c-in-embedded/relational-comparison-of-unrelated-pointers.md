---
id: emb-cppfound-0088
title: "Що виведе?<br><pre class=\"code-block\"><code><span class=\"code-type\">int</span> a=<span class=\"code-num\">1</span>,b=<span class=\"code-num\">2</span>;<br><span class=\"code-type\">int</span> *p=&amp;a,*q=&amp;b;<br><span class=\"code-fn\">printf</span>(\"%d\", p&lt;q);</code></pre>"
description: "Why relational comparison of pointers to different objects is undefined in C."
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

<span class="warn">Undefined behavior за стандартом C</span>. Реляційне порівняння (<code>&lt;</code>, <code>&gt;</code>) вказівників з різних об'єктів не визначено стандартом.<br><br>На практиці (більшість платформ, flat memory): результат залежить від розміщення змінних у пам'яті (порядок на стеку залежить від компілятора). Не portable;<br><br>Дозволено: <code>p == q</code>, <code>p != q</code> – порівняння на рівність між будь-якими вказівниками. Реляційні – тільки в межах одного масиву.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
