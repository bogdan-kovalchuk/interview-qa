---
id: emb-cppfound-0066
title: "Trap: що виведе?<br><pre class=\"code-block\"><code>int a=1;<br>int *p=&amp;a;<br>int *q=&amp;a;<br>q++;<br>printf(\"%d\",*q);</code></pre>"
description: "Why pointer arithmetic on a pointer to a standalone object is undefined."
track: embedded
section: c-in-embedded
level: junior
type: pitfall
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

<span class="warn">Undefined behavior</span>. <code>q++</code> -> <code>q</code> тепер вказує на адресу одразу після <code>a</code> на стеку. Це не елемент масиву – лише окрема змінна.<br><br>Pointer arithmetic визначена тільки в межах масиву (або struct за умовами). Для двох окремих змінних – навіть якщо вони поруч на стеку – <code>&amp;a + 1</code> -> UB;<br><br>Компілятор може розмістити <code>a</code> у регістрі без адреси у пам'яті -> <code>*q</code> читає сміття.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
