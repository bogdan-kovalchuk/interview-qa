---
id: emb-macros-0048
title: "Чим відрізняється семантика `inline` у C і C++?"
description: "У C++ inline-функція може мати визначення в кількох translation units (TU) через header без порушення ODR (One Definition Rule) – лінкер зливає копії; це штатний спосіб класти функції в header."
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

У C++ `inline`-функція може мати визначення в кількох translation units (TU) через header без порушення ODR (One Definition Rule) – лінкер зливає копії; це штатний спосіб класти функції в header.

У C (C99+) правила складніші: чистий `inline` дає лише inline-визначення без external symbol, тому потрібен `extern` у одному TU або, простіше, `static inline`.

Правило: у C для header-функцій майже завжди пиши `static inline`; у C++ достатньо `inline`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
