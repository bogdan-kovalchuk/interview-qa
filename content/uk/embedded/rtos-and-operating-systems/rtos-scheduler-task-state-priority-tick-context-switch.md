---
id: emb-rtos-0012
title: "Як працює RTOS scheduler і що означають task state, priority, tick і context switch?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: freertos-kernel-book
    title: "FreeRTOS Kernel Book and Reference Manual"
    url: https://www.freertos.org/Documentation/02-Kernel/07-Books-and-manual/01-RTOS_book
  - source_id: freertos-port-cm4f
    title: "Вихідний код FreeRTOS-Kernel: portable/GCC/ARM_CM4F/port.c"
    url: https://github.com/FreeRTOS/FreeRTOS-Kernel/blob/main/portable/GCC/ARM_CM4F/port.c
  - source_id: freertos-portmacro-cm4f
    title: "Вихідний код FreeRTOS-Kernel: portable/GCC/ARM_CM4F/portmacro.h"
    url: https://github.com/FreeRTOS/FreeRTOS-Kernel/blob/main/portable/GCC/ARM_CM4F/portmacro.h
---

## Short answer

RTOS scheduler вибирає ready task з найвищим priority або за policy для однакового priority. **Task state** описує ready/running/blocked/suspended, **tick** дає системний time base, а **context switch** зберігає registers поточної task і відновлює іншу. Preemption дозволяє вищому priority task витіснити нижчий.[^dou-embedded-interview]

## Detailed explanation

Розглянемо механізм на прикладі FreeRTOS на одноядерному MCU: терміни в інших RTOS (Zephyr, ThreadX, embOS) відрізняються назвами, але модель та сама. Scheduler – це код ядра RTOS, який вирішує, яка задача зараз виконується, і лише він переводить задачі в стан Running і з нього.[^freertos-kernel-book]

### Стани задачі

На одному ядрі в стані **Running** може бути лише одна задача; усі інші – у стані Not Running, який має три підстани:[^freertos-kernel-book]

- **Ready** – задача може виконуватися, але зараз не виконується.
- **Blocked** – задача чекає події: часової (минув інтервал `vTaskDelay()` чи настав абсолютний момент) або синхронізаційної (дані в queue, semaphore, mutex, event group, task notification). Чекання синхронізаційної події може мати timeout, тобто задача чекає обидва типи одночасно. У стані Blocked задача не споживає процесорного часу.
- **Suspended** – задача недоступна scheduler-у, доки її явно не відновлять через `vTaskResume()` або `xTaskResumeFromISR()`; таймаутів тут немає, і більшість застосунків цей стан не використовує.

Коли задачу знімають з виконання, її стан зберігається, і наступного разу вона продовжує роботу з тієї інструкції, на якій зупинилася.[^freertos-kernel-book]

### Пріоритети і правило вибору

У FreeRTOS пріоритети – числа від 0 (найнижчий) до `configMAX_PRIORITIES - 1`; кілька задач можуть мати однаковий пріоритет. Scheduler завжди обирає готову задачу з найвищим пріоритетом. Загальна реалізація на C не обмежує кількість пріоритетів, а оптимізована під архітектуру має сталий час вибору, але обмежує їх 32 на 32-бітних архітектурах.[^freertos-kernel-book] Idle task створюється автоматично під час `vTaskStartScheduler()` з пріоритетом 0, щоб завжди була задача, яку можна виконати.[^freertos-kernel-book]

Режим планування задають два параметри:[^freertos-kernel-book]

- `configUSE_PREEMPTION = 1`, `configUSE_TIME_SLICING = 1` – fixed-priority preemptive scheduling з time slicing, найпоширеніший варіант. Задача вищого пріоритету, що стала Ready, витісняє поточну негайно, у будь-який момент, а не тільки на tick. Задачі однакового пріоритету чергуються на кожному tick.
- `configUSE_TIME_SLICING = 0` – те саме без чергування рівних пріоритетів: менше перемикань, але задачі однакового пріоритету можуть отримувати дуже різну частку часу.
- `configUSE_PREEMPTION = 0` – cooperative: перемикання лише тоді, коли задача блокується або викликає `taskYIELD()`.

