---
id: emb-cppfound-0076
title: "Trap: яка помилка?<br><pre class=\"code-block\"><code>char buf[4]=\"abc\";<br>buf[4]='\\0';</code></pre>"
description: "Why writing at the first index after a string buffer is a buffer overflow."
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

<span class="warn">Buffer overflow!</span> <code>char buf[4] = "abc"</code> -> <code>buf = {'a','b','c','\0'}</code>. Масив 4 елементи, індекси 0..3. <code>buf[4]</code> – п'ятий елемент, за межами масиву.<br><br>Ще проблема: <code>"abc"</code> вже має '\0' на позиції 3 – null-terminator вже є. Рядок коректний;<br><br>Якби <code>char buf[3] = "abc"</code> – компілятор попередить або поміщає 'a','b','c' без '\0' (усікання); Завжди розмір буфера &gt; довжина рядка + 1.[^embeddedinterviewlab]

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
