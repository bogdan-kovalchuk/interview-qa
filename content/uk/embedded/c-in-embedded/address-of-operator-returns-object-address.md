---
id: emb-cppfound-0004
title: "Що таке операція взяття адреси <code>&amp;</code> і що вона повертає?"
description: "What the address-of operator returns and where it cannot be used."
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

Оператор <code>&amp;</code> (address-of) повертає <span class="key">адресу об'єкта</span> у пам'яті – значення типу "вказівник на тип об'єкта".<br><br><code>int x = 5; int *p = &amp;x;</code> – <code>p</code> тепер вказує на <code>x</code>.<br><br>Не можна взяти адресу:<br>• виразів без lvalue (<code>&amp;(a+b)</code> – помилка);<br>• <code>register</code> змінних;<br>• bit-field полів структури.<br><br>Типи: <code>&amp;int</code> -> <code>int*</code>, <code>&amp;arr</code> -> <code>int(*)[N]</code> (вказівник на масив, не на елемент).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
