---
id: emb-volconst-0012
title: "Що означає `volatile uint32_t * const reg`?"
description: "reg є const pointer to volatile uint32_t."
track: embedded
section: volatile-and-const
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

**`reg` є const pointer to volatile `uint32_t`**.

Адресу вказівника змінити не можна: `reg = other` буде помилкою компіляції. Але дані за цією адресою volatile: кожне `*reg` читається або записується реально. Це канонічний тип для фіксованого writable hardware register.

Embedded-use case: адреса GPIO output register стала, а вміст регістра може змінюватися апаратурою або записами firmware.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
