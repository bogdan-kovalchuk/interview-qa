---
id: emb-patterns-0034
title: "Trap: чому `reg |= (value << SHIFT)` без clear маски – баг?"
description: "OR лише виставляє біти, але не скидає старі – якщо поле вже мало значення, нове «накладеться» поверх."
track: embedded
section: common-code-patterns
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

<span class="warn">OR лише виставляє біти, але не скидає старі</span> – якщо поле вже мало значення, нове «накладеться» поверх.

Наприклад, старе поле `0b110`, пишемо `0b001` через `|=` -> отримаємо `0b111`, а не `0b001`.

Захист: спершу `reg &= ~MASK;`, потім `reg |= (value << SHIFT) & MASK;` – повний read-modify-write.[^embeddedinterviewlab]

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
