---
id: emb-cppfound-0087
title: "Що таке \"one-past-the-end\" pointer і які операції з ним дозволені?"
description: "Which operations are valid for a pointer one element past an array."
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

<span class="key">One-past-the-end</span> – вказівник на елемент одразу після масиву: <code>int *end = arr + N</code>. За стандартом C – легальний.<br><br>Дозволено:<br>• <span class="key">Формувати</span> (адреса коректна);<br>• <span class="key">Порівнювати</span>: <code>p != end</code>, <code>p &lt;= end</code>;<br>• <span class="key">Віднімати</span> від іншого вказівника у масиві.<br><br>Заборонено:<br>• <span class="warn">Розіменовувати</span>: <code>*end</code> -> UB;<br>• <span class="warn">Збільшувати далі</span>: <code>end+1</code> -> UB.<br><br>Стандартний ідіом: <code>for(int *p=arr; p!=arr+N; p++)</code>[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
