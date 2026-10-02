---
id: emb-dtypes-0038
title: "Що зробить startup code з секцією `.data` перед викликом `main()`?"
description: "У типовому GNU toolchain startup code копіює початкові значення .data з Flash (LMA) у RAM (VMA) перед запуском main()."
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
  - source_id: gnu-ld-lma-vma
    title: "GNU ld documentation: Output Section LMA"
    url: https://sourceware.org/binutils/docs/ld/Output-Section-LMA.html
    accessed: 2026-10-04
    kind: official
    version: "2.47"
    applicability: "Визначає LMA й VMA та описує GNU ld приклад, де секцію завантажують у ROM, а виконують із RAM; не задає обов’язкової startup-послідовності для всіх MCU."
---

## Short answer

У типовому bare-metal GNU toolchain startup code копіює початкові значення `.data` з Flash (LMA – Load Memory Address) у RAM (VMA – Virtual Memory Address); це поширена домовленість, а не універсальна вимога.[^gnu-ld-lma-vma]

Наприклад, ініціалізатор `uint32_t x = 42;` є в образі програми, а startup code копіює його представлення в RAM; порядок байтів залежить від платформи.

GNU startup-файл може копіювати так: `memcpy(&_sdata, &_sidata, &_edata - &_sdata);`, а потім обнуляти `.bss`: `memset(&_sbss, 0, &_ebss - &_sbss);`.[^gnu-ld-lma-vma]

## Detailed explanation

До виклику `main()` середовище виконання має підготувати об’єкти зі статичною тривалістю зберігання. Для типового bare-metal образу початкові значення змінних `.data` лежать у невольатильному сховищі, зазвичай Flash, але під час виконання секція розташована в RAM. У GNU ld linker script може задати для секції адресу завантаження (LMA) у Flash та адресу виконання (VMA) у RAM; startup code типової GNU-конфігурації копіює байти між діапазонами, визначеними linker script.[^gnu-ld-lma-vma]

Копіювання потрібне, бо RAM втрачає вміст після вимкнення живлення, тоді як початкові байти мають бути частиною програмного образу. Код запуску може бути написаний на асемблері або C і в типовій GNU-схемі використовує адресу джерела у Flash та межі `.data` у RAM. Конкретні назви символів і послідовність залежать від MCU, linker script та runtime, тому вирази `_sidata` чи `_sdata` не є вимогою стандарту C.[^gnu-ld-lma-vma] [^iso-c-n1570]

Окремо ділянку `.bss`, призначену для неініціалізованих або нульово ініціалізованих статичних об’єктів, зазвичай обнуляють до `main()`. Це інша операція: для `.data` переносять початкові байти, а для `.bss` записують нулі. Якщо startup code пропускає потрібну ініціалізацію або linker script задає неправильні межі, глобальні змінні можуть мати хибні значення ще до першого рядка прикладного коду.[^iso-c-n1570]

Приклад типової схеми, де символи задає конкретний linker script:
```c
extern unsigned char _sidata, _sdata, _edata;
for (unsigned char *src = &_sidata, *dst = &_sdata; dst < &_edata; )
    *dst++ = *src++;
```

Цей приклад ілюструє копіювання байтів, а не переносимий код для будь-якої системи: порівняння та символи мають відповідати linker script і адресному простору конкретної цілі. Ініціалізовані дані не обов’язково копіюються з Flash у всіх системах – частина MCU може виконувати код або читати константи безпосередньо з невольатильного сховища.[^iso-c-n1570]

**Типова помилка:** вважати, що C сам задає LMA/VMA чи назви startup-символів. Це домовленість toolchain та платформи; перевіряйте linker map і реалізацію startup code.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
