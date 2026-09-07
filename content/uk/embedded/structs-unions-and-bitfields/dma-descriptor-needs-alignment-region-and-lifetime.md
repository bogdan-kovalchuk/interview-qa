---
id: emb-structs-0043
title: "Trap: чому DMA descriptor struct не можна просто довільно розмістити на stack?"
description: "DMA може вимагати конкретне alignment, memory region і lifetime довший за stack frame."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
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

<span class="warn">DMA може вимагати конкретне alignment, memory region і lifetime довший за stack frame.</span>

Stack object може зникнути після повернення функції, бути невирівняним для DMA engine або лежати в cacheable RAM без clean/invalidate. Структура descriptor-а також має мати layout, який точно збігається з hardware manual.

Захист: DMA descriptors зазвичай роблять `static`, aligned, у правильній linker section, з explicit barriers/cache maintenance.[^embeddedinterviewlab]

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
