---
id: emb-align-0041
title: "Trap: чому однаковий `struct` у вихідному коді може мати різний бінарний layout?"
description: "Padding і alignment залежать від компілятора, архітектури та опцій збірки."
track: embedded
section: memory-alignment-and-endianness
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

Padding і alignment залежать від компілятора, архітектури та опцій збірки.

Той самий код на M4 і PowerPC дасть різні зсуви полів, а протилежна endianness ще й перевертає байти. Тому «однаковий .h файл» ≠ «однаковий байтовий формат».

Захист: ніколи не вважай два компілятори сумісними по layout; визначай явний wire-формат і серіалізуй поле за полем.[^embeddedinterviewlab]

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
