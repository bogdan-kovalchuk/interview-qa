---
id: emb-dtypes-0095
title: "Яке значення матиме? `int x = (int)(3.7);`"
description: "Перетворення double в int відкидає дробову частину до нуля, тому 3.7 стає 3, а не округлюється."
track: embedded
section: data-types-and-memory-layout
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
    applicability: "Джерело питання і відповіді; відповідь не перевірена незалежно."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? data-types-and-memory-layout; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

`x = 3`.

Перетворення `double -> int` у C відбувається через **truncation** (відкидання дробової частини, НЕ округлення): `3.7 -> 3`, `-3.7 -> -3` (до нуля).

Для округлення: `round(3.7) = 4`, `floor(3.7) = 3`, `ceil(3.7) = 4`.

Важливо у DSP та control systems: `int duty = (int)(percentage * 100.0f);` може давати систематичну похибку через truncation.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
