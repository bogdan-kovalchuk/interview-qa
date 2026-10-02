---
id: emb-dtypes-0007
title: "Яка послідовність ініціалізації C runtime до виклику `main()` на Cortex-M?"
description: "Ядро бере початкові значення з Vector Table, а startup-код ініціалізує пам’ять і передає керування runtime перед main()."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
tags: []
status: published
updated: 2026-10-04
content_revision: 4
reconciled_with:
  en: 4
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
  - source_id: cmsis-startup
    title: "CMSIS-Core startup file documentation"
    url: https://github.com/ARM-software/CMSIS_6/blob/main/CMSIS/Documentation/Doxygen/Core/src/core_startup_c.md
    accessed: 2026-10-04
    kind: official
    version: "CMSIS_6 main"
    applicability: "Типова роль startup-файлу CMSIS: Reset_Handler, MSP, вектори та передача керування runtime; конкретний порядок залежить від vendor startup."
  - source_id: gnu-ld-data
    title: "GNU ld: Output Section LMA"
    url: https://sourceware.org/binutils/docs/ld/Output-Section-LMA.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Приклад GNU ld із різними VMA/LMA для .data, копіюванням у RAM і zeroing .bss; це linker layout, не вимога мови C."
---

## Short answer

Після reset ядро Cortex-M бере початковий `MSP` і адресу `Reset_Handler` із перших записів Vector Table; їхні адреси у просторі пам’яті визначає конкретна реалізація MCU. Startup code виконує ранню системну ініціалізацію, копіює ініціалізовані дані до RAM, обнуляє ділянки нульової ініціалізації, передає керування C/C++ runtime, а runtime зрештою викликає `main()`. Детальний порядок і таблиці копіювання залежать від startup-файлу та toolchain.[^cmsis-startup] [^gnu-ld-data]

## Detailed explanation

Vector Table задає початкові значення для запуску: ядро встановлює `MSP` із першого запису й бере адресу `Reset_Handler` із запису reset-вектора. Не слід узагальнювати адреси `0x00000000` та `0x00000004`: початкова адреса таблиці залежить від ядра, конфігурації та memory map мікроконтролера.[^cmsis-startup]

Обробник reset зазвичай запускає код ініціалізації платформи, а потім передає керування коду запуску мови. У типовому образі для виконання `.data` має адресу у RAM, але її початкові байти містяться в образі завантаження, часто у Flash; startup копіює їх до RAM. Ділянки `.bss` резервують місце для нульово ініціалізованих об’єктів і startup встановлює там нулі. Linker script визначає розміщення й адреси завантаження, тож секційні назви та точний алгоритм – домовленість конкретного проєкту, а не правило Cortex-M.[^gnu-ld-data]

Після низькорівневого старту C++ runtime може виконати ініціалізатори статичних об’єктів, перш ніж викликати `main()`. У багатьох toolchain-ах ця межа реалізована через `SystemInit`, `_start` або бібліотечні функції; не кожен шаблон має однаковий порядок викликів.[^cmsis-startup]

Наприклад, якщо глобальна змінна має початкове значення `7`, її значення для виконання має бути доступне в RAM до того, як код програми прочитає її. Для типової схеми це означає, що linker розміщує початкові байти у Flash, а startup копіює їх за адресою виконання у RAM; сама C-мова не наказує використовувати саме такі секції або такий спосіб копіювання.[^gnu-ld-data]

Автоматичні локальні об’єкти без явного ініціалізатора не отримують автоматично нульове значення від цього стартового коду. Не покладайтеся на вміст стека: ініціалізуйте такі змінні перед читанням.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
