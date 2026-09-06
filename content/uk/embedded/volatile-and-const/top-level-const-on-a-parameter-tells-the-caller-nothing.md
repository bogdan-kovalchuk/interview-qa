---
id: emb-volconst-0041
title: "Чому `void f(uint8_t * const p)` не дуже корисне як API-контракт?"
description: "Бо const тут top-level і стосується лише локальної копії pointer parameter всередині функції."
track: embedded
section: volatile-and-const
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

**Бо `const` тут top-level і стосується лише локальної копії pointer parameter всередині функції.**

Caller не бачить різниці: pointer value і так передається by value. Функція не може змінити pointer у caller-а незалежно від `const`. Але вона все ще може змінювати `p[0]`, бо pointed-to data не const.

Правило: якщо хочеш пообіцяти, що buffer не буде змінено, пиши `void f(const uint8_t *p)`, а не `uint8_t * const p`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
