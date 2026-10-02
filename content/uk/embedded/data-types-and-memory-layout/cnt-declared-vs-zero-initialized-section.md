---
id: emb-dtypes-0055
title: "Що буде у `.bss` vs `.data` для: `uint32_t cnt;` та `uint32_t cnt = 0;` (глобальні)?"
description: "Обидва глобальні оголошення мають початкове значення 0; їхнє розміщення у .bss чи .data залежить від toolchain і linker script."
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
  - source_id: gcc-zero-bss
    title: "GCC: Optimize Options – -fno-zero-initialized-in-bss"
    url: https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Описує типове розміщення нульово ініціалізованих globals у BSS в GCC та прапорець, що його змінює; не описує всі компілятори чи linkers."
---

## Short answer

`uint32_t cnt;` має початкове значення 0; типово toolchain розміщує її у `.bss`, але це не правило мови C.[^gcc-zero-bss]

`uint32_t cnt = 0;` також має початкове значення 0 і GCC за типової конфігурації може розмістити її у `.bss`; прапорці чи інший toolchain можуть змінити секцію.[^iso-c-n1570] [^gcc-zero-bss]

Стандарт C гарантує нуль, а не конкретне ім’я секції. Перевіряй map-файл або ELF для своїх compiler/linker flags; запис `= 0` не змушує змінну перейти у `.data`.[^iso-c-n1570]

## Detailed explanation

Для об’єктів із static storage duration C гарантує початкове нульове значення, якщо ініціалізатор явно не заданий. Тому обидва глобальні оголошення `uint32_t cnt;` і `uint32_t cnt = 0;` мають значення 0 на початку виконання програми. Це властивість мови, а не обіцянка про конкретний сегмент ELF чи фізичну пам’ять.[^iso-c-n1570]

`.bss` та `.data` – домовленості toolchain і linker. Наприклад, GCC зазвичай розміщує нульово ініціалізовані змінні у `.bss`, включно з явним `= 0`, якщо target підтримує таку секцію. Його опція `-fno-zero-initialized-in-bss` змінює цю поведінку; інші компілятори, linker scripts або формати образу можуть мати інші правила. Тому формулювання «без ініціалізатора завжди `.bss`, з `= 0` завжди `.data`» неправильне.[^gcc-zero-bss]

У типовій embedded-системі стартовий код зануляє область `.bss`, а початкові байти `.data` копіює з їх load image у RAM. Це пояснює, чому секція має значення для витрат Flash/RAM, але точний startup contract визначає конкретний проєкт.[^gcc-zero-bss]

**Приклад перевірки:**

```text
arm-none-eabi-nm --print-size firmware.elf
arm-none-eabi-objdump -h firmware.elf
```

Дивись також linker map та командний рядок компіляції. Перевіряй символи після link для того самого target і flags; окремий object file може ще не відображати фінальне розміщення. Якщо потрібно явно зарезервувати RAM чи Flash, задавай це через linker script/атрибут і перевіряй результат, а не покладайся на різницю між формами ініціалізації. У freestanding середовищі також перевір, що startup routine виконується до коду, який читає ці globals: коректне раннє встановлення значень є частиною startup contract конкретної системи. Це відокремлює гарантію компілятора про значення від фактичної процедури запуску на платі.[^iso-c-n1570]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
