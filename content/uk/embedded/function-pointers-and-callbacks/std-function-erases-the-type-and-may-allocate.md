---
id: emb-fnptr-0042
title: "Чому `std::function` не завжди підходить для embedded callback API?"
description: "std::function зручний, але може мати overhead і потенційні allocation-и."
track: embedded
section: function-pointers-and-callbacks
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

**`std::function` зручний, але може мати overhead і потенційні allocation-и.**

Він стирає тип callable і може зберігати lambdas/functors, але це збільшує code size, може тягнути exceptions/RTTI залежно від toolchain і іноді використовує heap, якщо callable не вміщається в small buffer optimization.

Embedded-правило: у low-level drivers частіше використовують `function pointer + void *ctx`; у application layer `std::function` можливий, якщо політика проекту дозволяє.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
