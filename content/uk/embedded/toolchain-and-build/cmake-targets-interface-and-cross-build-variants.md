---
id: emb-build-0021
title: "Як CMake може описувати залежності, targets, interface include dirs і cross-platform build variants?"
track: embedded
section: toolchain-and-build
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gcc-overall-options
    title: "GCC manual: Options Controlling the Kind of Output"
    url: https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html
---

## Short answer

У CMake кожна library/application має бути **target** з власними sources, compile definitions, include dirs і link dependencies. `target_include_directories(... INTERFACE)` публікує headers для consumers, а `PRIVATE` лишає їх локальними. Cross-build variants задають toolchain file, presets, target-specific options і окремі targets для MCU, host tests та utilities.[^dou-embedded-interview]

## Detailed explanation

### Цільова модель сучасного CMake (Modern Target-Based CMake)

Застарілі практики CMake спиралися на глобальні команди `include_directories()`, `add_definitions()` та `link_libraries()`. У великих проєктах вбудованого ПЗ це призводило до неконтрольованого протікання шляхів пошуку заголовків і конфліктів макросів між ядром операційної системи (RTOS), апаратними бібліотеками (HAL) та прикладним кодом.

Сучасний підхід базується на концепції тарґетів (targets) – окремих ізольованих модулів, створених через `add_library()` або `add_executable()`. Кожен тарґет інкапсулює власні вихідні файли, правила компіляції та залежності, передаючи їх іншим компонентам виключно через явно визначені інтерфейси.

### Модифікатори видимості: PRIVATE, INTERFACE та PUBLIC

Під час налаштування властивостей тарґета (директиви `target_include_directories`, `target_compile_definitions`, `target_compile_options`) область видимості визначає транзитивність вимог використання (usage requirements):

```cmake
add_library(bme280_driver STATIC
    src/bme280.c
    src/bme280_math.c
)

target_include_directories(bme280_driver
    PUBLIC  ${CMAKE_CURRENT_SOURCE_DIR}/include
    PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/src
)

target_link_libraries(bme280_driver
    PUBLIC  hal_i2c
    PRIVATE c_runtime_utils
)
```

1. **PRIVATE**: властивість необхідна лише для збирання самого тарґета. Внутрішні заголовки в папці `src/` або внутрішні утиліти `c_runtime_utils` не потраплять до простору імен інших модулів, які лінкують `bme280_driver`.
2. **INTERFACE**: властивість не потрібна для збирання самого тарґета (типово для header-only бібліотек або абстрактних конфігураційних інтерфейсів), але вона примусово застосовується до кожного тарґета, що лінкує цей компонент через `target_link_libraries()`.
3. **PUBLIC**: комбінація двох попередніх. Каталог `include/` із заголовком `bme280.h` використовується для компіляції самого драйвера і автоматично додається в include-path споживачів драйвера.

### Крос-компіляція за допомогою Toolchain Files

Для збирання бінарного коду під цільову архітектуру (Target MCU) параметри цільової системи виносять в окремий файл тулчейна (наприклад, `arm-none-eabi.cmake`), який передається аргументом `-DCMAKE_TOOLCHAIN_FILE=...` або конфігурується у `CMakePresets.json`:

```cmake
set(CMAKE_SYSTEM_NAME Generic)
set(CMAKE_SYSTEM_PROCESSOR arm)

set(CMAKE_C_COMPILER   arm-none-eabi-gcc)
set(CMAKE_CXX_COMPILER arm-none-eabi-g++)
set(CMAKE_ASM_COMPILER arm-none-eabi-gcc)

# Запобігає падінню CMake при лінкуванні тестових програм для bare-metal
set(CMAKE_TRY_COMPILE_TARGET_TYPE STATIC_LIBRARY)
```

Вказівка `CMAKE_SYSTEM_NAME Generic` повідомляє генератору, що складання виконується для bare-metal платформи без стандартної ОС. Апаратні параметри ядра мікроконтролера (`-mcpu=cortex-m4`, `-mthumb`, `-mfpu=fpv4-sp-d16`, `-mfloat-abi=hard` згідно з документацією GCC [^gcc-overall-options]) зручно оформити як інтерфейсний тарґет (interface target):

```cmake
add_library(mcu_cortex_m4 INTERFACE)
target_compile_options(mcu_cortex_m4 INTERFACE
    -mcpu=cortex-m4 -mthumb -mfpu=fpv4-sp-d16 -mfloat-abi=hard
)
target_link_options(mcu_cortex_m4 INTERFACE
    -mcpu=cortex-m4 -mthumb -mfpu=fpv4-sp-d16 -mfloat-abi=hard
    -T${CMAKE_CURRENT_SOURCE_DIR}/linker/STM32F407VG.ld
    -Wl,--gc-sections
)
```

### Підтримка крос-платформних варіантів: Firmware vs Host Unit Tests

Тарґетна архітектура дозволяє паралельно підтримувати кілька варіантів збирання в одному репозиторії:
- **Цільовий образ прошивки (MCU Target)**: використовує крос-компілятор, підключає скрипти лінкера, вектори переривань і генерує артефакти `.elf`, `.hex`, `.bin`.
- **Хостові модульні тести (Host Unit Tests)**: алгоритмічні бібліотеки (фільтри, криптографія, черги, розбір бінарних протоколів) не прив’язані до апаратного заліза і лінкуються з тестовими фреймворками (GoogleTest, Unity, Catch2) під нативний компілятор комп’ютера розробника (x86_64 GCC чи Clang). Апаратні виклики периферії замінюються моками (mock objects).

Таке розмежування забезпечує швидкий запуск тестів у хмарних CI-системах без необхідності використання емуляторів або фізичних платформ[^dou-embedded-interview].

