---
id: emb-dtypes-0093
title: "Як linker script задає адресу `extern const uint8_t image_data[]`?"
description: "Linker script може розмістити вхідну секцію з даними та експортувати символ, який код C трактує як адресу масиву."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
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
  - source_id: gnu-ld-symbols
    title: "GNU ld: Source Code Reference"
    url: https://sourceware.org/binutils/docs/ld/Source-Code-Reference.html
    accessed: 2026-10-04
    kind: official
    version: "2.47"
    applicability: "Пояснює, що визначений у linker script символ є адресою без окремого об’єкта та як посилатися на нього з C; стосується GNU ld."
  - source_id: gnu-ld-sections
    title: "GNU ld: SECTIONS Command"
    url: https://sourceware.org/binutils/docs/ld/SECTIONS.html
    accessed: 2026-10-04
    kind: official
    version: "2.47"
    applicability: "Описує зіставлення input/output sections і розміщення output sections у GNU ld; конкретний memory map задає script."
---

## Short answer

Сам `extern const uint8_t image_data[]` є declaration, а не визначенням масиву; компонувальник зіставляє символ із компонованим образом. Фізична адреса та секція залежать від linker script і target – це не обов’язково Flash або `.rodata`. У GNU `ld` символ, визначений у script, є адресою без окремого об’єкта, тому код зазвичай оголошує його як масив і читає за цією адресою.[^gnu-ld-symbols]

## Detailed explanation

Рядок `extern const uint8_t image_data[];` повідомляє компілятору, що в іншому місці компонованої програми є символ, який можна використовувати як масив байтів лише для читання. У звичайному C-файлі він не виділяє місце й не додає самі байти до образу. Їх може внести інший object-файл або перетворення ресурсу на секцію; linker script задає, як вхідна секція потрапляє до вихідної секції та де та розміщується.[^gnu-ld-sections]

Не можна узагальнювати, що будь-який `const` масив опиняється у Flash. На вбудованій системі linker script може зіставити `.rodata` з ROM, а в іншій схемі розмістити дані у RAM; також образ може мати адресу завантаження окремо від адреси виконання. Для конкретного target відповідь дають карта пам’яті, linker script і map-файл збірки. Це низькорівнева домовленість ABI та компонувальника, а не правило мови C про фізичне розташування `const`.[^gnu-ld-sections]

У GNU `ld` script-символ на кшталт `image_data = ADDR(.flash_resources);` створює запис символу з адресою, але не резервує окрему змінну за цією адресою. Документація GNU ld рекомендує оголосити такий символ у C як масив, наприклад `extern const uint8_t image_data[];`, щоб `image_data` використовувалося як адреса першого байта. Якщо потрібна межа ресурсу, linker script зазвичай експортує окремі start/end символи або код знає довжину з метаданих; сам масивний declaration не передає розмір об’єкта компонувальнику.[^gnu-ld-symbols]

**Приклад:** об’єктний файл може покласти байти у вхідну секцію `.flash_data`, а script включити її в `.flash_resources` і розташувати цей output section у визначеному регіоні. У GNU `ld` `KEEP(*(.flash_data))` корисний, коли використовується garbage collection секцій і ресурс інакше не має звичайного посилання. Перевіряйте фактичний результат у map-файлі: назви секцій і розташування залежать від script, прапорців linker-а та цільового memory map.[^gnu-ld-sections]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
