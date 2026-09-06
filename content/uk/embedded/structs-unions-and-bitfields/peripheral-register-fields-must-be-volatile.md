---
id: emb-structs-0010
title: "Чому поля peripheral register struct мають бути `volatile`?"
description: "Бо кожне поле представляє hardware register, значення якого може змінитися поза C-кодом або мати side effects при читанні/записі."
track: embedded
section: structs-unions-and-bitfields
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

**Бо кожне поле представляє hardware register, значення якого може змінитися поза C-кодом або мати side effects при читанні/записі.**

Без `volatile` компілятор може кешувати status bit, прибрати читання read-to-clear register або об'єднати записи. Для Cortex-M це типова причина багів, які видно лише в release build.

Правило: register overlay має мати volatile-qualified fields або доступ через pointer to volatile register type.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
