---
id: emb-structs-0018
title: "Чому `union` часто додають тегом-дискримінатором?"
description: "Бо сам union не пам'ятає, який member зараз активний або логічно валідний."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: concept
tags: []
status: published
updated: 2026-09-06
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

**Бо сам union не пам'ятає, який member зараз активний або логічно валідний.**

Типовий патерн: `enum kind` поруч із `union payload`. Без discriminator код може прочитати temperature payload як pressure payload або interpret pointer як integer. Це логічна помилка навіть там, де binary access формально можливий.

Правило: для variant data структура має містити tag + union, а всі switch-и по tag мають обробляти всі варіанти.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
