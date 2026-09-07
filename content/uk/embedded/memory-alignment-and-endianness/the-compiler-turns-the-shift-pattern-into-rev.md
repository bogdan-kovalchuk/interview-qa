---
id: emb-align-0019
title: "Чому ручні byte-swap функції – нормальний вибір на ARM?"
description: "Компілятор розпізнає shift/mask патерн і генерує одну інструкцію REV/REV16."
track: embedded
section: memory-alignment-and-endianness
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

**Компілятор розпізнає shift/mask патерн і генерує одну інструкцію `REV`/`REV16`.**

Тобто читабельний портативний C компілюється так само ефективно, як inline assembly, але працює на будь-якому toolchain і легше супроводжується.

Правило: спершу пиши зрозумілий C; до intrinsics/asm вдавайся, лише якщо профіль показав потребу.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
