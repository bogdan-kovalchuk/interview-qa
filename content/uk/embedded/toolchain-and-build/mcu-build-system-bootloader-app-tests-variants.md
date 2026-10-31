---
id: emb-build-0024
title: "Як побудувати build system для MCU-проекту з bootloader, application, tests і hardware variants?"
track: embedded
section: toolchain-and-build
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gcc-overall-options
    title: "GCC manual: Options Controlling the Kind of Output"
    url: https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
---

## Short answer

Розбий build на окремі targets: `bootloader`, `app`, shared drivers, host tests, target tests і board configs. Кожен target має свій linker script, startup file, compile definitions, memory layout і output artifacts. Hardware variants краще описувати через board files/config targets, а не умовні блоки у кожному source file.[^dou-embedded-interview]

## Detailed explanation

### Модульна декомпозиція та ієрархія цілей (Targets)

Побудова сучасної системи збирання для складного мікроконтролерного продукту (зазвичай на базі CMake та Ninja) вимагає суворого розділення монолітної прошивки на ізольовані таргети[^gcc-overall-options]:

1. **Bootloader Target**:
   - Має власний мінімалістичний скрипт компонування, прив’язаний до початку Flash-пам’яті (наприклад, сектори 0–1, адреси `0x08000000–0x0800FFFF`).
   - Використовує окремий мінімальний startup-код без підключення "важких" компонентів операційної системи.
   - Відповідає за перевірку цілісності та автентичності основної програми (CRC32, SHA-256, ECDSA), обробку аварійного відновлення та оновлення по інтерфейсах UART/CAN/USB.
2. **Application Target**:
   - Розміщується зі зміщенням у Flash (offset, наприклад з адреси `0x08010000` з урахуванням вирівнювання таблиці векторів `VTOR`).
   - Підключає повний стек RTOS, мережеві бібліотеки та бізнес-логіку пристрою.
3. **Shared Components Library (`libshared`)**:
   - Статична бібліотека, що містить спільні структури даних: формат заголовка прошивки (`FirmwareHeader_t`), версії протоколів, криптографічні ключі та спільні константи розподілу оперативної пам’яті (No-Init RAM для передачі boot-прапорців між перезавантаженнями).
4. **Host Unit Tests Target**:
   - Модулі чистої бізнес-логіки та алгоритмів компілюються під нативну хост-систему (x86_64 / Clang / GCC) для миттєвого проходження тестів (Unity, GoogleTest, CppUTest) без використання фізичного заліза чи емуляторів. Апаратні драйвери HAL підміняються моками (mocking frameworks).
5. **Target / HIL Integration Tests**:
   - Спеціальні прошивки, які прошиваються у реальний мікроконтролер для тестування низькорівневої апаратури (DMA, шини I2C, пам’ять Flash, таймери).

### Керування апаратними ревізіями (Hardware Variants)

Класична антипатерна практика полягає у захаращенні коду макросами умовного компілювання виду `#ifdef BOARD_REV_1_2`. Це унеможливлює тестування коду, руйнує модульність і веде до помилок компіляції під час зміни однієї конфігурації.

У професійних білд-системах застосовують патерн **Board Support Package (BSP) Configuration Targets**:
- Створюється окремий каталог конфігурацій `bsp/` з підкаталогами під кожну ревізію плати (`boards/rev_a/`, `boards/rev_b/`).
- Кожен підкаталог містить файл конфігурації виводів (pinout mapping), параметри тактування та розміри встановленої мікросхеми Flash/RAM.
- У CMake ревізія обирається через параметр збирання, наприклад `-DBOARD_VARIANT=rev_b`. Білд-система підключає відповідний каталог через `target_include_directories()` та призначає специфічний linker script, зберігаючи весь прикладний код незмінним.

### Організація пам’яті та вихідні артефакти

Для уникнення колізій між завантажувачем та додатком застосовують незалежні конфігурації адресного простору[^gnu-ld-manual]:
- **Memory Map Contracts**: єдиний YAML або конфігураційний файл верхнього рівня визначає межі Flash/RAM, на основі якого скрипти автоматично генерують `bootloader.ld`, `app.ld` та C-заголовки зміщень векторів.
- **Пост-процесинг артефактів**:
  1. Після компіляції створюються незалежні файли `bootloader.elf` та `app.elf`.
  2. За допомогою `objcopy` генеруються двійкові образи `.bin` та шістнадцяткові файли `.hex`.
  3. **Склейка заводського образу**: за допомогою утиліти `srec_cat` або спеціального Python-скрипта бінарники завантажувача та додатка об’єднуються в один цілісний файл `factory_production.hex` для одноразового прошивання на виробничій лінії.
  4. **Генерація OTA-пакета**: до файлу `app.bin` додається структурований заголовок із магічним числом, версією прошивки, розміром та підписом CRC32/ECDSA, формуючи кінцевий артефакт оновлення `firmware_update.bin`.

### Сучасні принципи побудови на Modern CMake

- Використання генератора **Ninja** для максимальної швидкості паралельного збирання.
- Декларація властивостей через `target_compile_definitions`, `target_include_directories` та `target_link_libraries` із явним контролем видимості (`INTERFACE`, `PUBLIC`, `PRIVATE`), що виключає випадковий витік прапорців з одного модуля в інший.
- Автоматичний експорт `compile_commands.json` для інтеграції з серверами мови Clangd/LSP та лінтерами `clang-tidy`[^dou-embedded-interview].
