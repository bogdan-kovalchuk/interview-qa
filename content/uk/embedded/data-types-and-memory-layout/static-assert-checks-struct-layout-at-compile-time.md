---
id: emb-dtypes-0099
title: "Навіщо потрібен `static_assert` при роботі зі структурами у embedded?"
description: "static_assert перевіряє sizeof і offsetof структур при компіляції, гарантуючи відповідність протоколу."
track: embedded
section: data-types-and-memory-layout
level: middle
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  en: 3
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; це джерело не є доказом тверджень."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу data-types-and-memory-layout; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

`static_assert` (у C11 `_Static_assert`, у C++ `static_assert`) перевіряє constant expression під час компіляції та спричиняє діагностику, якщо умова хибна.[^iso-c-n1570]

Для embedded: `static_assert(sizeof(CanFrame) == 13, "Wrong CAN frame size");`
`static_assert(offsetof(UartPacket, crc) == 6, "CRC offset mismatch");`

Такі перевірки фіксують очікуваний розмір і зсуви для конкретної збірки, але не гарантують однаковий layout для інших ABI чи відповідність усьому протоколу.

Для бінарного формату перевіряй потрібні `sizeof` і `offsetof`, а переносне кодування полів визначай окремо.[^iso-c-n1570]

## Detailed explanation

`static_assert` (у C11 це `_Static_assert`) перевіряє constant expression під час трансляції й робить програму некоректною, якщо умова хибна.[^iso-c-n1570] Для структур це зручно, щоб зафіксувати очікування щодо `sizeof` або `offsetof` і зупинити збірку, коли зміна типу чи ABI порушила це очікування.

Компілятор може вставляти padding між полями та в кінці структури для вирівнювання. Тому сума розмірів полів не обов’язково дорівнює `sizeof` структури, а позиція поля може різнитися між ABI, архітектурами та параметрами компілятора. Наприклад, перевірка `offsetof(Packet, crc) == 6` фіксує конкретний контракт для цільової збірки; вона не доводить, що такий самий layout існує на кожній платформі.

Для C структур із bit-fields мають додаткові обмеження: `offsetof` не можна переносно застосувати до bit-field, а порядок і розміщення bit-fields залежать від реалізації. У C++ `offsetof` визначений для standard-layout класів; інші випадки не є переносним способом перевірки двійкового формату. Якщо wire protocol має фіксоване кодування, явна серіалізація байтів часто надійніша за передачу сирого представлення структури.

Такі перевірки корисні для register map або ABI, але їх слід прив’язати до правильного target і документованого формату. Перевірка розміру не доводить endian order, не прибирає padding і не гарантує відповідність вимогам протоколу. Для layout із явними полями додай перевірки потрібних offsets; для форматів на дроті перевіряй також кодування кожного поля.

**Типова помилка:** вважати, що успішний `static_assert(sizeof(T) == N)` гарантує повністю portable бінарний формат. Це лише перевірка однієї властивості в поточній компіляції; точну переносність забезпечує визначений протоколом encode/decode, а не випадковий layout компілятора.[^iso-c-n1570]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
