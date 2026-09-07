---
id: emb-cppfound-0059
title: "Чи можна порівнювати вказівники (`<`, `>`) і коли це визначена поведінка?"
description: "When relational pointer comparisons are defined."
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

Порівняння `==` та `!=` – завжди **визначено** між будь-якими двома вказівниками одного типу.

Порівняння `<`, `>`, `<=`, `>=` – **визначено лише** якщо обидва вказівники вказують на **один і той самий масив** (або структуру). Порівняння вказівників різних об'єктів -> <span class="warn">UB за стандартом</span>.

Практика: більшість платформ дають коректну відповідь навіть для різних об'єктів, але не покладайся на це у portable коді.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
