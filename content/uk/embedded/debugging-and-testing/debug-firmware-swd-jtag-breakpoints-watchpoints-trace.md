---
id: emb-debug-0001
title: "Як налагоджувати firmware на реальному MCU через SWD/JTAG, breakpoints, watchpoints і trace?"
track: embedded
section: debugging-and-testing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gdb-manual
    title: "Debugging with GDB"
    url: https://sourceware.org/gdb/current/onlinedocs/gdb.pdf
  - source_id: openocd-arch-commands
    title: "OpenOCD User's Guide: Architecture and Core Commands"
    url: https://openocd.org/doc/html/Architecture-and-Core-Commands.html
  - source_id: openocd-general-commands
    title: "OpenOCD User's Guide: General Commands"
    url: https://openocd.org/doc/html/General-Commands.html
  - source_id: openocd-reset-config
    title: "OpenOCD User's Guide: Reset Configuration"
    url: https://openocd.org/doc/html/Reset-Configuration.html
  - source_id: cmsis-itm
    title: "CMSIS-Core: ITM Functions"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__ITM__Debug__gr.html
---

## Short answer

Підключити probe через SWD/JTAG, завантажити ELF із symbols і перевірити reset/halt sequence. Breakpoints ставлять зупинки в code, watchpoints ловлять read/write конкретної адреси, а trace/SWO/ETM показує події без грубого printf. Для ISR/DMA bugs краще комбінувати debugger з logic analyzer і не зупиняти timing-sensitive code без потреби.[^dou-embedded-interview]

## Detailed explanation

### Ланцюжок налагодження

Налагодження на реальному MCU – це ланцюжок: GDB на host-і, GDB server (OpenOCD, pyOCD або сервер виробника probe), сам probe і debug-інтерфейс мікроконтролера. JTAG – чотирипровідний інтерфейс (TCK, TMS, TDI, TDO), SWD – двопровідний варіант від Arm (SWDIO, SWCLK). OpenOCD приймає з’єднання GDB за замовчуванням на порту 3333.[^openocd-general-commands] GDB має отримати той самий ELF із debug symbols, що прошитий у flash; розбіжність образу і ELF – найчастіша причина "breakpoint не спрацьовує" і "змінні показують нісенітницю".

```sh
arm-none-eabi-gdb build/app.elf
(gdb) target extended-remote :3333
(gdb) monitor reset halt
(gdb) load
(gdb) hbreak main
(gdb) continue
```

### Reset і підключення до "неслухняного" MCU

На Cortex-M є два програмні способи скидання. OpenOCD за замовчуванням використовує `vectreset` (біт VECTRESET в AIRCR), але це скидає лише ядро, а периферія залишається в попередньому стані; `sysresetreq` скидає систему. Cortex-M0, M0+ і M1 `vectreset` не підтримують.[^openocd-arch-commands] Наслідок для налагодження: після "reset" через debugger периферія може бути не в тому стані, що після ввімкнення живлення, і баг ініціалізації не відтворюється.

Якщо firmware одразу після старту перепризначає debug-виводи на GPIO, засинає або має неправильні option bytes, probe не може підключитися. Для цього є connect under reset: OpenOCD з `connect_assert_srst` тримає SRST активним під час підключення; ця можливість підтримується лише частиною цілей, наприклад STM32.[^openocd-reset-config]

### Breakpoints

Software breakpoint – це заміна інструкції на інструкцію зупинки. У RAM це просто, а у flash вимагає перепрограмування, тому для коду у flash GDB server зазвичай використовує апаратні компаратори адреси (на Cortex-M це блок FPB). Команда `hbreak` у GDB явно просить апаратну точку зупинки; GDB прямо зазначає, що її головне призначення – код у ROM, де інструкцію змінити не можна, і що апаратних регістрів обмежена кількість. Для remote target ліміт задається `set remote hardware-breakpoint-limit`.[^gdb-manual] На практиці на Cortex-M їх кілька штук, тому зайві breakpoints треба вимикати.

