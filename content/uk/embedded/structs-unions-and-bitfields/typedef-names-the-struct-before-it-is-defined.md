---
id: emb-structs-0050
title: "Що означає `typedef struct Foo Foo;`?"
description: "Це створює typedef-ім'я Foo для типу struct Foo, часто ще до повного визначення структури."
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

**Це створює typedef-ім'я `Foo` для типу `struct Foo`**, часто ще до повного визначення структури.

Якщо тіло структури не задане, `Foo` є incomplete type. Можна використовувати `Foo *` у API, але не можна створювати `Foo object` by value до повного визначення.

Embedded-use case: opaque handles для драйверів: `Foo_Init(Foo *self)` або `Foo *Foo_Open(...)`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
