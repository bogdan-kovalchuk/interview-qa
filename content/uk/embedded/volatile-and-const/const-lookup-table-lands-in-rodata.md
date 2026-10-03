---
id: emb-volconst-0025
title: "В яку секцію зазвичай потрапить `const` таблиця?"
description: "У .rodata у Flash, якщо це file-scope або static object і linker script не робить спеціальних винятків."
track: embedded
section: volatile-and-const
level: junior
type: mechanism
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
  - source_id: gnu-ld-linker-scripts
    title: "GNU ld manual: Linker Scripts"
    url: https://sourceware.org/binutils/docs/ld.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Пояснює, що linker script зіставляє секції з областями пам’яті; конкретне розміщення залежить від скрипту."
---

## Question code

```c
const uint16_t sine_lut[256] = { 0, 402, 804 };
```

## Short answer

Зазвичай у read-only section; linker script може розмістити її у Flash, але точні секція й адреса залежать від конфігурації.[^gnu-ld-linker-scripts]

У цьому прикладі 256 елементів типу `uint16_t` займають `256 * 2 = 512` байтів, якщо тип має 16 біт. Якщо linker залишає таблицю в пам’яті програми, яку MCU читає напряму, ці байти не потрібні в SRAM; перевірте це у map-файлі.[^gnu-ld-linker-scripts]

`const` не задає фізичного розміщення: C не визначає `.rodata` чи `.data`, а лише забороняє зміну через цей lvalue.[^iso-c-n1570]

## Detailed explanation

`const uint16_t sine_lut[256]` оголошує масив, елементи якого не можна змінювати через звичайний доступ до `sine_lut`. Це властивість типів C; стандарт не встановлює, чи лежить об’єкт у Flash, SRAM або іншій пам’яті, і не вимагає конкретної назви секції.[^iso-c-n1570]

У типовому embedded toolchain компілятор поміщає такі дані в read-only input section, а linker script відображає цю секцію на output section та адресу в доступному діапазоні ROM/Flash. Скрипт може налаштувати інакше, а різні архітектури мають різні правила читання програмної пам’яті, тож `.rodata` – поширена домовленість, не універсальний наслідок `const`.[^gnu-ld-linker-scripts]

Якщо таблиця читається безпосередньо з Flash, стартова ініціалізація не копіює її в SRAM. Якщо linker script задає RAM-адресу виконання або код старту переносить таблицю для швидшого доступу, SRAM усе одно може використовуватися. Перевіряйте map-файл, ELF-адреси та startup code разом; назва секції сама по собі не підтверджує фізичну адресу.[^gnu-ld-linker-scripts]

Приклад розміру: 256 елементів по 2 байти дають 512 байтів за умови реалізації з 16-бітним `uint16_t`. Якщо таблиця у Flash, що читається напряму, ці 512 байтів заощаджують SRAM порівняно з копією в RAM. Типова помилка – робити висновок про економію лише за словом `const`; спершу перевірте зібраний образ і конфігурацію linker.[^gnu-ld-linker-scripts]

## Sources

<!-- generated from frontmatter -->
