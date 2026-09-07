---
id: emb-macros-0040
title: "Trap: чому це не function-like макрос?"
description: "Пробіл між F і (x) робить його object-like макросом."
track: embedded
section: inline-and-macros
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
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

```c
#define F (x) (x) * (x)
int r = F(3);
```

<span class="warn">Пробіл між `F` і `(x)` робить його object-like макросом.</span>

Препроцесор бачить ім'я `F`, що замінюється на весь текст `(x) (x) * (x)`. Тоді `F(3)` розгорнеться у `(x) (x) * (x)(3)` – використовується невизначений `x`, очевидна помилка.

Захист: у function-like макросі дужка `(` має йти одразу за ім'ям, без пробілу: `#define F(x) ((x) * (x))`.[^embeddedinterviewlab]

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
