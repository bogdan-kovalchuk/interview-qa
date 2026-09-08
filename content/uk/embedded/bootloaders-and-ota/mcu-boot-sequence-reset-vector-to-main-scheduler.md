---
id: emb-boot-0005
title: "Що відбувається під час boot sequence MCU від reset vector до main або scheduler start?"
description: "Після reset CPU бере SP і reset handler з vector table, startup code копіює .data, очищає .bss, викликає constructors і переходить у main, далі ініціалізуються HAL/drivers і запускається scheduler."
track: embedded
section: bootloaders-and-ota
level: senior
type: concept
tags: []
status: published
updated: 2026-09-08
content_revision: 4
reconciled_with:
  en: 4
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження цього питання й відповіді; текст відповіді не перевірений незалежно від оригінальної Anki-колоди спільноти."
  - source_id: mcuboot-design
    title: "MCUboot design documentation"
    url: https://docs.mcuboot.com/design.html
    accessed: 2026-09-06
    kind: official
    version: "current"
    applicability: "Авторитетне джерело рівня секції для понять розділу bootloaders-and-ota; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
  - source_id: armv7m-arm
    title: "ARMv7-M Architecture Reference Manual"
    url: https://developer.arm.com/documentation/ddi0403/e/
    accessed: 2026-09-08
    kind: official
    version: "E"
    applicability: "Архітектура ARMv7-M; reset behavior, vector table та exception model."
---

## Short answer

Після reset CPU бере initial stack pointer і reset handler з vector table. Startup code налаштовує low-level runtime: clock мінімально або пізніше, копіює `.data` з flash у RAM, очищає `.bss`, викликає constructors у C++ і переходить у `main`. Далі firmware ініціалізує HAL/drivers, interrupts, RTOS objects і запускає scheduler.[^dou-embedded-interview]

## Detailed explanation

Після reset CPU на ARM Cortex-M виконує послідовність, визначену архітектурою ARMv7-M:

1. **Hardware reset.** CPU завантажує початковий MSP з адресу `0x00000000` (Flash base) і адресу Reset Handler з `0x00000004`. PC отримує адресу Reset Handler – виконання починається звідти.

2. **Reset Handler and startup code.** Reset Handler – це зазвичай `Reset_Handler` у startup-файлі (`startup.s`). Він викликає `SystemInit` (базове тактування) і виконує ініціалізацію C/C++ runtime: копіює `.data` з Flash у RAM, заповнює `.bss` нулями, викликає конструктори глобальних об'єктів C++ (`__libc_init_array`).

3. **Виклик `main()`.** Після завершення runtime-ініціалізації викликається `main`.

4. **Ініціалізація HAL/drivers.** У `main` firmware ініціалізує HAL (Hardware Abstraction Layer) або драйвери: тактування (PLL, clock tree, prescalers), GPIO, периферію (UART, SPI, I2C, ADC), DMA.

5. **Конфігурація interrupts.** Налаштування NVIC (Nested Vectored Interrupt Controller): пріоритети переривань (preemption priority, sub-priority), реєстрація ISR-обробників у vector table, увімкнення переривань.

6. **Створення RTOS-об'єктів.** Якщо використовується RTOS (FreeRTOS, Zephyr, ThreadX): створюються черги, семафори, м'ютекси, task-дескриптори.

7. **Запуск scheduler.** Викликається `osKernelStart()` (CMSIS-RTOS) або еквівалент. Scheduler починає виконання tasks відповідно до пріоритетів. Для bare-metal систем `main` зазвичай входить у нескінченний цикл (`while(1)`) з опитуванням подій або очікуванням переривань (`__WFI()`).

**Ключовий момент для переходу від bootloader до application:** bootloader записує нове значення у VTOR (Vector Table Offset Register), щоб CPU використовував vector table application, а не bootloader'а. Без цього переривання application будуть оброблятися через handler'и bootloader'а, що призведе до crash.

**Ініціалізація .data/.bss і конструктори** – обов'язкові перед `main`, інакше глобальні змінні міститимуть сміття, а C++-об'єкти не будуть сконструйовані. Це вимога C/C++ ABI.[^armv7m-arm]

## Evaluation guide

### Expected signals

- Чітко називає адресу vector table: SP з `0x00000000`, reset handler з `0x00000004`; розуміє, чому саме такий порядок (ARMv7-M spec).
- Пояснює .data/.bss ініціалізацію як вимогу C/C++ ABI, не просто «copy-paste з linker script».
- Згадує VTOR і пояснює, чому bootloader мусить його оновити перед передачею керування.
- Розрізняє bare-metal superloop і RTOS scheduler; називає конкретні RTOS (FreeRTOS, Zephyr, ThreadX).
- Згадує NVIC priority grouping (preemption vs sub-priority) і його вплив на ISR latency.
- Описує __libc_init_array / constructors для C++ і чому це критично.

### Red flags

- Не знає, що перші два слова Flash – це SP і PC, а не код.
- Плутає Cortex-M boot з Cortex-A (MMU, Linux boot, U-Boot -> kernel).
- Не згадує .bss або вважає, що RAM ініціалізується апаратно.
- Не розуміє різниці між MSP і PSP (Main vs Process Stack Pointer).
- Не може пояснити, чому VTOR необхідний при переході від bootloader до application.

### Level-up follow-up

- Як змінюється boot sequence, якщо є secure bootloader (TrustZone, SAU)?
- Як ініціалізація clock (PLL lock time) впливає на boot time і як її мінімізувати?
- Як C++ exceptions та RTTI впливають на startup code і vector table (exception tables)?

## Sources

<!-- generated from frontmatter -->
