---
id: emb-safety-0001
title: "Які функції watchdog бувають і чим independent watchdog відрізняється від window watchdog?"
track: embedded
section: safety-security-and-reliability
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iec-61508-1-2010
    title: "IEC 61508-1:2010 – Functional safety: General requirements"
    url: https://webstore.iec.ch/en/publication/5515
  - source_id: zephyr-watchdog-api
    title: "Zephyr Project documentation: Watchdog driver API"
    url: https://docs.zephyrproject.org/latest/doxygen/html/group__watchdog__interface.html
  - source_id: zephyr-wdt-window
    title: "Zephyr Project documentation: wdt_window struct reference"
    url: https://docs.zephyrproject.org/latest/doxygen/html/structwdt__window.html
  - source_id: esp-idf-watchdogs
    title: "ESP-IDF Programming Guide (ESP32): Watchdogs"
    url: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/system/wdts.html
  - source_id: nrf52840-wdt
    title: "nRF52840 Product Specification: WDT – Watchdog timer"
    url: https://docs.nordicsemi.com/bundle/ps_nrf52840/page/wdt.html
  - source_id: ti-tps3430
    title: "TI TPS3430 Window Watchdog Timer with Programmable Reset Delay (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/tps3430.pdf
---

## Short answer

Watchdog скидає систему, якщо firmware не виконує refresh у правильний час. **Independent watchdog** зазвичай має окремий low-speed clock і працює навіть при проблемах main clock. **Window watchdog** вимагає refresh не надто рано й не надто пізно, тому ловить як зависання, так і runaway loop.[^dou-embedded-interview]

## Detailed explanation

Базова функція будь-якого watchdog – скинути систему, якщо firmware вчасно не виконав refresh (qid:emb-irq-0002). Навколо неї виробники додають кілька можливостей, і саме вони відрізняють один watchdog від іншого.

### Які функції бувають

- **Timeout і reset** – обов’язкова частина. Часто можна вибрати, що саме скидати: у Zephyr API прапорці `WDT_FLAG_RESET_SOC`, `WDT_FLAG_RESET_CPU_CORE` або `WDT_FLAG_RESET_NONE` (без скидання).[^zephyr-watchdog-api]
- **Раннє попередження** – переривання або callback перед reset, щоб зберегти діагностику. ESP-IDF описує апаратні watchdogs з чотирма стадіями: ранні можуть генерувати переривання, пізні – reset.[^esp-idf-watchdogs]
- **Кілька каналів** – окремі timeout для різних частин системи; у Zephyr кожен встановлений timeout має свій channel ID для `wdt_feed()`.[^zephyr-watchdog-api]
- **Незалежне тактування** – watchdog працює від власного генератора.
- **Вікно** – refresh приймається лише в певному інтервалі часу.
- **Захист від вимкнення** – конфігурацію блокують після старту, а в деяких реалізаціях watchdog не можна вимкнути з коду застосунку.[^zephyr-watchdog-api]

### Independent watchdog

Його суть – незалежність від того, що може зламатися разом із програмою. Найчастіше йдеться про тактування: якщо watchdog рахує від того самого clock, що й CPU, то зупинка чи збій main clock зупиняє і watchdog, і захисту немає. Тому independent watchdog живиться від окремого low-speed генератора. Наприклад, WDT у nRF52840 рахує від LFCLK і, якщо інше джерело 32,768 kHz не працює, сам примусово вмикає RC-генератор 32,768 kHz.[^nrf52840-wdt]

Найвищий ступінь незалежності дає зовнішня мікросхема watchdog: вона має власне тактування і виставляє сигнал скидання на вхід reset MCU, тому продовжує працювати навіть тоді, коли внутрішній watchdog вимкнено помилковою конфігурацією або пошкоджено разом з рештою кристала. Приклад – TPS3430 від TI, автономний window watchdog з програмованим вікном і затримкою reset.[^ti-tps3430]

Недолік простого (не віконного) watchdog у тому, що він контролює лише верхню межу: якщо refresh надійшов будь-коли до timeout, усе гаразд.

### Window watchdog

Window watchdog вимагає, щоб refresh надійшов не пізніше верхньої межі і не раніше нижньої. У datasheet TPS3430 імпульс на вході WDI має прийти між `tWDL(max)` і `tWDU(min)`; передчасний імпульс фіксується як early fault, запізнілий – як late fault, і в обох випадках вихід WDO переходить в активний низький рівень на час `tRST`. Перший імпульс після старту обробляється як у звичайного watchdog, тобто має прийти лише до верхньої межі.[^ti-tps3430] У Zephyr те саме задається структурою `wdt_window` з полями `min` і `max` у мілісекундах; якщо апаратура не підтримує вікна, `min` має дорівнювати 0, а значення, які неможливо встановити точно, округлюються вгору.[^zephyr-wdt-window]

Навіщо нижня межа: збій може загнати програму в короткий цикл, який раз у раз проходить через виклик refresh. Звичайний watchdog такий стан пропустить, бо refresh надходить навіть частіше, ніж треба. Window watchdog побачить надто ранній refresh і скине систему. Так само він реагує на програму, що пропускає частину роботи і через це доходить до refresh раніше.

### Як вибрати вікно

Refresh має надходити з детермінованого місця з відомим періодом, наприклад з циклічного task. Межі вікна рахують з урахуванням jitter циклу і допуску генератора watchdog. Приклад: task з періодом 50 мс і jitter ±5 мс робить refresh через 45–55 мс після попереднього. Вікно `min = 40 мс`, `max = 60 мс` має запас по 5 мс з обох боків. Якщо refresh викликати з місця, де період плаває (обробник подій, цикл з довгими блокувальними операціями), вікно доведеться розширити настільки, що його нижня межа втратить сенс.

### Порівняння коротко

- Independent: захищає від відмови основного тактування і програмних зависань; контролює лише «не пізніше».
- Window: контролює «не раніше і не пізніше», тож ловить також runaway-код; вимагає детермінованого розкладу refresh.
- Зовнішній window watchdog поєднує обидві властивості і не залежить від кристала MCU.

### Що хоче почути інтерв’юер

Що independent означає незалежне тактування (а в ідеалі – окремий кристал), а window означає двосторонню перевірку часу. Плюс розуміння, що вікно треба розраховувати з допусками і що refresh із таймерного переривання знецінює будь-який watchdog.
