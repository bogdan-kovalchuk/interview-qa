---
id: emb-structs-0047
title: "Trap: що не так із `#pragma pack` у public header без обережності?"
description: "Він може змінити packing для наступних структур у чужому коді."
track: embedded
section: structs-unions-and-bitfields
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

<span class="warn">Він може змінити packing для наступних структур у чужому коді.</span>

Якщо header вмикає packing і не відновлює попередній стан, він ламає layout unrelated structs, ABI і alignment. Це особливо неприємно в embedded, де один header може вплинути на driver structs або RTOS control blocks.

Захист: використовуй push/pop pragmas або локальні attributes, мінімізуй scope packing і перевіряй layout static assertions.[^embeddedinterviewlab]

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
