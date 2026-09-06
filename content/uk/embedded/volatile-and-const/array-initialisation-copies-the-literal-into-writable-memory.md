---
id: emb-volconst-0031
title: "Чим відрізняються `const char *p = \"OK\"` і `char p[] = \"OK\"`?"
description: "const char p вказує на read-only string literal, а char p[] створює mutable array з копією символів."
track: embedded
section: volatile-and-const
level: junior
type: mechanism
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

**`const char *p` вказує на read-only string literal, а `char p[]` створює mutable array з копією символів.**

У першому випадку `p[0] = 'N'` заборонено типом. У другому випадку масив містить `'O'`, `'K'`, `'\0'` у власному storage, і `p[0] = 'N'` дозволено.

Embedded-наслідок: literal може жити у Flash, а mutable array зазвичай потребує RAM.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
