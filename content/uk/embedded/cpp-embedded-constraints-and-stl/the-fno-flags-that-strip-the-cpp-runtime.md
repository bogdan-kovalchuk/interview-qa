---
id: emb-cppstl-0019
title: "Які ключові прапорці компіляції для embedded C++?"
track: embedded
section: cpp-embedded-constraints-and-stl
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: gcc-cxx-dialect
    title: "GCC: C++ Dialect Options"
    url: https://gcc.gnu.org/onlinedocs/gcc/C_002b_002b-Dialect-Options.html
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
---

## Short answer

**`-fno-exceptions`, `-fno-rtti`, `-fno-threadsafe-statics`, `-fno-use-cxa-atexit`, `-fno-unwind-tables`.**

Вони прибирають: винятки, RTTI, mutex на ініціалізації static (pthread), реєстрацію dtor через `__cxa_atexit`, та `.eh_frame`-таблиці. Часто з `-Os` і `-std=c++17`.

Правило: ці прапорці роблять C++ детермінованим і компактним на голому залізі.[^embeddedinterviewlab]

## Detailed explanation

### Базовий набір прапорців C++ для bare-metal систем

За замовчуванням компілятор C++ (GCC або Clang) налаштований на розміщені (hosted) платформи з повноцінною операційною системою (POSIX, Windows), де є потоки, динамічна пам’ять та підтримка розкрутки стека (stack unwinding). У середовищі мікроконтролера (наприклад, ARM Cortex-M) без операційної системи багато з цих механізмів є непотрібними або шкідливими[^gcc-cxx-dialect].

Для отримання мінімального, детермінованого та компактного бінарного файлу застосовують спеціальний набір прапорців компіляції (`-fno-*`).

### Детальний аналіз ключових прапорців

1. **`-fno-exceptions`**:
   Повністю відключає підтримку оброблення винятків (`try`, `catch`, `throw`)[^gcc-cxx-dialect].
   - *Ефект*: усуває генерацію секцій розкрутки стека (`.ARM.extab`, `.ARM.exidx` для архітектури ARM або `.eh_frame`), що зазвичай заощаджує від 15% до 30% Flash-пам’яті.
   - *Детермінізм*: ліквідує недетермінований час виконання, пов’язаний із пошуком відповідного блоку catch під час виникнення винятку. Будь-який `throw` у користувацькому коді стає помилкою компіляції.

2. **`-fno-rtti`**:
   Вимикає генерацію метаданих типів під час виконання (Run-Time Type Information)[^gcc-cxx-dialect].
   - *Ефект*: вилучає дескриптори `std::type_info`, текстові рядки імен типів та таблиці зв’язків успадкування з Flash-пам’яті.
   - *Обмеження*: блокує використання операторів `typeid` та `dynamic_cast`. Звичайні віртуальні функції та `vtable` продовжують працювати.

3. **`-fno-threadsafe-statics`**:
   Вимикає генерацію коду блокувань навколо ініціалізації локальних статичних змінних (так званих «magic statics»)[^gcc-cxx-dialect][^itanium-cxx-abi].
   - *Ефект*: компілятор перестає викликати функції ABI `__cxa_guard_acquire` та `__cxa_guard_release`, які на багатьох платформах тягнуть залежності від бібліотеки потоків (POSIX threads) або генерують складні атомарні операції.
   - *Результат*: перевірка ініціалізації зводиться до швидкого читання одного байтового прапорця (`LDRB`/`CMP`).

4. **`-fno-use-cxa-atexit`**:
   Скасовує виклики `__cxa_atexit` для реєстрації деструкторів глобальних і статичних об’єктів[^itanium-cxx-abi].
   - *Ефект*: усуває необхідність у динамічній таблиці деструкторів у RAM та heap-виділеннях для їх реєстрації під час запуску системи. Оскільки мікроконтролер ніколи не виходить із функції `main()`, ці деструктори ніколи не виконуються.

5. **`-fno-unwind-tables` та `-fno-asynchronous-unwind-tables`**:
   Забороняють генерацію таблиць розгортання кадру викликів для налагоджувача або profiler. Економить Flash, якщо для аналізу збоїв використовується звичайний апаратний SWD/JTAG відладчик.

### Комплексна оптимізація розміру бінарного коду

Для отримання максимального ефекту разом із прапорцями `-fno-*` застосовують системні прапорці компонування:
- `-Os` (або `-Oz`): оптимізація за розміром коду;
- `-ffunction-sections` та `-fdata-sections`: розміщення кожної функції та об’єкта даних в окремих підсекціях (`.text.func`, `.rodata.data`);
- `-Wl,--gc-sections`: наказує лінкеру повністю видалити неробочий (dead code) та невикликані секції;
- `-specs=nano.specs`: підключення оптимізованої для вбудованих систем бібліотеки Newlib Nano.
