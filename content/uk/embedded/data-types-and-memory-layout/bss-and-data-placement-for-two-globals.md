---
id: emb-dtypes-0008
title: "Визначте секцію пам'яті: `uint32_t error_count;` (глобальна) та `uint32_t sensor_count = 5;` (глобальна)"
description: "У типовому linker layout нульово ініціалізована глобальна йде в .bss, а ненульово ініціалізована – у .data."
track: embedded
section: data-types-and-memory-layout
level: junior
type: mechanism
tags: []
status: published
updated: 2026-10-04
content_revision: 3
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
  - source_id: gnu-ld-data
    title: "GNU ld: Output Section LMA"
    url: https://sourceware.org/binutils/docs/ld/Output-Section-LMA.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Приклад GNU ld із різними VMA/LMA для .data, копіюванням у RAM і zeroing .bss; це linker layout, не вимога мови C."
---

## Short answer

`error_count` має статичну тривалість зберігання й нульову ініціалізацію, тому в типовому embedded linker layout потрапляє до `.bss`; startup встановлює цю ділянку в нулі. `sensor_count` має ненульове початкове значення, тому за типової схеми з RAM для змінних потрапляє до `.data`: образ початкових байтів зберігається за load address і копіюється до runtime address. Точні секції та адреси задає toolchain і linker script.[^gnu-ld-data]

## Detailed explanation

Обидва оголошення на рівні файлу мають static storage duration: пам’ять для них існує протягом виконання програми, а не лише під час одного виклику функції. За правилами C об’єкт без явного ініціалізатора з такою тривалістю зберігання отримує нульову ініціалізацію.[^iso-c-n1570]

У поширеному embedded linker layout нульово ініціалізовані змінні розміщують у `.bss`. Для економії місця у виконуваному образі `.bss` часто не містить самих нульових байтів: startup код обнуляє відповідний діапазон RAM перед передачею керування програмі.[^gnu-ld-data]

Для `sensor_count` початкове значення дорівнює `5`, тому типовий linker script розміщує змінну у `.data`. Якщо runtime адреса – RAM, початкове значення зазвичай зберігається в образі за окремою load address і startup копіює його до RAM. Отже, фраза «не займає Flash» для `.bss` стосується типового формату образу, а не універсального правила про всі файли прошивки чи карти пам’яті.[^gnu-ld-data]

Назви секцій є домовленістю toolchain. Linker script може об’єднати секції, змінити їх розташування або застосувати іншу модель пам’яті; перевіряйте map-файл і startup-код конкретної збірки.

## Sources

<!-- generated from frontmatter -->
