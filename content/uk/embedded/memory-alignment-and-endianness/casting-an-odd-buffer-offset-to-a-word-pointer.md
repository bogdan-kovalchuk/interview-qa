---
id: emb-align-0031
title: "Trap: чому `*(uint32_t*)&buf[1]` небезпечно?"
description: "Адреса &buf[1] не кратна 4 -> misaligned access (HardFault на M0, штраф на M3/M4), плюс потенційне порушення strict aliasing."
track: embedded
section: memory-alignment-and-endianness
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
uint32_t v = *(uint32_t*)&buf[1];
```

## Short answer

<span class="warn">Адреса `&buf[1]` не кратна 4 -> misaligned access</span> (HardFault на M0, штраф на M3/M4), плюс потенційне порушення strict aliasing.

Cast `uint8_t*` -> `uint32_t*` обіцяє компілятору вирівнювання, якого немає.

Захист: `uint32_t v; memcpy(&v, &buf[1], 4);` – безпечно для будь-якого зсуву і без UB.[^embeddedinterviewlab]

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
