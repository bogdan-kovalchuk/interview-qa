---
id: emb-fund-0017
title: "Чим архітектура Harvard відрізняється від von Neumann і як це впливає на доступ до Flash/RAM?"
track: embedded
section: fundamentals
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: armv7m-arm
    title: "ARMv7-M Architecture Reference Manual"
    url: https://developer.arm.com/documentation/ddi0403/e/
  - source_id: arm-cortex-m4-guide
    title: "Cortex-M4 Devices Generic User Guide"
    url: https://documentation-service.arm.com/static/5f2ac76d60a93e65927bbdc5
  - source_id: microchip-atmega328p-datasheet
    title: "Microchip Technology: ATmega328P 8-bit AVR Microcontroller Datasheet"
    url: https://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-7810-Automotive-Microcontrollers-ATmega328P_Datasheet.pdf
  - source_id: avr-libc-program-space
    title: "AVR-LibC: Data in Program Space"
    url: https://avrdudes.github.io/avr-libc/avr-libc-user-manual/pgmspace.html
---

## Short answer

У **von Neumann** code і data ділять один address space/bus. У **Harvard** instruction і data memories/buses розділені, тому Flash і RAM можуть мати різні правила доступу. На деяких MCU читання constants із program memory потребує спеціальних instructions/API, а self-programming Flash має обмеження по erase/write і timing.[^dou-embedded-interview]

## Detailed explanation

### Класичні архітектури: von Neumann проти Harvard

Головна відмінність між цими двома моделями полягає в організації шин пам’яті та адресних просторів:

- **Архітектура von Neumann** використовує спільну системну шину (шину адреси та шину даних) і єдиний адресний простір як для виконуваного коду (інструкцій), так і для оброблюваних даних. Процесор не може одночасно за один машинний такт зчитувати код інструкції (instruction fetch) та виконувати операцію читання або запису даних у RAM (data access). Це явище називають «пляшковим горлом фон Неймана» (von Neumann bottleneck).
- **Архітектура Harvard** фізично розділяє пам’ять інструкцій і пам’ять даних на рівні окремих наборів шин і незалежних адресних просторів. Центральний процесор може одночасно здійснювати вибірку наступної інструкції з програмної пам’яті та читати або записувати операнд у пам’ять даних. Це дозволяє реалізувати глибокий конвеєр (instruction pipeline) без затримок на доступ до пам’яті.

### Чистий Harvard в 8-бітних MCU (AVR)

Класичним прикладом гарвардської архітектури у вбудованих системах є 8-бітне сімейство AVR (наприклад, ATmega328P).[^microchip-atmega328p-datasheet] Тут програмна пам’ять (Flash) та пам’ять даних (Data Space: регістри I/O та SRAM) мають повністю ізольовані адресні простори (а EEPROM винесена в окремий енергонезалежний простір):

- Адреса `0x0100` у просторі Flash вказує на 16-бітне машинне слово інструкції, а та сама адреса `0x0100` у просторі Data SRAM вказує на байт змінної в оперативній пам’яті.[^microchip-atmega328p-datasheet]
- Стандартні асемблерні інструкції завантаження й збереження даних (`LD`, `ST`, `LDS`, `STS`) фізично підключені лише до шини даних SRAM. Процесор не може звернутися до Flash за допомогою звичайного вказівника мови C.
- Для читання константних таблиць, шрифтів чи текстових рядків безпосередньо з Flash використовується спеціальна асемблерна інструкція `LPM` (Load Program Memory), яка неявно адресує Flash через регістрову пару `Z` (`r31:r30`).[^microchip-atmega328p-datasheet]
- У мові C для компілятора avr-gcc це вимагає макросу `PROGMEM` та спеціальних викликів на зразок `pgm_read_byte(&variable)` із заголовка `<avr/pgmspace.h>`.[^avr-libc-program-space] Якщо оголосити масив як `const char msg[] = "Test";` без атрибута `PROGMEM`, стартап-код скопіює весь масив із Flash у дефіцитну SRAM під час ініціалізації контролера.

### Modified Harvard у 32-бітних MCU (ARM Cortex-M)

Сучасні 32-бітні ядра ARM Cortex-M (Cortex-M3, M4, M7) використовують модифіковану гарвардську архітектуру (Modified Harvard):[^armv7m-arm]

- **Логічно (для програміста)** адресний простір є єдиним і лінійним (flat 32-bit address space обсягом 4 ГБ).[^armv7m-arm] Flash (діапазон `0x08000000` або `0x00000000`), внутрішня SRAM (`0x20000000`) та периферійні регістри відображені в єдину карту пам’яті.[^arm-cortex-m4-guide] Звичайний вказівник мови C може однаково адресувати як змінну в SRAM, так і константу `const` у Flash. Читання констант виконується стандартною інструкцією `LDR` без додаткових API чи спеціальних мнемонік.
- **Фізично (на рівні кристала)** ядро Cortex-M має розділені шини: ICode (instruction fetch з Flash), DCode (доступ до констант і таблиць векторів у Flash) та System bus (доступ до SRAM, периферії та зовнішньої пам’яті).[^arm-cortex-m4-guide] Завдяки матриці шин (Bus Matrix / Crossbar Switch) ядро може одночасно завантажувати інструкцію через шину ICode та записувати дані в SRAM через шину System bus, що усуває конфлікти шини й забезпечує високу швидкодію.

### Вплив на роботу з Flash і RAM

Різниця в апаратному доступі диктує правила роботи з пам’яттю:

1. **Швидкодія та wait states:** Внутрішня SRAM працює на повній частоті ядра (нуль тактів очікування). Енергонезалежна Flash-пам’ять суттєво повільніша: на високих тактових частотах контролер Flash вимагає налаштування тактів затримки (Flash latency / wait states). Для збереження пропускної здатності використовують попередню вибірку (prefetch) та кеш інструкцій і даних (наприклад, ST ART Accelerator або I/D Cache у Cortex-M7).[^arm-cortex-m4-guide]
2. **Самопрограмування Flash та оновлення прошивки (IAP):** Читання з Flash можливе побайтно або машинними словами без зупинки програми. Проте операції запису та стирання вимагають високої напруги та виконуються цілими секторами або сторінками. Під час запису Flash контролер зазвичай призупиняє шину й виконання коду (Flash stall). Щоб уникнути зриву критичних переривань або зависання під час оновлення прошивки (In-Application Programming), код процедури запису копіюють у RAM і виконують звідти (або використовують мікроконтролери з dual-bank Flash, де виконання коду триває з одного банку під час оновлення іншого).
