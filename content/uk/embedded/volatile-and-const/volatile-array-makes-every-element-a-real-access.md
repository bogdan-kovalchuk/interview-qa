---
id: emb-volconst-0058
title: "Що означає `volatile uint8_t rx_buf[64]` для DMA receive buffer?"
description: "Кожен елемент масиву має volatile-qualified type, тому читання rx_buf[i] має бути реальним memory access."
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

**Елементи `volatile uint8_t rx_buf[64]` мають volatile-qualified type**, тож їхні доступи враховуються за правилами конкретної реалізації C.

Це може бути потрібно, якщо DMA змінює bytes поза control flow CPU. Але це не вирішує cache coherency, не гарантує, що DMA вже завершив запис, і не робить multi-byte parsing атомарним.

Правило: volatile buffer може бути частиною DMA protocol, але потрібні completion flags, barriers/cache maintenance і ownership discipline.[^iso-c-n1570]

## Detailed explanation

`volatile uint8_t rx_buf[64]` оголошує масив із 64 елементів типу `volatile uint8_t`: qualifier належить типу елементів, тому `rx_buf[i]` має volatile-qualified type. Стандарт C вимагає зберігати observable behaviour volatile accesses за правилами реалізації, але визначення такого доступу лишається implementation-defined; volatile не означає універсальний машинний load певної ширини.[^iso-c-n1570]

Це може бути доречним у платформному DMA API, коли пристрій змінює буфер поза control flow CPU. Однак DMA не є потоком виконання C, тому стандарт мови не визначає синхронізацію CPU з DMA. З’ясуй контракт MCU і драйвера: як повідомляється completion, чи потрібна cache invalidation, і як передаються права на буфер.[^iso-c-n1570]

На MCU з data cache DMA може записати RAM, тоді як CPU читає стару cache line. `volatile` саме по собі не інвалідує cache, не створює memory barrier для сусідніх non-volatile даних і не робить багатобайтове читання атомарним. Такі гарантії надають platform-specific cache maintenance, DMA API та synchronization primitives.[^iso-c-n1570]

Приклад: після заповнення буфера драйвер має підтвердити завершення transfer і виконати потрібну cache maintenance операцію, а вже тоді parser читає байти. Якщо DMA ще працює, читання може побачити суміш старих і нових байтів; довжина даних має надходити з окремого протоколу завершення.[^iso-c-n1570]

**Типова помилка:** вважати volatile альтернативою DMA API. Окремо реалізуй ownership, completion notification та cache coherency.

## Sources

<!-- generated from frontmatter -->
