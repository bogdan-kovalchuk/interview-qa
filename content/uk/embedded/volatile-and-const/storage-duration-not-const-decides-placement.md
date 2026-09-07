---
id: emb-volconst-0027
title: "Trap: чи завжди локальний `const` масив автоматично лежить у Flash?"
description: "Ні, не завжди. const забороняє запис через цей identifier, але storage placement залежить від storage duration, ABI, оптимізації та linker script."
track: embedded
section: volatile-and-const
level: junior
type: pitfall
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

<span class="warn">Ні, не завжди.</span>

`const` забороняє запис через цей identifier, але storage placement залежить від storage duration, ABI, оптимізації та linker script. Локальний automatic `const` object може бути на stack або оптимізований у immediate constants. File-scope або `static const` значно частіше потрапляє в `.rodata`.

Захист: для великих embedded LUT використовуй `static const` або file-scope `const` і перевіряй map file.[^embeddedinterviewlab]

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