Кожна зупинка ядра змінює timing: таймери і DMA зазвичай продовжують працювати, UART переповнюється, watchdog може скинути систему, а в motor control зупинка ядра з увімкненим PWM небезпечна. Покроковий режим теж взаємодіє з перериваннями: OpenOCD `cortex_m maskisr auto` спершу дає виконатися pending-обробникам, а потім робить крок із вимкненими перериваннями, і для цього потрібна вільна апаратна точка FPB.[^openocd-arch-commands]

### Watchpoints

Watchpoint зупиняє програму, коли змінюється (`watch`), читається (`rwatch`) або будь-як використовується (`awatch`) вираз чи адреса. Апаратна watchpoint працює без сповільнення і повідомляє про зміну точно на інструкції, що її зробила. Якщо апаратного ресурсу немає, для `watch` GDB ставить програмну (`rwatch` і `awatch` можуть бути лише апаратними): виконує програму покроково й перевіряє значення, що в сотні разів повільніше, а зміну показує на наступному операторі, а не на інструкції.[^gdb-manual] Для embedded це означає: програмна watchpoint на MCU з перериваннями майже непридатна, а апаратних (на Cortex-M це компаратори DWT) кілька штук.

Класичне застосування – пошкодження пам’яті: глобальна змінна раптом змінюється, і невідомо ким. `watch -l g_state.mode` зупинить ядро на інструкції, що записала значення, і `bt` покаже винуватця – переповнення сусіднього масиву, stack overflow задачі чи чужий вказівник. Водночас watchpoint відстежує доступи процесора; запис DMA-контролера в ту саму адресу вона, як правило, не помітить, і тоді треба перевіряти дескриптори DMA.

Ще один інструмент – vector catch: зупинка на HardFault, MemManage, BusFault, UsageFault або reset ще до виконання обробника. OpenOCD нагадує, що без увімкнення в NVIC MemManage, BusFault і UsageFault ескалюють у HardFault, а перевірки ділення на нуль і невирівняного доступу в UsageFault треба вмикати явно.[^openocd-arch-commands]

### Trace: спостерігати, не зупиняючи

Trace потрібен там, де зупинка руйнує симптом. CoreSight має блоки ITM, DWT і ETM, вихід яких іде через TPIU або SWO на вивід SWO (конфігурація SWV) чи на паралельний trace port.[^openocd-arch-commands]

- **ITM** у Cortex-M3/M4/M7 має 32 канали. CMSIS використовує канал 0 для `ITM_SendChar()` – printf-подібного виводу через debug-інтерфейс, а канал 31 резервує для RTOS-ядра.[^cmsis-itm] Це значно дешевше за printf через UART, але не безкоштовно: перед записом код чекає, поки стимул-порт буде готовий (так зроблено і в прикладі CMSIS для каналу 31).[^cmsis-itm]
- **DWT** на ARMv7-M дає лічильник циклів і події, корисні для профілювання.
- **ETM** – трасування інструкцій; потребує паралельного trace port або вбудованого буфера і відповідного probe.[^openocd-arch-commands]
- **RTT** – протокол SEGGER на основі читання й запису пам’яті під час роботи ядра; OpenOCD підтримує його, і він особливо корисний для ядер без SWO, як Cortex-M0.[^openocd-general-commands]

```c
#include "stm32f4xx.h"   /* any CMSIS device header for Cortex-M3/M4/M7 */

void trace_mark(char c)
{
    ITM_SendChar((uint32_t)c);   /* channel 0, visible in the SWO viewer */
}
```

### Що очікують на співбесіді

Кандидат має показати, що вибирає інструмент під клас помилки: breakpoint і стек викликів – для логіки; апаратна watchpoint – для пошкодження пам’яті; vector catch і регістри fault – для HardFault; ITM, RTT, GPIO-маркер і logic analyzer – для timing і ISR/DMA, де зупинка ядра змінює поведінку. І знати обмеження: мало апаратних точок, reset через debugger не дорівнює power-on reset, а зупинене ядро не зупиняє решту світу.
