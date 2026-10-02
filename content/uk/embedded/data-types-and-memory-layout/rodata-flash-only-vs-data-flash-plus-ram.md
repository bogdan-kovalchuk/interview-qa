---
id: emb-dtypes-0072
title: "Яка різниця між `.rodata` у Flash і `.data` у RAM з точки зору ресурсів?"
description: "Linker script визначає, чи лежать константи у Flash, а ініціалізовані дані часто копіюються з Flash у RAM."
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
  - source_id: gnu-ld
    title: "The GNU linker: Linker Scripts"
    url: https://sourceware.org/binutils/docs/ld.pdf
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Описує VMA, LMA та копіювання ініціалізованих секцій у linker-script прикладах GNU ld; інші linker-и й карти пам'яті можуть відрізнятися."
---

## Short answer

**`.rodata`** часто розміщують у Flash за рішенням linker script; назва секції сама цього не гарантує. Якщо CPU читає її напряму, таблиця не потребує копії в RAM.[^gnu-ld]

Для ініціалізованої `.data` startup-код часто копіює початкові байти з Flash (LMA) до RAM (VMA), витрачаючи місце в обох пам’ятях; це задають linker script і startup-код.[^gnu-ld]

`const` не гарантує розміщення у Flash: перевіряйте linker map і можливості MCU.[^gnu-ld]

## Detailed explanation

`.rodata` і `.data` – звичні назви секцій у toolchain, а не гарантія фізичного розташування. Linker script зіставляє секції з адресними областями; у системі з окремими Flash і RAM він може розмістити константні дані в read-only Flash, якщо процесор може читати її напряму.[^gnu-ld]

Для змінної з початковим значенням типовий сценарій інший: її runtime-адреса (VMA) лежить у RAM, а завантажувальна адреса (LMA) – у Flash. Під час старту startup-код копіює байти з LMA до VMA, щоб програма могла змінювати значення в RAM. Це створює витрати на образ у Flash і на робоче місце в RAM, але точне розміщення визначає компонування, а не правило мови C. У map-файлі ці адреси допомагають побачити фактичний розмір кожної області.[^gnu-ld]

**Приклад:** велику таблицю коефіцієнтів, яку програма лише читає, можна оголосити `const` і розмістити в read-only секції. Якщо MCU читає цю пам’ять напряму, копія таблиці в RAM не потрібна. Окремі MCU мають обмеження швидкості, адресації чи доступу до Flash, а linker script може розмістити секцію інакше; перевіряйте map-файл і документацію плати.[^gnu-ld]

Типова помилка – прирівнювати `const` до «обов’язково лише Flash» або вважати, що `.data` завжди дублюється. Кваліфікатор `const` обмежує зміну через відповідний lvalue у C, а фізичне розміщення й ініціалізація належать до рішень toolchain та платформи. Нуль-ініціалізовані дані зазвичай потрапляють у `.bss`: початковий масив байтів не обов’язково зберігати в образі, хоча під час роботи вони займають RAM. Тому розмір бінарного образу не дорівнює обсягу RAM після старту.[^gnu-ld]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
