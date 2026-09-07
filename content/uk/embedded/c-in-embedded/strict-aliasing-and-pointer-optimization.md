---
id: emb-cppfound-0054
title: "Що таке pointer aliasing і як він впливає на оптимізацію?"
description: "How strict aliasing affects pointer-based optimization."
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

**Pointer aliasing** – ситуація коли два вказівники різних типів вказують на одну область пам'яті.

Strict aliasing rule (C99 §6.5): компілятор може вважати, що вказівники різних типів не alias-ують (окрім `char*`/`unsigned char*`). Це дозволяє більш агресивну оптимізацію.

Порушення: `int x; float *fp = (float*)&x; *fp = 1.0f;` -> UB.

Захист: `memcpy` для type punning, `char*` для byte access, `restrict` для явної гарантії no-aliasing.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
