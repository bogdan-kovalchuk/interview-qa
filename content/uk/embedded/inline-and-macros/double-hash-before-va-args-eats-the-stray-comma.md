---
id: emb-macros-0018
title: "Що означає `##` перед `__VA_ARGS__` у variadic-макросі?"
description: "##__VA_ARGS__ прибирає зайву кому, коли variadic-аргументів немає."
track: embedded
section: inline-and-macros
level: junior
type: mechanism
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

## Question code

```c
#define DBG(fmt, ...) printf(fmt, ##__VA_ARGS__)
```

## Short answer

**`##__VA_ARGS__` прибирає зайву кому**, коли variadic-аргументів немає.

Без `##` виклик `DBG("hi")` розгорнувся б у `printf("hi", )` – <span class="warn">синтаксична помилка</span> через висячу кому. З `##` кома зникає -> `printf("hi")`.

Правило: `##__VA_ARGS__` – GNU-розширення (GCC/Clang); у C23/C++20 портативний аналог – `__VA_OPT__(,)`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
