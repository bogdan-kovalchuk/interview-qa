---
id: emb-cppfound-0036
title: "Як в пам'яті розміщується 2D масив <code>int arr[3][4]</code> (row-major)?"
description: "How C stores two-dimensional arrays in row-major order."
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

2D масив у C зберігається у <span class="key">row-major order</span>: рядки йдуть один за одним у неперервній пам'яті.<br><br><code>arr[0][0], arr[0][1], arr[0][2], arr[0][3],</code><br><code>arr[1][0], arr[1][1], arr[1][2], arr[1][3],</code><br><code>arr[2][0], arr[2][1], arr[2][2], arr[2][3]</code><br><br>Всього: 3×4×4 = 48 байт. Формула адреси: <code>&amp;arr[i][j] = arr + i*4 + j</code> (у елементах). Оптимальна ітерація: рядок за рядком (cache-friendly).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
