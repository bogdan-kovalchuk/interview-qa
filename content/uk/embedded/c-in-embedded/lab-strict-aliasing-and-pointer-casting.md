---
id: emb-cppfound-0077
title: "Що таке strict aliasing rule і як він стосується pointer casting?"
description: "How strict aliasing constrains accesses through incompatible pointer types."
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

**Strict aliasing rule** (C99 §6.5): компілятор може вважати що вказівники різних несумісних типів НЕ alias-ують (не вказують на одну область пам'яті).

Дозволяє агресивну оптимізацію: якщо змінили через `float*` – компілятор не зобов'язаний перечитати через `int*`.

Виключення: `char*` та `unsigned char*` можуть alias-увати будь-що.

Порушення: `int x; float *fp=(float*)&x; *fp=1.0f;` -> UB. Захист: `memcpy` або `union` (у C).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
