---
id: emb-cppstl-0005
title: "Що таке `std::expected<T, E>` і чим замінити його до C++23?"
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

## Short answer

**Тип, що несе АБО значення, АБО помилку, і робить перевірку результату явною в типі.**

До C++23 пишуть власний легкий `Result<T, E>` без heap-алокації – невеликий клас із прапорцем «успіх/помилка» та union-подібним сховищем.

Правило: `expected`/`Result` поєднує значення й помилку в одному типі без винятків і без купи.[^embeddedinterviewlab]

## Detailed explanation

### Концепція std::expected у C++23

`std::expected<T, E>` – це шаблонний тип-сума (vocabulary type), стандартизований у C++23[^iso-cpp-n4861]. Він призначений для представлення результату операції, яка може завершитися або успішним поверненням корисного значення типу `T`, або помилкою типу `E`.

Він усуває головний компроміс у вбудованому C++: як повернути результат операції без використання винятків (`-fno-exceptions`) і без використання незручних вихідних параметрів (`output references`).

Внутрішня будова `std::expected`:
- Об’єкт містить нерозмічене об’єднання (`union`), у якому фізично накладаються комірки пам’яті для `T` та `E`.
- Окремий булевий прапорець (дискримінатор) вказує, який саме стан є активним у даний момент.
- Розмір об’єкта дорівнює `max(sizeof(T), sizeof(E)) + padding + sizeof(bool)` з урахуванням вимог вирівнювання типів.

### Переваги у вбудованих системах реального часу

1. **Природна семантика оператора `return`**:
   Замість передачі вихідних параметрів за посиланням функція повертає об’єкт безпосередньо:
   ```cpp
   std::expected<uint16_t, SensorError> read_adc();
   ```
2. **Гарантія відсутності використання неініціалізованих даних**:
   Неможливо отримати доступ до корисного значення `T`, доки не виконано перевірку:
   ```cpp
   auto res = read_adc();
   if (res) {
       uint16_t value = *res; // безпечний доступ
   } else {
       SensorError err = res.error(); // доступ до коду помилки
   }
   ```
3. **Підтримка функціональних ланцюжків (Monadic Operations)**:
   Методи `.and_then()`, `.or_else()`, `.transform()` дозволяють будувати конвеєри обробки без багаторівневих вкладених блоків `if`:
   ```cpp
   auto packet = read_sensor()
                     .and_then(calibrate)
                     .transform(format_packet);
   ```

### Чим замінити std::expected до C++23

Більшість промислових вбудованих проєктів наразі використовують компілятори стандартів C++14, C++17 або C++20. Для заміни застосовують перевірені рішення:

1. **Популярні header-only бібліотеки**:
   - `tl::expected` від Sy Brand – де-факто індустріальний стандарт сумісності для C++11/14/17. Бібліотека повністю повторює майбутній інтерфейс `std::expected`, підтримує монадні операції і бездоганно працює з прапорцем `-fno-exceptions` без виділення пам’яті в купі (zero-heap allocation).
2. **Власний мінімалістичний клас `Result<T, E>`**:
   У проєктах з жорсткими обмеженнями на сторонні залежності реалізують компактну структуру:
   ```cpp
   template <typename T, typename E>
   class Result {
       bool m_has_value;
       union {
           T m_val;
           E m_err;
       };
   public:
       Result(T val) : m_has_value(true), m_val(val) {}
       Result(E err) : m_has_value(false), m_err(err) {}
       ~Result() {
           // явний виклик деструктора активного члена для нетривіальних типів
       }
       explicit operator bool() const { return m_has_value; }
       const T& value() const { return m_val; }
       const E& error() const { return m_err; }
   };
   ```
3. **Стандартні класи `std::optional` та `std::variant` (починаючи з C++17)**:
   - Якщо код помилки не має значення, а важливий лише факт успіху або невдачі, застосовують `std::optional<T>`.
   - `std::variant<T, E>` здатний нести або значення, або помилку, проте робота з ним вимагає незручного синтаксису `std::holds_alternative` або `std::get_if`.

### Швидкодія на процесорах ARM Cortex-M

Якщо `T` та `E` є дрібними скалярними типами (наприклад, `uint16_t` та `enum class Error : uint8_t`), розмір усього об’єкта `std::expected` або `Result` складає 4 байти. Компілятор повертає його повністю в єдиному регістрі `r0` згідно з конвенцією AAPCS, забезпечуючи максимальну швидкодію без використання пам’яті RAM або стека.
