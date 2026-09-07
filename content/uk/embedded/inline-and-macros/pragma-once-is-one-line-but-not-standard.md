---
id: emb-macros-0016
title: "Чим `#pragma once` відрізняється від класичного include guard?"
description: "#pragma once дає той самий захист одним рядком на початку файлу, без ризику зіткнення імен макросів-guard."
track: embedded
section: inline-and-macros
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
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

**`#pragma once` дає той самий захист одним рядком** на початку файлу, без ризику зіткнення імен макросів-guard.

Мінус: він <span class="warn">не входить до стандарту C/C++</span>, хоча підтримується GCC, Clang, MSVC, IAR. Класичний `#ifndef`-guard портативніший і працює навіть з дивними файловими системами та symlink-ами.

Правило: для максимальної портативності – `#ifndef`-guard; для зручності у відомому toolchain – `#pragma once` прийнятний.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
