---
id: emb-cppfound-0052
title: "Чим відрізняється <code>char arr[] = \"hello\"</code> від <code>char *p = \"hello\"</code>?"
description: "How writable character arrays differ from pointers to string literals."
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

<code>char arr[] = "hello"</code> – <span class="key">масив</span>: компілятор виділяє 6 байт і копіює символи. Дані у writable пам'яті (stack або .data). <code>arr[0] = 'H'</code> – легально.<br><br><code>char *p = "hello"</code> – <span class="key">вказівник</span> на рядковий літерал у .rodata (Flash/read-only). <code>p[0] = 'H'</code> -> <span class="warn">UB/HardFault</span>.<br><br><code>sizeof(arr) = 6</code>, <code>sizeof(p) = 4</code> (або 8). Масив у стеку, вказівник тільки зберігає адресу.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
