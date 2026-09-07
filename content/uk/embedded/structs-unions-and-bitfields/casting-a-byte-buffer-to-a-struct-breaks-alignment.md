---
id: emb-structs-0045
title: "Trap: чому overlay структури на raw buffer може порушити alignment?"
description: "buf має alignment для uint8_t, не обов'язково для struct Header."
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

## Question code

```c
uint8_t buf[8];
struct Header *h = (struct Header *)buf;
```

## Short answer

<span class="warn">`buf` має alignment для `uint8_t`, не обов'язково для `struct Header`.</span>

Якщо `Header` містить `uint32_t`, pointer `h` може бути невирівняним. Розіменування такого pointer може бути undefined behavior або fault. Крім того, strict aliasing і effective type rules теж можуть бути проблемою.

Захист: парсь bytes явно або копіюй у вирівняний local `struct Header h; memcpy(&h, buf, sizeof h);`, якщо binary layout контрольований.[^embeddedinterviewlab]

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
