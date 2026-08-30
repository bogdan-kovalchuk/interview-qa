---
id: emb-cppfound-0009
title: "Що таке array decay і в яких контекстах масив перетворюється на вказівник?"
description: "When an array is converted to a pointer to its first element."
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

<span class="key">Array decay</span> – автоматичне перетворення масиву на вказівник на його перший елемент.<br><br>Відбувається у більшості виразів:<br>• При передачі у функцію: <code>f(arr)</code> -> функція отримує <code>int*</code>;<br>• У арифметиці: <code>arr+1</code> -> <code>int*</code>;<br>• При присвоєнні: <code>int *p = arr</code>.<br><br>Наслідок: функція <span class="warn">втрачає інформацію про розмір</span> масиву. Тип стає <code>int*</code>, а не <code>int[N]</code>.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
