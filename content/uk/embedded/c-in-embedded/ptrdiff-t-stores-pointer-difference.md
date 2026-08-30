---
id: emb-cppfound-0033
title: "Що таке <code>ptrdiff_t</code> і навіщо він потрібен?"
description: "The signed type used for differences between pointers."
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

<span class="key">ptrdiff_t</span> – знаковий цілочисельний тип для зберігання результату відняття двох вказівників. Визначений у <code>&lt;stddef.h&gt;</code>.<br><br>Розмір: відповідає розрядності платформи (32-bit -> 4B, 64-bit -> 8B).<br><br>Навіщо: <code>p - q</code> дає кількість елементів між вказівниками. Результат – знаковий (може бути від'ємним); Зберігати у <code>int</code> може бути недостатньо на 64-bit;<br><br>Форматна специфікація: <code>%td</code> для <code>printf</code>.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
