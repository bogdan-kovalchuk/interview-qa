---
id: emb-dtypes-0050
title: "Що означає? `__attribute__((section(\".ccmram\"))) uint32_t fast_buf[256];`"
description: "Атрибут section просить компілятор помістити масив у секцію .ccmram; фактичне розміщення задає linker script."
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
  - source_id: gcc-common-attributes
    title: "GCC: Common Attributes"
    url: https://gcc.gnu.org/onlinedocs/gcc/Common-Attributes.html
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Пояснює, що section attribute призначає змінну секції об’єктного файла; фізичне розміщення та підтримка залежать від linker і платформи."
---

## Short answer

Атрибут GCC `section(".ccmram")` просить покласти глобальний масив у named input section `.ccmram`; сам по собі він не призначає RAM-адресу, не гарантує швидкість чи сумісність із DMA. Вихідний linker script має зіставити цю секцію з доступною пам’яттю, а startup code – правильно обробити її ініціалізацію.[^gcc-common-attributes]

## Detailed explanation

Атрибут `__attribute__((section(".ccmram")))` GCC змінює секцію об’єктного файла, куди компілятор кладе визначену глобальну змінну. Назва `.ccmram` – домовленість між вихідним кодом і конфігурацією компонування, а не стандартна назва C і не команда процесору ввімкнути особливий режим пам’яті. GCC прямо застерігає, що довільні секції залежать від формату файла й платформи.[^gcc-common-attributes]

Щоб масив справді опинився в конкретній ділянці пам’яті, linker script повинен прийняти input section `.ccmram`, розмістити її у відповідному output section і прив’язати до memory region з адресою та розміром, які існують у цільовому MCU. Без такого правила linker може видати помилку або застосувати інше компонування; це перевіряють у map-файлі та таблиці секцій готового ELF.[^gcc-common-attributes]

Назва часто використовується в STM32-проєктах для Core Coupled Memory, але властивості CCM визначаються конкретною моделлю MCU, а не атрибутом. Не можна робити висновок про нульове очікування, доступність для DMA чи придатність для ISR лише з `.ccmram`: потрібно звірити адресу, підключення до шини, обмеження DMA і характеристики часу в документації саме цього чипа. Тут приклад показує намір компонування, а не універсальну гарантію продуктивності.[^gcc-common-attributes]

Оскільки `fast_buf` не має явного ініціалізатора, startup code також має врахувати цю секцію, якщо за правилами програми її елементи мусять мати початкові нулі. Типові startup routine часто чистять лише стандартну `.bss`; custom section може залишитися поза діапазоном, доки розробник не додасть її символи до linker script і коду запуску. Отже, правильна перевірка охоплює атрибут, linker script, map-файл і startup, а не лише декларацію.[^gcc-common-attributes]

**Типові помилки:**
- Вважати назву `.ccmram` достатньою для фактичного розміщення.
- Приписувати секції властивості конкретного MCU без перевірки його reference manual.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
