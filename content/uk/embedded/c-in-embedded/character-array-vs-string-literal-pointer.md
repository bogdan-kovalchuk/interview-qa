---
id: emb-cppfound-0052
title: "Чим відрізняється `char arr[] = \"hello\"` від `char *p = \"hello\"`?"
description: "How writable character arrays differ from pointers to string literals."
track: embedded
section: c-in-embedded
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 2
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

`char arr[] = "hello"` – **масив**: компілятор виділяє 6 байт і копіює символи. Дані у writable пам'яті (stack або .data). `arr[0] = 'H'` – легально.

`char *p = "hello"` – **вказівник** на рядковий літерал у .rodata (Flash/read-only). `p[0] = 'H'` -> <span class="warn">UB/HardFault</span>.

`sizeof(arr) = 6`, `sizeof(p) = 4` (або 8). Масив у стеку, вказівник тільки зберігає адресу.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
