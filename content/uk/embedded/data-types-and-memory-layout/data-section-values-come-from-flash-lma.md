---
id: emb-dtypes-0083
title: "Що зберігає `.data` секція і звідки береться її значення при завантаженні?"
description: ".data тримає ініціалізовані глобальні, чиї початкові значення startup code копіює з Flash (LMA) у RAM."
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
  - source_id: gnu-ld-lma
    title: "GNU ld manual: Output Section LMA"
    url: https://sourceware.org/binutils/docs/ld/Output-Section-LMA.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Пояснює VMA/LMA та приклад startup-копіювання ROM-образу ініціалізованих даних у RAM; конкретні назви символів визначає linker script."
---

## Short answer

У типовій bare-metal конфігурації `.data` містить дані, що мають початкові значення в RAM; linker script може призначити їм LMA у Flash і VMA у RAM.[^gnu-ld-lma]

Якщо LMA і VMA відрізняються, startup code копіює байти з образу за LMA у діапазон RAM за VMA; символи меж залежать від linker script.

Після цього startup code часто зануляє `.bss`, а тоді викликає `main()`. Деталі залежать від runtime і linker script.[^gnu-ld-lma]

## Detailed explanation

У embedded-системі RAM після reset не обов’язково містить початкові значення глобальних змінних. Тому образ програми зберігає копію ініціалізованих даних у завантажуваній пам’яті, зазвичай Flash. Linker описує два адресні простори для секції: VMA (де секція має бути під час виконання) та LMA (де її байти зберігаються в образі). Для `.data` типовий варіант – VMA у RAM і LMA у Flash; linker script задає це розміщення, наприклад через `AT` або `AT>`.[^gnu-ld-lma]

Під час старту до `main()` startup code бере джерельну адресу образу й копіює діапазон у адресу призначення. У прикладі GNU ld символи linker script позначають початок і кінець робочого діапазону, а цикл переносить байти з ROM-області. У типовому шаблоні `_sidata` є джерелом у Flash, а `_sdata` та `_edata` задають межі RAM, але це лише поширені імена – скрипт або startup-файл може використовувати інші символи чи спосіб копіювання.[^gnu-ld-lma]

Це не те саме, що `.bss`: секція без явного вмісту може резервувати місце в RAM, яке startup code зануляє, тож нульові байти не обов’язково зберігати у Flash-образі. Проте точна класифікація залежить від toolchain, оптимізацій, атрибутів змінних і формату виконуваного файла. Не кожна глобальна змінна мусить лишитися у `.data`: невикористану можуть вилучити, а спеціально розміщені об’єкти можуть потрапити до іншої секції.[^gnu-ld-lma]

**Типові помилки:**

- Казати, що сама назва `.data` гарантує зберігання у Flash. Під час виконання секція зазвичай перебуває в RAM; у Flash лежить її завантажуваний образ за LMA, якщо так налаштовано linker script.[^gnu-ld-lma]
- Вважати `_sidata`, `_sdata` та `_edata` стандартними символами C. Це домовленість між конкретним linker script і startup code.
- Приписувати копіювання компілятору C. Його зазвичай виконує startup/runtime-код, створений або підключений toolchain для конкретного target.[^gnu-ld-lma]

Під час діагностики корисно зіставити три речі: linker script, map-файл та ELF. У map-файлі видно, які input sections потрапили до output `.data`, а в ELF можна перевірити адреси та розміри секцій. Якщо RAM-адреса й адреса завантаження однакові, окреме копіювання може бути зайвим; коли вони різні, завантажувач або startup routine має забезпечити переміщення байтів до використання глобальних змінних.[^gnu-ld-lma]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
