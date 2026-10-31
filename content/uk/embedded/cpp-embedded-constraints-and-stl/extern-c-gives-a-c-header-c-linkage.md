---
id: emb-cppstl-0015
title: "Як викликати C-код із C++ через `extern \"C\"`?"
track: embedded
section: cpp-embedded-constraints-and-stl
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
---

## Question code

```c
extern "C" {
  #include "vendor_hal.h"
  #include "freertos/task.h"
}
```

## Short answer

**`extern "C"` вмикає C linkage – без name mangling, тож лінкер знаходить C-символи.**

Без нього C++ шукав би mangled-ім’я (`_Z...`), якого в C-об’єктнику немає -> undefined reference. Багато vendor headers уже мають власний `__cplusplus`-guard; тоді додаткова обгортка не потрібна.

Правило: C API (application programming interface) має бути оголошений із C linkage, але не загортай header, якщо він уже робить це сам.[^embeddedinterviewlab]

## Detailed explanation

### Проблема декорування імен (Name Mangling) та зв’язування символів

Мова C++ підтримує перевантаження функцій (function overloading), простори імен (`namespace`) та класи з методами. Для розрізнення функцій з однаковими іменами, але різними типами аргументів, компілятор C++ використовує механізм декорування імен (Name Mangling)[^iso-cpp-n4861]. Компілятор перетворює початкове ім’я функції на унікальний символ для таблиці символів об’єктного файлу (ELF), кодуючи в ньому простір імен, клас та типи параметрів.

Наприклад, стандартна функція ініціалізації периферії:
```c
void HAL_UART_Init(UART_HandleTypeDef* huart);
```
- Компілятор C зберігає її в об’єктному файлі `stm32_hal_uart.o` під простим незмінним символом `HAL_UART_Init`.
- Компілятор C++ (відповідно до стандарту Itanium C++ ABI, що діє в `arm-none-eabi-gcc` та Clang) перетворює її на манґльоване ім’я виду `_Z13HAL_UART_InitP20UART_HandleTypeDef`.

Якщо включити C-заголовок у C++ файл без специфікації зв’язування, компілятор C++ згенерує виклик декорованого імені. Під час фінального компонування лінкер повідомить про помилку:
```text
undefined reference to `_Z13HAL_UART_InitP20UART_HandleTypeDef'
```
Лінкер не знайде такого символу, оскільки C-бібліотека містить лише недекорований символ `HAL_UART_Init`.

### Механізм специфікації зв’язування `extern "C"`

Директива `extern "C"` вказує компілятору C++, що оголошені всередині неї сутності повинні використовувати мовне зв’язування мови C (C Language Linkage)[^iso-cpp-n4861]:
1. **Вимкнення Name Mangling**: Компілятор експортує та імпортує ім’я функції в об’єктний файл точно так, як воно записане в коді (без префіксів `_Z` та суфіксів типів).
2. **Конвенція викликів (Calling Convention)**: Забезпечується сумісність розташування аргументів у регістрах та на стеку відповідно до стандарту ABI цільової платформи (наприклад, ARM Architecture Procedure Call Standard – AAPCS).

Специфікація `extern "C"` може застосовуватися:
- До окремої функції:
  ```cpp
  extern "C" void HardFault_Handler(void);
  ```
- До цілого блоку оголошень (включно з підключенням файлів заголовків):
  ```cpp
  extern "C" {
  #include "vendor_hal.h"
  #include "freertos/FreeRTOS.h"
  #include "freertos/task.h"
  }
  ```

### Практика взаємодії з vendor SDK та типові помилки

У сучасних вбудованих проєктах (STM32Cube HAL, ESP-IDF, NXP SDK, Zephyr RTOS, FreeRTOS) переважна більшість низькорівневих бібліотек написана на C. 

Правила коректного підключення:
1. **Перевірка наявності вбудованого guard**:
   Більшість якісних бібліотек уже мають внутрішній захист у своїх заголовкових файлах:
   ```c
   #ifdef __cplusplus
   extern "C" {
   #endif
   /* оголошення функцій */
   #ifdef __cplusplus
   }
   #endif
   ```
   Якщо заголовок уже містить цей препроцесорний блок, загортати `#include` у зовнішній `extern "C"` не потрібно.
2. **Заборона шаблонів всередині `extern "C"`**:
   Якщо помилково обгорнути у блок `extern "C"` заголовок, що містить конструкції C++ (шаблони функцій, класи з віртуальними методами або `namespace`), компілятор видасть помилку:
   `error: template with C linkage`[^iso-cpp-n4861]. Специфікація мовного зв’язку C забороняє генерацію сутностей, яких не існує в стандарті мови C.
3. **Обробники переривань (ISR)**:
   Векторна таблиця мікроконтролера в стартап-файлі (`startup_stm32.s`) очікує точні символьні імена функцій C (`SysTick_Handler`, `USART1_IRQHandler`). Якщо обробник переривання реалізується у файлі `.cpp`, його обов’язково слід помічати `extern "C"`, інакше процесор при виникненні переривання здійснить перехід за вектором на стандартну заглушку `Default_Handler`.
