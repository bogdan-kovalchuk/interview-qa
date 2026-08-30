---
id: emb-cppfound-0062
title: "Як передати масив у функцію і зберегти інформацію про його розмір?"
description: "Ways to preserve array length when array-to-pointer decay removes it."
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

Оскільки масив decay-ується до вказівника, розмір <span class="warn">не передається автоматично</span>. Варіанти:<br><br>1) <span class="key">Явний параметр</span>: <code>void f(int *arr, size_t n)</code> – найпростіше;<br>2) <span class="key">Sentinel value</span>: null-terminator для рядків, спеціальне значення;<br>3) <span class="key">Struct + масив</span>: <code>struct { int *data; size_t len; }</code>;<br>4) C++ <span class="key">std::span</span> або <code>std::array&lt;int,N&gt;</code>.<br><br>Захист: <code>_Static_assert(sizeof(arr) != sizeof(int*), "Use real array")</code> у caller.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
