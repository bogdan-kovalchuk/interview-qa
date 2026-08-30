---
id: emb-cppfound-0082
title: "Що таке pointer decay при передачі масиву як аргументу функції?"
description: "Why an array argument becomes a pointer to its first element."
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

При передачі масиву у функцію він <span class="key">автоматично перетворюється</span> на вказівник на перший елемент (decay).<br><br><code>int arr[8];</code><br><code>f(arr)</code> -> <code>f(int *)</code> – функція отримує вказівник.<br><br>Наслідки:<br>• <code>sizeof(arr)</code> всередині функції = <code>sizeof(int*)</code>, не 32;<br>• Нема copy – функція отримує доступ до оригінального масиву;<br>• Нема range checking.<br><br>Рішення: <code>f(int arr[], size_t n)</code> або у C++: <code>template&lt;size_t N&gt; f(int (&amp;arr)[N])</code>.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
