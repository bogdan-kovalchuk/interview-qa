---
id: emb-macros-0044
title: "Trap: що не так із `#define BIT(n) (1 << (n))` при `BIT(31)`?"
description: "Літерал 1 має тип int (signed), тому 1 << 31 зсуває біт у знаковий розряд -> undefined behavior для signed на 32-бітному int."
track: embedded
section: inline-and-macros
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 1
reconciled_with:
  en: 3
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання і відповіді; відповідь незалежно не перевірена."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
---

## Short answer

<span class="warn">Літерал `1` має тип `int`</span> (signed), тому `1 << 31` зсуває біт у знаковий розряд -> <span class="warn">undefined behavior</span> для signed на 32-бітному `int`.

На багатьох MCU «спрацює» як `0x80000000`, але стандарт цього не гарантує, і compiler може оптимізувати непередбачувано.

Захист: `#define BIT(n) (1u << (n))` або `(UINT32_C(1) << (n))` – unsigned-зсув визначений.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
