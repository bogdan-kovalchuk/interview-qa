---
id: emb-align-0024
title: "Trap: реальний баг «кожен другий сенсор». Що сталося?"
description: "M4-gateway (LE – little-endian) і PowerPC-нода (BE – big-endian) обмінювалися сирими memcpy структурами."
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

## Short answer

<span class="warn">M4-gateway (LE – little-endian) і PowerPC-нода (BE – big-endian) обмінювалися сирими `memcpy` структурами.</span>

Поле `uint8_t sensor_id` мало різний padding (3B на M4, 1B на PowerPC), що зсувало наступний `uint32_t` на 2 байти. Непарні id «випадково» працювали, парні давали сміття (~14000°C).

Захист: явний wire-формат + серіалізація поле за полем з `htonl`/`htons`. Ніколи не вважай, що два компілятори дадуть однаковий layout.[^embeddedinterviewlab]

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
