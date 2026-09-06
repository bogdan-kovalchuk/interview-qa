---
id: emb-volconst-0057
title: "Trap: чи однакові `const volatile uint32_t *` і `volatile const uint32_t *`?"
description: "Так, для pointed-to base type порядок const і volatile не змінює значення."
track: embedded
section: volatile-and-const
level: junior
type: pitfall
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

**Так, для pointed-to base type порядок `const` і `volatile` не змінює значення.**

Обидва типи означають pointer to const volatile `uint32_t`. Дані за pointer не можна записувати через цей lvalue, але читання має бути volatile. Важливо не плутати це з `const volatile uint32_t * const`, де додатковий `const` після `*` захищає сам pointer.

Правило: порядок cv-qualifiers біля одного рівня типу не головне; головне, до якого рівня pointer chain вони застосовані.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