### Tick

Tick – періодичне апаратне переривання (на Cortex-M зазвичай SysTick), яке дає RTOS часову базу. Частоту задає `configTICK_RATE_HZ`: при 100 Гц один tick (і один time slice) триває 10 мс. Усі таймаути API вказуються в ticks, а `pdMS_TO_TICKS()` переводить мілісекунди в ticks, тому роздільна здатність таймаутів обмежена періодом tick. Лічильник tick-ів рахує переривання від старту scheduler-а.[^freertos-kernel-book] На кожному tick ядро оновлює лічильник, переводить у Ready задачі, чий час очікування минув, і за потреби запитує перемикання. Однак scheduler запускається не лише на tick: також одразу після того, як поточна задача заблокувалася, і коли переривання перевело в Ready задачу вищого пріоритету.[^freertos-kernel-book]

Важлива деталь – різниця між відносною і абсолютною затримкою. `vTaskDelay()` рахує ticks від моменту виклику, тож тривалість роботи задачі додається до періоду. Для періодичної задачі потрібен `vTaskDelayUntil()`, який будить задачу в точний момент лічильника tick-ів:[^freertos-kernel-book]

```c
static void control_task(void *arg)
{
    TickType_t last_wake = xTaskGetTickCount();

    for (;;) {
        vTaskDelayUntil(&last_wake, pdMS_TO_TICKS(10)); /* fixed 10 ms period */
        read_sensor();
        update_actuator();
    }
}
```

Режим `configUSE_TICKLESS_IDLE` може надовго зупиняти tick, коли нічого не готове до виконання, щоб заощадити енергію.[^freertos-kernel-book]

### Context switch

Context switch – збереження регістрів поточної задачі на її власний стек і відновлення регістрів іншої задачі. На ARM Cortex-M4F (порт GCC/ARM_CM4F) це реалізовано так:[^freertos-port-cm4f]

1. Під час старту scheduler-а порт робить PendSV і SysTick переривань найнижчого пріоритету.
2. Обробник SysTick викликає `xTaskIncrementTick()` і, якщо потрібне перемикання, лише встановлює біт pending для PendSV.[^freertos-port-cm4f] Те саме роблять `portYIELD()` і `portYIELD_FROM_ISR()`: обидва макроси записують біт `PENDSVSET` у регістр керування перериваннями.[^freertos-portmacro-cm4f]
3. Обробник PendSV читає PSP поточної задачі, зберігає на її стек `r4`–`r11`, `r14` і, якщо задача використовувала FPU, `s16`–`s31`; решту регістрів процесор уже поклав на стек апаратно при вході у виняток. Новий top of stack записується в TCB.
4. `vTaskSwitchContext()` обирає наступну задачу, після чого PendSV відновлює її регістри з її стека, встановлює PSP і повертається з винятку, вже в нову задачу.

Через найнижчий пріоритет PendSV виконується лише тоді, коли не активний жоден інший обробник, тож перемикання задач не вклинюється в обслуговування апаратних переривань. Про апаратну частину входу у виняток і `EXC_RETURN` – qid:emb-irq-0005.

Коли API викликано з ISR (функції з суфіксом `FromISR`), перемикання автоматично не відбувається: функція встановлює `*pxHigherPriorityTaskWoken = pdTRUE`, і ISR має викликати `portYIELD_FROM_ISR()`. Якщо цього не зробити, розбуджена задача вищого пріоритету чекатиме до наступного запуску scheduler-а, у найгіршому разі до наступного tick.[^freertos-kernel-book]

### Типові помилки

- Активне очікування (порожній цикл) у задачі високого пріоритету: вона ніколи не блокується і повністю позбавляє часу нижчі пріоритети.[^freertos-kernel-book]
- `vTaskDelay()` там, де потрібен стабільний період.
- Очікування точності, кращої за період tick, від таймаутів RTOS.
- Пропущений `portYIELD_FROM_ISR()` після `...FromISR()` і, як наслідок, затримка реакції до одного tick.
- Однакові пріоритети для задач з різними вимогами до latency, через що поведінка залежить від time slicing.
