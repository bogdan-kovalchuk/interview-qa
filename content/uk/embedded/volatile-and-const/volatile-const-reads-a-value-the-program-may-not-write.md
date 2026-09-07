---
id: emb-volconst-0014
title: "Що таке `volatile const` і навіщо воно потрібне?"
description: "volatile const описує об'єкт, який програма не має права змінювати, але значення якого може змінитися без участі програми."
track: embedded
section: volatile-and-const
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 1
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

**`volatile const`** описує об'єкт, який програма не має права змінювати, але значення якого може змінитися без участі програми.

Типовий приклад: read-only status register. Firmware тільки читає; hardware оновлює біти стану. Без `volatile` компілятор може повторно використати старе значення, а без `const` програміст може випадково записати в read-only register.

Embedded-правило: для апаратних read-only регістрів використовуй pointer to `volatile const` data.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
