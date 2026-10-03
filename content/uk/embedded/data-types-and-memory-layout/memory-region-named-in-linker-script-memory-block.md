---
id: emb-dtypes-0097
title: "Що таке memory region і як він задається у linker script?"
description: "Memory region - іменована ділянка адресного простору, задана атрибутами і межами у блоці MEMORY."
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
  - source_id: gnu-ld-memory
    title: 'GNU ld documentation: MEMORY command'
    url: https://sourceware.org/binutils/docs/ld/MEMORY.html
    accessed: 2026-10-04
    kind: official
    version: current
    applicability: 'Синтаксис MEMORY, атрибути регіонів і використання GNU ld для розміщення секцій; інші linker можуть мати інший синтаксис.'
---

## Short answer

**Memory region** – іменована ділянка адресного простору. Задається у блоці `MEMORY` linker script:

`MEMORY {
  FLASH (rx)   : ORIGIN = 0x08000000, LENGTH = 512K
  RAM   (rwx)  : ORIGIN = 0x20000000, LENGTH = 128K
  CCMRAM (rwx) : ORIGIN = 0x10000000, LENGTH = 64K
}`

Атрибути: `r` – read, `w` – write, `x` – execute. Секції прив’язуються через `> REGION` у блоці `SECTIONS`.[^gnu-ld-memory]

## Detailed explanation

Memory region у GNU linker script описує діапазон адрес, доступний компонувальнику, його довжину та атрибути пам’яті.[^gnu-ld-memory] Це декларація для компонування, а не виділення RAM під час виконання й не налаштування контролера пам’яті.

У блоці `MEMORY` задають ім’я, атрибути, початкову адресу та довжину кожної області. Наприклад, `FLASH` може починатися з адреси `0x08000000`, а `RAM` з `0x20000000`; ці числа є прикладом конкретної мапи MCU, а не універсальними адресами. Атрибути `r`, `w`, `x` описують придатність області для читання, запису й виконання та допомагають linker підібрати розміщення для секцій, яким не задано явного регіону.[^gnu-ld-memory]

У `SECTIONS` програміст пов’язує output section з названою областю, наприклад `.text > FLASH` і `.data > RAM AT > FLASH`. Так `.data` матиме адресу виконання в RAM, а її початкові байти зберігатимуться у Flash для копіювання під час старту. Сам linker не виконує це копіювання: startup code має реалізувати його, якщо така схема потрібна. `NOLOAD` та інші конструкції також впливають на те, як секція потрапляє в образ.

Linker перевіряє, чи поміщаються розміщені секції в задані діапазони; помилка переповнення часто виявляє завелику прошивку або неправильні довжини. Але коректний linker script не доводить, що фізична адреса відповідає конкретній мікросхемі, що RAM доступна певному ядру або що MPU налаштований відповідно. Ці властивості треба звіряти з datasheet/reference manual і конфігурацією запуску.

**Типова помилка:** вважати назву `RAM` магічною або задавати довжину всього адресного простору замість фактично доступної пам’яті. Перевіряй мапу пам’яті пристрою та linker map-файл після компонування, особливо при додаванні секцій, DMA-буферів і bootloader-reserved діапазонів.[^gnu-ld-memory]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
