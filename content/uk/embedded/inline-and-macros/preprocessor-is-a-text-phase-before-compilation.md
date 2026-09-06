---
id: emb-macros-0001
title: "Що таке препроцесор C і коли він виконує свою роботу?"
description: "Препроцесор – це текстова фаза, яка виконується до компіляції і обробляє директиви #include, #define, #if."
track: embedded
section: inline-and-macros
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

**Препроцесор** – це текстова фаза, яка виконується до компіляції і обробляє директиви `#include`, `#define`, `#if`.

Він робить лише text substitution: не знає типів, scope, синтаксису C чи C++. Тому помилка у макросі проявляється вже після розгортання, у згенерованому коді, а не у місці `#define`.

Правило: щоб побачити реальний результат розгортання, дивись output `gcc -E file.c`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
