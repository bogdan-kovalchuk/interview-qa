---
id: emb-dtypes-0069
title: "Що таке linker script і яку роль він відіграє у розміщенні секцій?"
description: "Linker script зіставляє input sections із output sections та memory regions; розміщення залежить від script і target."
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
  - source_id: gnu-ld-scripts
    title: "GNU ld: Scripts"
    url: https://sourceware.org/binutils/docs/ld/Scripts.html
    accessed: 2026-10-04
    kind: official
    version: "2.47"
    applicability: "Описує призначення linker script та команду MEMORY; синтаксис і startup conventions можуть бути toolchain-specific."
  - source_id: gnu-ld-memory
    title: "GNU ld: MEMORY Command"
    url: https://sourceware.org/binutils/docs/ld/MEMORY.html
    accessed: 2026-10-04
    kind: official
    version: "2.47"
    applicability: "Пояснює опис регіонів пам’яті й обмежень розміщення для GNU ld."
  - source_id: gnu-ld-sections
    title: "GNU ld: SECTIONS Command"
    url: https://sourceware.org/binutils/docs/ld/SECTIONS.html
    accessed: 2026-10-04
    kind: official
    version: "2.47"
    applicability: "Пояснює зіставлення вхідних і вихідних секцій та їх розміщення."
  - source_id: gnu-ld-lma
    title: "GNU ld: Output Section LMA"
    url: https://sourceware.org/binutils/docs/ld/Output-Section-LMA.html
    accessed: 2026-10-04
    kind: official
    version: "2.47"
    applicability: "Пояснює різницю load address і runtime address та синтаксис AT/AT>."
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
---

## Short answer

**Linker script** (`.ld` файл) описує, як linker зіставляє input sections із output sections і керує memory layout; `MEMORY` задає доступні регіони, а `SECTIONS` – їх розміщення.[^gnu-ld-scripts]

Наприклад, `MEMORY` може описати іменовані регіони пам’яті:
`FLASH (rx) : ORIGIN = 0x08000000, LENGTH = 512K`
`RAM (rwx) : ORIGIN = 0x20000000, LENGTH = 128K`.

У `SECTIONS` задаються правила для секцій:
`.text : { *(.text*) } > FLASH`
`.data : { *(.data*) } > RAM AT> FLASH`

Символи на кшталт `_sdata`, `_edata`, `_sidata` linker не створює автоматично: їх зазвичай явно визначає конкретний script для startup code, який копіює `.data` з load address у RAM.[^gnu-ld-lma]

## Detailed explanation

Компілятор формує object files з input sections, наприклад `.text`, `.rodata`, `.data` і `.bss`. GNU linker завжди використовує linker script: явно переданий script замінює вбудований default script. Його основна роль – зіставити input sections у вихідні секції та задати memory layout фінального образу.[^gnu-ld-scripts]

Команда `MEMORY` описує регіони пам’яті, їх початок і довжину. Вона дає linker-у змогу призначати секції та повідомляти про переповнення; імена регіонів локальні для script. Це обмеження компонування, а не виявлення фізичної пам’яті пристрою.[^gnu-ld-memory]

Команда `SECTIONS` збирає вхідні секції у вихідні та визначає розташування. Атрибути `> RAM` і `> FLASH` вибирають регіон для runtime address. Для initialized data часто runtime address (VMA) лежить у RAM, а load address (LMA) – у Flash через `AT>`; це дозволяє startup code скопіювати байти до виконання програми.[^gnu-ld-sections][^gnu-ld-lma] Невдале правило може спричинити переповнення регіону або неправильну адресу завантаження, хоча компіляція окремих файлів минула успішно; тому результат перевіряють після link.

**Приклад:**

```text
.data : { *(.data*) } > RAM AT> FLASH
```

Script може визначити символи-маркери меж `.data`, але їх треба оголосити відповідно до startup code, а назви не стандартизовані. Linker map показує адреси, розміри, секції й вільний простір. Якщо `.data` завелика для RAM, linker сигналізує про переповнення замість автоматичного перенесення. Тому після редагування script перевіряють і map, і стартову ініціалізацію.[^gnu-ld-scripts]

Такі символи позначають адреси, за якими startup code копіює байти, а не звичайні змінні. Перевіряй це оголошення разом із кодом ініціалізації та linker map після змін script.[^gnu-ld-scripts]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
