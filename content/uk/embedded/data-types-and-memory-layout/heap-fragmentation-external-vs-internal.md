---
id: emb-dtypes-0034
title: "Що таке heap fragmentation і чому це критично для embedded?"
description: "Heap fragmentation залишає вільну пам’ять розкиданою дрібними блоками; без MMU живі блоки не переміщуються, тож embedded-код часто обирає static allocation або memory pool."
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
  - source_id: freertos-heap
    title: "FreeRTOS heap_4 implementation"
    url: https://github.com/FreeRTOS/FreeRTOS-Kernel/blob/main/portable/MemMang/heap_4.c
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Показує злиття суміжних вільних блоків у heap_4; інші allocator-и можуть відрізнятися."
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

Heap fragmentation виникає після множинних `malloc`/`free`: вільної пам’яті сумарно може вистачати, але найбільший суміжний блок замалий для запиту, тож `malloc` може повернути `NULL`.

**Зовнішня**: багато малих вільних блоків. **Внутрішня**: виділений блок більший за запит (alignment/metadata).

Відсутність MMU не заважає allocator-у зливати суміжні вільні блоки: наприклад, FreeRTOS `heap_4` виконує таке coalescing. Однак переміщення живих об’єктів для compaction – окрема властивість allocator-а, а звичайні C-вказівники ускладнюють таке переміщення.[^freertos-heap]

## Detailed explanation

Heap fragmentation описує втрату можливості використати вільну пам’ять для конкретного запиту через її розподіл або накладні витрати. За external fragmentation вільні ділянки розділені зайнятими блоками. Наприклад, якщо allocator має три вільні блоки по 100 байтів, сума становить 300 байтів, але запит на 180 байтів може не пройти, коли потрібен один суміжний блок.

Internal fragmentation виникає всередині виділеного блоку: allocator округлює запит для alignment, додає metadata або видає блок певного класу розміру. Запит на 17 байтів може зайняти 24; різниця недоступна іншим запитам, доки блок зайнятий. Стратегії пошуку, розбиття та злиття залежать від allocator, тому загальна кількість вільних байтів сама собою не характеризує фрагментацію.

MMU не визначає, чи можна зливати сусідні вільні блоки. Звичайні C-вказівники прив’язані до адрес, тому переміщення живих об’єктів потребує спеціальної handle-based архітектури. Водночас allocator без MMU може зливати суміжні вільні блоки: FreeRTOS heap_4 робить це, обмежуючи fragmentation. Блоки, між якими залишаються зайняті об’єкти, все одно не зіллються.[^freertos-heap]

**Типова помилка:** вважати, що невдалий `malloc` доводить повне вичерпання heap. Перевіряйте найбільший доступний суміжний блок, статистику allocator і шаблон запитів. Для передбачуваної пам’яті підходять static allocation, пули фіксованих блоків або allocator із перевіреними затримками та правилами злиття. Наприклад, після звільнення кожного другого блока суміжні вільні ділянки лишаються розділеними зайнятими об’єктами; просте злиття сусідів не може їх об’єднати. Періодичність і розмір запитів важливі так само, як сума виділених байтів. Тестуйте довгі послідовності реальних allocate/free операцій.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
