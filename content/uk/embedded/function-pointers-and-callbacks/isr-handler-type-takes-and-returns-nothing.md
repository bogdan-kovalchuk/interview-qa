---
id: emb-fnptr-0024
title: "Як оголосити тип ISR handler без аргументів і без return value?"
description: "Тип function pointer описує C callback без аргументів і без значення результату, але не формат hardware vector table."
track: embedded
section: function-pointers-and-callbacks
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
  - source_id: arm-cortex-m-startup
    title: "Arm: Decoding the startup file for Arm Cortex-M4"
    url: "https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/decoding-the-startup-file-for-arm-cortex-m4"
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Приклад Cortex-M4: vector table має початковий stack pointer і адреси handlers; не є однорідним масивом C function pointers."
---

## Short answer

Типово:

`typedef void (*isr_handler_t)(void);`

Цей typedef задає тип C function pointer, але сам по собі не описує hardware vector table. На Cortex-M перший vector є initial stack pointer, тому таблиця має спеціальний layout.[^arm-cortex-m-startup]

Не оголошуй усю Cortex-M vector table як однорідний масив `isr_handler_t`: startup code і linker script задають її платформний формат.[^arm-cortex-m-startup]

## Detailed explanation

Оголошення `typedef void (*isr_handler_t)(void);` створює псевдонім для вказівника на функцію, яка приймає рівно нуль аргументів і повертає `void`. Зірочка в дужках важлива: вона означає pointer на function; без дужок `void *isr_handler_t(void)` оголошувало б функцію, що повертає вказівник на `void`, а це інша конструкція.[^iso-c-n1570]

Тип дозволяє оголосити callback-змінну або елементи звичайної C dispatch table та викликати сумісну функцію через pointer. Сигнатура має відповідати справжньому handler. Передача аргументів, яких функція не очікує, або виклик через несумісний function pointer не стають безпечними лише завдяки typedef; правила C для function call вимагають сумісного типу функції.[^iso-c-n1570]

Водночас цей тип не є повним описом апаратної vector table. Наприклад, Cortex-M vector table має initial stack pointer у першому записі, а записи handler адрес далі; отже, вся таблиця не є простим масивом однакових `isr_handler_t` елементів. Startup assembly або спеціальні декларації та linker script формують правильне розташування, а конкретний ABI визначає деталі входу в ISR.[^arm-cortex-m-startup]

Приклад використання як звичайного callback:

```c
typedef void (*isr_handler_t)(void);
static void timer_handler(void) { /* acknowledge timer */ }
static isr_handler_t callback = timer_handler;
```

Це лише ілюструє тип у C; воно саме по собі не встановлює `callback` у hardware vector table. **Типові помилки:** плутати тип function pointer із типом самої функції, опускати дужки навколо `*name` та припускати, що typedef задає виклик ISR чи апаратне розміщення.[^iso-c-n1570] [^arm-cortex-m-startup]

## Sources

<!-- generated from frontmatter -->
