---
id: emb-cppfound-0053
title: "Що поверне <code>sizeof(\"hello\")</code> vs <code>sizeof(char*)</code> на 32-bit?"
description: "How sizeof treats a string literal and a pointer."
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

<code>sizeof("hello")</code> -> <span class="key">6</span>. Рядковий літерал – масив: <code>{'h','e','l','l','o','\0'}</code>. <code>sizeof</code> рядкового літерала повертає розмір масиву включно з null-terminator.<br><br><code>sizeof(char*)</code> -> <span class="key">4</span>. Розмір вказівника = розрядність платформи;<br><br>Важливо: <code>sizeof("hello")</code> не decay-ується до вказівника (sizeof – одне з трьох виключень array decay). Тому отримуємо розмір масиву.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
