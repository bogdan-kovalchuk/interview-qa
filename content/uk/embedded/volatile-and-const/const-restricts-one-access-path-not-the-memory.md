---
id: emb-volconst-0049
title: "Чому `const` не є \"гарантією фізичної незмінності\" об'єкта?"
description: "const обмежує записи через конкретний typed access, але не доводить, що фізична пам'ять ніколи не зміниться."
track: embedded
section: volatile-and-const
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

**`const` обмежує записи через конкретний typed access, але не доводить, що фізична пам'ять ніколи не зміниться.**

Об'єкт може бути mutable, але переданий у функцію як `const T *`, щоб ця функція його не змінювала. А `volatile const` прямо описує випадок, де firmware не пише, але hardware може змінювати значення.

Правило: `const` це контракт доступу в типах C; physical immutability залежить від storage, MPU, Flash контролера та hardware.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
