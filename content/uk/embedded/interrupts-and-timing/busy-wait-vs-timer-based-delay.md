---
id: emb-irq-0007
title: "Як реалізований delay у firmware і чому busy-wait delay часто гірший за timer-based підхід?"
track: embedded
section: interrupts-and-timing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: cmsis-core-nvic
    title: "CMSIS-Core (Cortex-M): Interrupts and Exceptions (NVIC)"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__NVIC__gr.html
  - source_id: armv7m-arm
    title: "ARMv7-M Architecture Reference Manual"
    url: https://developer.arm.com/documentation/ddi0403/latest/
  - source_id: freertos-task-delay
    title: "FreeRTOS vTaskDelay API reference"
    url: https://www.freertos.org/Documentation/02-Kernel/04-API-references/01-Task-control/01-vTaskDelay
  - source_id: cmsis-core-cm4-header
    title: "CMSIS 6: core_cm4.h (Cortex-M4 core peripheral access layer)"
    url: https://github.com/ARM-software/CMSIS_6/blob/main/CMSIS/Core/Include/core_cm4.h
  - source_id: cmsis-core-systick
    title: "CMSIS-Core (Cortex-M): SysTick Timer"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__SysTick__gr.html
---

## Short answer

Delay може бути busy loop, CPU cycle counter, SysTick, hardware timer або RTOS sleep. **Timer-based delay** краще зберігає CPU time, дозволяє sleep/power saving і не ламається від зміни clock чи optimization. <span class="warn">Busy-wait блокує main loop/task і погано масштабується для ISR-driven або RTOS firmware.</span>[^dou-embedded-interview]

## Detailed explanation

У вбудованих системах затримки (delays) застосовуються для дотримання таймінгів протоколів зв’язку (I2C, SPI, 1-Wire), очікування стабілізації живлення та аналогових вузлів або формування інтервалів опитування сенсорів. Спосіб організації затримки визначає надійність прошивки, точність часових інтервалів та енергоспоживання пристрою.

### Основні підходи до реалізації затримок

1. **Програмний цикл (Busy-wait loop):**
   Виконання пустого або інкрементного циклу в CPU:
   ```c
   for (volatile uint32_t i = 0; i < count; i++) {
       __NOP();
   }
   ```
   Ключове слово `volatile` запобігає видаленню циклу компілятором під час оптимізації. Проте реальна тривалість циклу залежить від рівня оптимізації (`-O0`, `-O2`, `-Os`), наявності Flash wait states, Flash prefetch, I-Cache та конвеєра ядра.

2. **Апаратний лічильник циклів (DWT CYCCNT):**
   Ядра ARM Cortex-M3/M4/M7 мають лічильник циклів `DWT->CYCCNT`.[^armv7m-arm] Він опційний: біт `DWT_CTRL.NOCYCCNT` показує, що лічильника немає, а перед використанням його вмикають бітами `DEMCR.TRCENA` і `DWT_CTRL.CYCCNTENA`.[^cmsis-core-cm4-header] Увімкнений лічильник рахує кожен такт процесора, дозволяючи реалізувати детермінований мікросекундний polling без калібрування кількості ітерацій циклу. Проте CPU залишається повністю завантаженим.

3. **Апаратний таймер або системний таймер SysTick:**
   SysTick – 24-бітний лічильник ядра (поле `RELOAD` має маску `0xFFFFFF`).[^cmsis-core-cm4-header] Приклад CMSIS налаштовує мілісекундний тік викликом `SysTick_Config(SystemCoreClock / 1000)`, тобто період задається в тактах ядра, і після зміни частоти ядра таймер треба переналаштувати.[^cmsis-core-systick] Периферійний таймер тактується від своєї шини або окремого джерела. Опитування прапорця `COUNTFLAG` або використання глобального лічильника мілісекунд у перериванні `SysTick_Handler` забезпечує незалежність інтервалу від оптимізації коду.

4. **Блокуюча затримка в RTOS (`vTaskDelay` / `vTaskDelayUntil`):**
   При виклику такої функції планувальник переводить поточну задачу зі стану `Running` у стан `Blocked` на вказану кількість системних тіків.[^freertos-task-delay] Процесор негайно перемикається на виконання інших готових задач або переходить у фонову задачу `Idle`, яка може ввести мікроконтролер у режим зниженого енергоспоживання за допомогою інструкції `WFI` (Wait For Interrupt).

### Чому busy-wait критично поступається підходу на базі таймерів

- **Марне витрачання енергії (Power Consumption):** Під час виконання `while` або `for` ядро продовжує споживати максимальний динамічний струм. На відміну від цього, timer-based підхід дозволяє перевести CPU в режим сну (Sleep / Deep Sleep) до спрацьовування таймера.
- **Блокування потоку керування:** У системі типу super-loop (main loop) виклик `delay_ms(100)` зупиняє всю іншу обробку: опитування кнопок, оновлення дисплея чи обробку пакетів.
- **Дрейф тривалості через переривання:** Якщо під час виконання програмного циклу спрацьовує переривання (ISR), процесор призупиняє цикл і витрачає час на виконання обробника. В результаті програмна затримка подовжується рівно на час, витрачений у всіх вкладених ISR. Апаратний же таймер продовжує відлік незалежно від виконання програмного коду ядра.
- **Крихкість при рефакторингу:** Зміна джерела тактування (перемикання з внутрішнього RC-генератора на зовнішній кварц із PLL), увімкнення кешу чи зміна прапорців компілятора руйнує всі розрахунки програмного циклу.

### Коли busy-wait є виправданим

Busy-wait доречний лише для дуже коротких інтервалів (від кількох наносекунд до кількох мікросекунд) – наприклад, очікування кількох тактів для встановлення стабільного рівня на лінії GPIO або затримка між перемиканнями сигналів шини. На таких інтервалах накладні витрати на налаштування переривання таймера чи перемикання контексту RTOS перевищують тривалість самої затримки.
