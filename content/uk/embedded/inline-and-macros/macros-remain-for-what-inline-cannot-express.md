---
id: emb-macros-0023
title: "Для чого макроси досі незамінні навіть у MISRA-проєкті?"
description: "Там, де static inline не може замінити препроцесор: • Адреси регістрів з volatile-cast; • утиліти, які не бувають функціями: ARRAY_SIZE, UNUSED, STATIC_ASSERT; • Conditional compilation (#ifdef, #if defined); • X-macros і code generation; •"
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

Там, де `static inline` не може замінити препроцесор:

• Адреси регістрів з `volatile`-cast; • утиліти, які не бувають функціями: `ARRAY_SIZE`, `UNUSED`, `STATIC_ASSERT`; • Conditional compilation (`#ifdef`, `#if defined`); • X-macros і code generation; • стрінгіфікація (`#`) і склеювання токенів (`##`).

Правило: макрос – для текстових/compile-time трюків; `static inline` – для всього, що поводиться як функція.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
