---
id: emb-align-0013
title: "Trap: чому не можна казати «endianness не важлива на ARM, бо там завжди little-endian»?"
description: "ARM bi-endian, і навіть LE (little-endian) система постійно працює з big-endian даними."
track: embedded
section: memory-alignment-and-endianness
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

<span class="warn">ARM bi-endian, і навіть LE (little-endian) система постійно працює з big-endian даними.</span>

Cortex-M за замовчуванням little-endian, але архітектура підтримує і big-endian режим. Головне – мережеві й польові протоколи (TCP/IP – Transmission Control Protocol/Internet Protocol, CAN – Controller Area Network, Modbus TCP) – big-endian, тож конвертація потрібна завжди.

Захист: на інтерв'ю говори про byte order явно і використовуй `htonl`/`ntohl`, а не «припущення про платформу».[^embeddedinterviewlab]

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
