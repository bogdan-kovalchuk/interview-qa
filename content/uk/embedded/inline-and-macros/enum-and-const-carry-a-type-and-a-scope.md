---
id: emb-macros-0030
title: "Чому для іменованих констант у C часто кращі `enum`/`const`, ніж `#define`?"
description: "enum і const мають тип і scope, видимі дебагеру, тоді як #define – безтипова текстова заміна без області видимості."
track: embedded
section: inline-and-macros
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

**`enum` і `const` мають тип і scope, видимі дебагеру**, тоді як `#define` – безтипова текстова заміна без області видимості.

`enum { MAX_CH = 8 };` дає compile-time integer-константу з ім'ям у debug info і не засмічує global namespace. `const` теж типобезпечний, але у C займає пам'ять і не є integer constant expression для розміру масиву.

Правило: цілочисельні compile-time константи -> `enum`; типізовані -> `const`; `#define` – коли потрібен саме препроцесор.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
