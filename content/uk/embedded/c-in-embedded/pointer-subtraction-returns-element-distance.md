---
id: emb-cppfound-0049
title: "Як pointer arithmetic поводиться при відніманні двох вказівників?"
description: "What pointer subtraction returns and when it is defined."
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

Відняття двох вказівників одного типу повертає <span class="key">ptrdiff_t</span> – кількість елементів між ними (не байт).<br><br><code>int *p = arr+4; int *q = arr+1; p - q = 3</code> (три <code>int</code>-елементи).<br><br>Умова: обидва вказівники мають вказувати на <span class="key">один масив</span> (або one-past-the-end). Відняття вказівників що вказують на різні масиви/об'єкти -> <span class="warn">UB</span>.<br><br>Застосування: <code>strlen</code>-подібний підрахунок, offset між елементами буфера.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
