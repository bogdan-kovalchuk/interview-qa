---
id: emb-macros-0021
title: "Що таке X-macro і яку проблему він вирішує?"
description: "X-macro – це список, визначений один раз, який розгортають у різних контекстах."
track: embedded
section: inline-and-macros
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

**X-macro – це список, визначений один раз, який розгортають у різних контекстах**.

Класична задача: тримати синхронними `enum` і таблицю рядків/обробників. Список елементів описують через макрос `X(...)`, а потім по-різному визначають `X`, щоб згенерувати enum, масив імен, switch тощо.

Правило: додавання нового елемента в один список автоматично оновлює всі згенеровані сутності – <span class="warn">неможливо забути</span> оновити пару.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
