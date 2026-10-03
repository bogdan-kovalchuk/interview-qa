---
id: emb-volconst-0013
title: "Що означає `volatile const uint32_t * const STATUS`?"
description: "STATUS є const pointer to volatile const uint32_t."
track: embedded
section: volatile-and-const
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 2
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
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
---

## Short answer

**`STATUS` є const pointer to volatile const `uint32_t`**.

Адреса pointer не змінюється. Через цей тип не можна записати дані за адресою, а volatile-кваліфікатор застосовується до читань; конкретні правила такого доступу визначає реалізація C. Це типовий тип для read-only status register, якщо таку модель визначає документація MCU.[^iso-c-n1570]

Правило: `const` забороняє змінювати об’єкт через цей lvalue, а `volatile` позначає об’єкт, який може змінюватися невідомими для реалізації способами.[^iso-c-n1570]

## Detailed explanation

`volatile const uint32_t * const STATUS` містить два рівні `const`/`volatile`. Кваліфікатор після першого `*` фіксує сам вказівник `STATUS`. Кваліфікатори перед `*` описують цільовий об’єкт: через цей тип його не можна модифікувати, а volatile-властивість указує, що об’єкт може змінюватися способами, не видимими компілятору. У C `const` і `volatile` не скасовують одне одного – вони накладають окремі обмеження на тип.[^iso-c-n1570]

Таку комбінацію часто використовують для status register: програма лише читає стан, тоді як периферія може оновлювати біти. `const` забороняє запис через `STATUS`, а `volatile` вказує, що читання не слід трактувати як звичайне значення, яке гарантовано лишається незмінним. Формулювання стандарту обмежене: реалізація визначає, що вважається volatile access, тому потрібна сумісність із компілятором і memory map конкретного пристрою.[^iso-c-n1570]

Важливо відрізняти заборону запису через вказівник від фізичної незмінності об’єкта. `const` у типі не означає, що апаратура не може оновити регістр, і не є механізмом захисту пам’яті. Це обмеження для коду C, який користується саме таким lvalue. Аналогічно, `volatile` не означає, що кожне читання атомарне або що воно синхронізує різні ядра чи DMA; це окрема властивість доступу, описана реалізацією.[^iso-c-n1570]

Приклад абстрактної декларації для адреси статусного регістра:

```c
volatile const uint32_t * const status =
    (volatile const uint32_t *)STATUS_ADDRESS;
uint32_t bits = *status;  // читання дозволене
```

Присвоєння нового pointer значення змінній `status` заборонене через const на самому pointer. Присвоєння на кшталт `*status = 0` також заборонене, але з іншої причини: цільовий тип const-qualified. Не роби висновку про права запису лише з назви регістра – звір його властивості з reference manual, а тип оголошуй за контрактом апаратури та правилами тулчейна.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->
