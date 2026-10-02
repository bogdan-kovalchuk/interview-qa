---
id: emb-dtypes-0048
title: "Для яких секцій потрібна Flash-to-RAM копія при завантаженні, а для яких - ні?"
description: "У типовій bare-metal схемі startup code копіює .data у RAM і обнуляє .bss; розміщення .rodata залежить від linker script."
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
  - source_id: embedded-gnu-ld
    title: "GNU ld: Using LD"
    url: https://ftp.gnu.org/old-gnu/Manuals/ld-2.9.1/html_chapter/ld_3.html
    accessed: 2026-10-04
    kind: official
    version: "2.9.1 manual"
    applicability: "Приклад linker script пояснює LMA/VMA, копіювання ініціалізованих даних і обнулення .bss; конкретна startup реалізація залежить від цільової системи."
---

## Short answer

У типовій bare-metal схемі `.data` має початкові значення в образі Flash і адресу виконання в RAM, тож startup code копіює байти; `.bss` резервує RAM, яку startup code обнуляє. Розміщення `.rodata` та `.text` залежить від linker script і можливостей MCU, тому назви секцій самі по собі не гарантують читання з Flash чи виконання XIP.[^embedded-gnu-ld]

## Detailed explanation

Секції описують різні потреби програми під час запуску. У типовій вбудованій системі змінні з ненульовою початковою ініціалізацією зберігають значення в образі програми, але використовують RAM під час виконання. Linker script задає load memory address (LMA) у Flash і virtual memory address (VMA) у RAM, а startup code переносить початкові байти перед викликом `main`.[^embedded-gnu-ld]

Для `.bss` потрібен простір у RAM для об’єктів зі статичною тривалістю зберігання, початкове значення яких дорівнює нулю або не задане. У типовому startup цей діапазон не копіюється з Flash: код запуску проходить від початкового до кінцевого символу секції та записує нулі. Отже, «не копіюється» не означає «не потребує роботи під час старту» – обнулення все одно займає час.[^embedded-gnu-ld]

`.rodata` часто містить рядкові літерали та інші константні дані. На MCU з виконанням із Flash linker script зазвичай залишає її там, щоб не витрачати RAM і не копіювати її при старті. Це звична домовленість конкретного toolchain, а не вимога мови C: інший linker script, адресний простір або архітектура можуть розмістити секцію інакше. Аналогічно `.text` може запускатися безпосередньо з Flash лише за підтримки такого режиму пристроєм.[^embedded-gnu-ld]

Практичний приклад: `int counter = 3;` за типової схеми потрапить до `.data`, а `int samples[256];` зі статичною тривалістю зберігання – до `.bss`. Конкретні рішення компілятора й linker залежать від оптимізації, атрибутів і сценарію компонування; дивляться map-файл та startup code, а не лише вихідний код. Перенесення змінної до `const` може дозволити зберігати її в `.rodata`, але не гарантує цього без відповідної конфігурації пам’яті.[^embedded-gnu-ld]

**Типові помилки:**
- Плутати копіювання `.data` з обнуленням `.bss`.
- Вважати `.rodata` або XIP універсальними властивостями всіх платформ.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
