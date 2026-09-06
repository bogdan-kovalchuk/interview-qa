---
id: emb-structs-0040
title: "Trap: чому `memcmp(&a, &b, sizeof a)` поганий спосіб порівняти структури?"
description: "Бо padding bytes можуть відрізнятися, навіть якщо всі поля рівні."
track: embedded
section: structs-unions-and-bitfields
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

Бо padding bytes можуть відрізнятися, навіть якщо всі поля рівні.

Padding не є логічною частиною стану структури. Він може містити старі stack bytes або різні значення після різних шляхів ініціалізації. `memcmp` порівнює raw bytes, тому може повернути "не рівні" для структур з однаковими member values.

Захист: порівнюй поля явно або нормалізуй serialization format. Для security-sensitive output не витікай padding bytes назовні.[^embeddedinterviewlab]

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
