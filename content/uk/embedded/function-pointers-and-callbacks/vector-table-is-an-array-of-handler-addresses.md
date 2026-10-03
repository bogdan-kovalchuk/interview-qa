---
id: emb-fnptr-0023
title: "Що таке interrupt vector table з точки зору function pointers?"
description: "Це таблиця адрес handler-функцій, яку CPU використовує при exception/interrupt entry."
track: embedded
section: function-pointers-and-callbacks
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
  - source_id: arm-cortex-m-startup
    title: "Arm: Decoding the startup file for Arm Cortex-M4"
    url: "https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/decoding-the-startup-file-for-arm-cortex-m4"
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Приклад Cortex-M4: vector table містить initial stack pointer і адреси reset/exception handlers; інші ядра та MCU можуть мати відмінності."
---

## Short answer

**Це розміщена за визначеною архітектурою таблиця векторів**, серед яких є адреси handlers для exception/interrupt entry.

На Cortex-M перший елемент задає initial stack pointer, а наступні містять адреси Reset_Handler та інших handlers. Це не звичайний C callback API: layout задають архітектура, startup code і linker configuration.[^arm-cortex-m-startup]

ISR handler signature і розміщення vector table мають відповідати startup code, linker script і ABI платформи.[^arm-cortex-m-startup]

## Detailed explanation

Interrupt vector table – це область пам’яті у форматі, визначеному процесорним ядром, звідки воно бере початкові значення для запуску та обробки exceptions. Її часто описують як список адрес функцій, але таке спрощення неповне: на Cortex-M нульовий вектор містить initial stack pointer, а наступний – адресу Reset_Handler; далі йдуть вектори винятків і переривань.[^arm-cortex-m-startup]

Під час reset ядро використовує перші записи для встановлення stack pointer і початку виконання reset handler. Коли виникає відповідний exception або IRQ, індекс вектора визначає, звідки отримується адреса обробника. Тому порядок записів має збігатися з архітектурою та конкретним набором переривань MCU; довільний масив C callbacks не стає vector table лише тому, що містить function pointers.[^arm-cortex-m-startup]

Розташування таблиці і формат записів формуються startup code та linker script. На Cortex-M може використовуватися VTOR для вибору бази таблиці, якщо це підтримується конкретною реалізацією ядра. Звідси випливає, що оновлення таблиці під час запуску application – це платформна операція з вимогами до адреси, вирівнювання та доступу, а не стандартна властивість C.[^arm-cortex-m-startup]

**Типові помилки:**

- Називати кожен елемент vector table звичайним function pointer: перший запис Cortex-M є stack pointer.
- Ігнорувати фіксований порядок vector slots і реалізаційні IRQ MCU.
- Плутати архітектурну таблицю векторів із прикладною dispatch table, що індексується opcode.[^arm-cortex-m-startup]

## Sources

<!-- generated from frontmatter -->
