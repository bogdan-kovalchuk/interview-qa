---
id: emb-align-0043
title: "Що має продемонструвати кандидат у питаннях про alignment і endianness?"
description: "Передбачати padding і перевпорядковувати поля, пояснювати endianness і коректно вживати htonl/ntohl."
track: embedded
section: memory-alignment-and-endianness
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
  - source_id: posix-htonl
    title: "The Open Group Base Specifications: htonl, htons, ntohl, ntohs"
    url: https://pubs.opengroup.org/onlinepubs/000095399/functions/htonl.html
    accessed: 2026-10-04
    kind: spec
    version: "Issue 6"
    applicability: "Визначає перетворення 16- і 32-бітних значень між host і network byte order; не задає довільний формат серіалізації."
  - source_id: arm-cortex-m-faults
    title: "Arm: Debugging Embedded Systems Part 2: Fault handling and diagnosis"
    url: https://developer.arm.com/community/arm-community-blogs/b/embedded-and-microcontrollers-blog/posts/debugging-embedded-systems-part-2-fault-handling-and-diagnosis
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Описує типи fault і конфігуровані fault через unaligned access на Cortex-M3/M4 та доступний HardFault на Cortex-M0; це не повний архітектурний довідник."
---

## Short answer

**Передбачати можливий padding, пояснювати endianness і серіалізувати поля у визначеному форматі.**

Розміщення полів і padding залежать від ABI; `htonl`/`ntohl` призначені для 32-бітних значень у network byte order, а не для будь-якого wire-формату.[^iso-c-n1570] [^posix-htonl]

Серіалізуй поля явно: розмір, порядок байтів і значення padding мають бути частиною протоколу, а не випадковим образом `struct`.[^iso-c-n1570]

## Detailed explanation

Alignment означає вимоги до адреси, на якій реалізація розміщує об’єкт певного типу. У C вирівнювання членів `struct` і можливі проміжки padding визначаються реалізацією, тому однакова декларація може мати різні `sizeof` та offsets на різних ABI. Перестановка членів іноді зменшує padding, але це слід перевіряти через `sizeof` і `offsetof` саме для цільового компілятора.[^iso-c-n1570]

Endianness описує порядок байтів багатобайтового значення в пам’яті. Це не те саме, що layout `struct`: навіть коли порядок байтів відомий, компілятор може вставити padding. Тому передавання сирого образу `struct` у файл або пакет робить протокол залежним від ABI, endianness і представлення типів. Надійний формат задає ширину кожного поля, byte order і спосіб кодування, після чого байти формуються поле за полем.[^iso-c-n1570]

`htonl` і `ntohl` перетворюють 32-бітне ціле між host byte order і network byte order; відповідні `htons` та `ntohs` працюють із 16-бітними значеннями. Це зручні функції для мережевих протоколів, але вони самі не пакують структуру й не визначають формат прикладного повідомлення.[^posix-htonl]

Наприклад, якщо структура містить `uint8_t kind` і `uint32_t count`, не можна припускати, що її розмір дорівнює п’яти байтам або що поле `count` лежить одразу після `kind`. Для wire-формату запишіть `kind` і окремо чотири байти `count` у погодженому порядку. Не перетворюйте невідоме зміщення pointer cast-ом на `uint32_t *`: таке читання може порушити alignment вимогу типу або межі буфера.[^iso-c-n1570]

**Типові помилки:**

- Вважати padding фіксованим правилом мови, а не властивістю реалізації та ABI.[^iso-c-n1570]
- Називати `htonl` універсальним endian-конвертером для будь-яких довжин і форматів.[^posix-htonl]
- Приписувати всім Cortex-M однакову реакцію на misaligned доступ: поведінка залежить від інструкції, ядра, пам’яті й конфігурації fault handling.[^arm-cortex-m-faults]

## Sources

<!-- generated from frontmatter -->
