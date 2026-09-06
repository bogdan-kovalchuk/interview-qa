---
id: emb-volconst-0053
title: "Чому запис `volatile uint32_t counter; counter++;` не безпечний для ISR-shared counter?"
description: "counter++ є read-modify-write, а не атомарна операція."
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

`counter++` є read-modify-write, а не атомарна операція.

Компілятор виконає volatile read, додасть 1 у регістрі CPU, потім volatile write. Якщо ISR теж змінює `counter` між read і write, одне оновлення може загубитися. `volatile` лише гарантує, що read і write не будуть прибрані.

Захист: оновлюй shared counter у critical section або використовуй atomic operation, якщо платформа й toolchain її підтримують.[^embeddedinterviewlab]

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
