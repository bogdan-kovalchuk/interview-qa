---
id: emb-cppfound-0074
title: "Чим небезпечний VLA (variable length array) у embedded?"
description: "Why variable-length arrays complicate stack guarantees and analysis."
track: embedded
section: c-in-embedded
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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
    applicability: "Авторитетне джерело рівня секції для понять розділу c-in-embedded; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

**VLA** (C99) – масив з розміром визначеним під час виконання: `void f(int n) { int arr[n]; }`.

Небезпеки у embedded:

1. <span class="warn">Stack overflow</span>: розмір не відомий на compile-time -> не можна гарантувати достатньо стека;
2. Нема compile-time `sizeof` – важко аналізувати stack usage;
3. MISRA C:2012 та C11 – VLA опціональний (removed from mandatory);
4. Clang/GCC: `-Wvla` для попереджень.

Замість VLA: static масив максимального розміру + runtime перевірка розміру.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
