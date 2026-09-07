---
id: emb-volconst-0050
title: "Trap: чи можна передати `const uint8_t *` у функцію, яка очікує `uint8_t *`?"
description: "Без cast не можна; з cast можна приховати помилку дизайну."
track: embedded
section: volatile-and-const
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

<span class="warn">Без cast не можна; з cast можна приховати помилку дизайну.</span>

Функція з параметром `uint8_t *` має право писати у buffer, тож передача `const uint8_t *` порушує цей контракт. Якщо buffer лежить у Flash/`.rodata`, випадковий запис може закінчитися fault-ом або undefined behavior.

Захист: розділяй API: input buffer як `const uint8_t *`, output buffer як `uint8_t *`. Не прибирай qualifiers cast-ом для зручності.[^embeddedinterviewlab]

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
