---
id: emb-cppstl-0017
title: "Що таке name mangling і чому через нього потрібен `extern \"C\"`?"
track: embedded
section: cpp-embedded-constraints-and-stl
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI: External Names (Mangling)"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html#mangling
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**C++ кодує сигнатуру у символ (для overload resolution): `sensor_read(uint8_t)` -> `_Z10sensor_readh`; C не мангли́ть.**

Без `extern "C"` лінкер шукатиме mangled-ім’я й не знайде немангленого C-символу -> помилка лінкування.

Правило: mangling – причина, чому міжмовний інтерфейс вимагає C linkage.[^embeddedinterviewlab]

## Detailed explanation

### Що таке name mangling і навіщо він потрібен у C++

Name mangling (декорація імен) – це механізм компілятора C++, який перетворює ідентифікатор функції або змінної на унікальний низькорівневий символ об’єктного файлу (ELF, COFF тощо), кодуючи в його текстовому імені інформацію про простір імен, належність до класу та типи параметрів[^iso-cpp-n4861].

На відміну від мови C, C++ підтримує перевантаження функцій (function overloading), простори імен (`namespace`), класи та шаблони. Наприклад, у коді можуть одночасно існувати функції з однаковим ім’ям:
```cpp
void uart_write(uint8_t byte);
void uart_write(const char* str);
```
Таблиці символів об’єктних файлів та лінкер оперують пласким адресним простором глобальних імен без урахування семантики мови програмування. Щоб лінкер міг розрізнити два різні тіла функції та пов’язати кожну точку виклику з відповідною адресою в секції `.text`, компілятор кодує сигнатуру за правилами ABI (наприклад, Itanium C++ ABI, прийнятий у GCC та Clang)[^itanium-cxx-abi]:
- `uart_write(uint8_t)` перетворюється на `_Z10uart_writeh` (префікс `_Z`, довжина імені 10, назва `uart_write`, тип `h` для `unsigned char`);
- `uart_write(const char*)` перетворюється на `_Z10uart_writePKc` (`PKc` означає pointer to `const char`).

### Причина несумісності з мовою C

У мові C перевантаження функцій відсутнє[^iso-c-n1570]. Компілятор C генерує символ, що буквально відповідає ідентифікатору у вихідному коді: функція `void uart_write(uint8_t byte);` у C-файлі транслюється в простий символ `uart_write`.

Якщо C++ файл викликає цю функцію, оголошену без додаткових вказівок, компілятор C++ автоматично застосовує name mangling і формує запит на символ `_Z10uart_writeh`. Під час збирання лінкер переглядає об’єктні файли, знаходить лише символ `uart_write`, не бачить збігу і перериває роботу з помилкою:
```text
undefined reference to 'uart_write(unsigned char)'
```

### Призначення специфікатора `extern "C"`

Конструкція `extern "C"` задає так зване C linkage (зв’язування мови C) для оголошень у C++[^iso-cpp-n4861]. Вона наказує C++ компілятору генерувати та шукати символ без декорування імен, точно так, як це робить компілятор C:
```cpp
extern "C" {
    void uart_write(uint8_t byte);
}
```
Після цього компілятор C++ генерує посилання на символ `uart_write`, і лінкер без проблем знаходить об’єктний код, скомпільований C-компілятором або написаний на чистому асемблері.

### Важливість для вбудованих систем і векторів переривань

У bare-metal розробці для мікроконтролерів (зокрема ARM Cortex-M) таблиця векторів переривань містить фіксовані імена функцій обробників (ISR), визначені в асемблерному або C-файлі стартапу: `Reset_Handler`, `SysTick_Handler`, `USART1_IRQHandler`.

Якщо визначити функцію обробника переривання у файлі `.cpp` без блоку `extern "C"`:
1. Компілятор зманглить її ім’я (наприклад, у `_Z15SysTick_Handlerv`).
2. Вектор переривання у стартап-файлі, який очікує точний символ `SysTick_Handler` зі слабким зв’язуванням (`[WEAK]`), не буде перевизначений користувацьким кодом.
3. При виникненні апаратного переривання процесор виконає стандартний порожній обробник або зависне у нескінченному циклі `Default_Handler`.
