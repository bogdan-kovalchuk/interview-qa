---
id: emb-irq-0002
title: "Що таке watchdog?"
track: embedded
section: safety-security-and-reliability
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: cmsis-core-nvic
    title: "CMSIS-Core (Cortex-M): Interrupts and Exceptions (NVIC)"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__NVIC__gr.html
  - source_id: linux-watchdog-api
    title: "The Linux Watchdog driver API"
    url: https://docs.kernel.org/watchdog/watchdog-api.html
  - source_id: nrf52840-wdt
    title: "nRF52840 Product Specification: WDT – Watchdog timer"
    url: https://docs.nordicsemi.com/bundle/ps_nrf52840/page/wdt.html
  - source_id: zephyr-watchdog-api
    title: "Zephyr Project documentation: Watchdog driver API"
    url: https://docs.zephyrproject.org/latest/doxygen/html/group__watchdog__interface.html
  - source_id: esp-idf-watchdogs
    title: "ESP-IDF Programming Guide (ESP32): Watchdogs"
    url: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/system/wdts.html
---

## Short answer

**Watchdog Timer (WDT)** – апаратний таймер, що автоматично скидає (reset) мікроконтролер, якщо програма не «погодувала» його вчасно.[^dou-embedded-interview]

Принцип: програма повинна регулярно записувати спеціальне значення в регістр WDT («kick» або «feed»). Якщо цього не відбулося – таймер спрацьовує і виконується system reset.

Захищає від: зависання програми, нескінченного циклу, stack overflow. Типи: **IWDG** (independent, від окремого генератора, не зупиняється при зупинці основного тактування) і **WWDG** (window watchdog – скидати треба лише у певному часовому вікні, захист від «годування занадто часто»).

## Detailed explanation

Watchdog timer – апаратна схема, яка може скинути систему у разі програмної відмови.[^linux-watchdog-api] По суті це лічильник, що рахує незалежно від CPU; програма періодично перезапускає його (feed, kick, refresh), а якщо перезапуску не було протягом заданого timeout, watchdog ініціює reset. Ідея проста: зависла програма не може сама помітити, що зависла, а окремий лічильник – може.

### Як це виглядає в регістрах

Добрий приклад – WDT у nRF52840. Він рахує вниз від low-frequency clock (LFCLK) і, якщо жодне інше джерело 32,768 kHz не працює, сам примусово вмикає RC-генератор 32,768 kHz. Timeout задає reload value: `timeout [s] = (CRV + 1) / 32768`. Щоб перезапустити лічильник, у кожен увімкнений reload request register треба записати спеціальне значення `0x6E524635`. Після старту регістри CRV, RREN і CONFIG блокуються для подальшої конфігурації.[^nrf52840-wdt]

Приклад розрахунку: для timeout 2 с потрібно `CRV + 1 = 2 * 32768 = 65536`, тобто `CRV = 65535`.

Спеціальне значення і заблокована конфігурація мають практичний сенс: випадковий запис у пам’ять «загубленою» програмою навряд чи погодує watchdog чи вимкне його. З тієї ж причини деякі watchdogs взагалі не можна вимкнути з коду застосунку; у Zephyr API на такий випадок передбачено код помилки `-EPERM` для `wdt_disable()`.[^zephyr-watchdog-api]

### Від чого захищає і від чого ні

Watchdog ловить стани, у яких програма перестала проходити точку годування: нескінченний цикл, deadlock, очікування прапорця, що ніколи не з’явиться, crash, після якого ядро застрягло у fault handler. Stack overflow він ловить лише опосередковано – якщо зіпсована пам’ять призвела до зависання.

Не ловить він логічні помилки, за яких цикл продовжує крутитися й годувати лічильник: застосунок «живий», але робить не те. Також звичайний watchdog не бачить runaway-коду, що годує його надто часто; для цього існує window watchdog (qid:emb-safety-0001).

### Де годувати

Найпоширеніша помилка – годувати watchdog з таймерного переривання. Переривання продовжують надходити, навіть коли основний цикл або task зависли, тож watchdog ніколи не спрацює. ESP-IDF показує, як правильно розділити ролі: Interrupt Watchdog годується з tick-переривання FreeRTOS і тому виявляє ситуації, коли самі ISR надовго заблоковані, а Task Watchdog стежить за конкретними tasks (за замовчуванням – за idle task кожного CPU) і виявляє tasks, що довго працюють без yield.[^esp-idf-watchdogs]

У багатозадачній системі watchdog зазвичай годує один supervisor, який перед цим перевіряє heartbeat кожного критичного task. Якщо хоч один task не відзвітував за свій період, feed пропускають, і система скидається.

### Попередження перед reset

Скидання знищує стан, потрібний для діагностики, тому багато watchdogs мають кілька стадій. У ESP-IDF апаратні watchdogs мають чотири стадії timeout: ранні можна налаштувати на переривання, пізні – на system reset; Interrupt Watchdog спочатку викликає panic handler, а друга стадія апаратно скидає чип.[^esp-idf-watchdogs] У nRF52840, якщо ввімкнено переривання TIMEOUT, reset відкладається на два такти 32,768 kHz після події.[^nrf52840-wdt] У Linux аналогічну роль виконує pretimeout: окремий сигнал за задану кількість секунд до скидання, щоб ядро встигло зберегти діагностику.[^linux-watchdog-api] За цей час встигають зберегти причину й адресу в пам’ять, що переживає reset.

### Практичні деталі

- **Debugger.** Якщо watchdog не налаштовано інакше, він може продовжувати рахувати під час зупинки на breakpoint і скинути плату посеред налагодження. nRF52840 після reset за замовчуванням продовжує рахувати в сні, але ставить лічильник на паузу, поки CPU зупинений debugger-ом; обидві поведінки задаються в регістрі CONFIG;[^nrf52840-wdt] у Zephyr це опції `WDT_OPT_PAUSE_IN_SLEEP` і `WDT_OPT_PAUSE_HALTED_BY_DBG`.[^zephyr-watchdog-api] Пауза в сні – свідомий компроміс: watchdog тоді не захищає від зависання в low-power режимі.
- **Після reset.** Firmware читає причину скидання, записує її в лог і рахує послідовні watchdog resets; якщо їх забагато, переходить у safe mode або відкочує оновлення, а не крутиться в нескінченному циклі reset.
- **Linux.** У системах з ОС watchdog годує userspace daemon через `/dev/watchdog`. Якщо драйвер підтримує magic close, він не вимикає watchdog при закритті файлу, доки перед цим не записано символ `V`, а з `CONFIG_WATCHDOG_NOWAYOUT` запущений watchdog не можна вимкнути взагалі; тож аварійне завершення daemon закінчиться reboot після timeout.[^linux-watchdog-api]

### Що хоче почути інтерв’юер

Що watchdog – останній рубіж, а не заміна обробки помилок; що feed має підтверджувати здоров’я всієї системи, а не просто факт роботи переривань; що timeout вибирають з урахуванням найдовшої легітимної операції (запис flash, handshake); і що після reset треба знати його причину.
