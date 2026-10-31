---
id: emb-tmplcx-0029
title: "Як constexpr дає compile-time bounds checking?"
track: embedded
section: templates-and-constexpr
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
---

## Short answer

**Коли розмір – NTTP, індекси/межі можна перевірити `static_assert`-ом на етапі компіляції.**

Напр. `get<I>()` з `static_assert(I < N, "out of range")` зробить вихід за межі compile error, а не runtime-багом.

Правило: переноси перевірку меж у compile time скрізь, де індекс/розмір відомі статично.[^embeddedinterviewlab]

## Detailed explanation

### Механізм: NTTP та `static_assert`

У класичному C перевірка меж масивів або відсутня (що породжує фатальні помилки buffer overflow), або виконується під час роботи програми через runtime `if (index >= SIZE)`. У вбудованих системах другий варіант збільшує розмір прошивки (Flash) і сповільнює обробку в критичних секціях або перериваннях.

Якщо розмір буфера та індекс доступу відомі на етапі трансляції, у C++ їх можна передати як параметри шаблону, що не є типами (Non-Type Template Parameters, NTTP).[^iso-cpp-n4861] Це дає змогу виконати перевірку через `static_assert`:

```cpp
#include <cstddef>

template <typename T, std::size_t N>
class StaticArray {
    T data_[N];
public:
    // Доступ за індексом, відомим під час компіляції
    template <std::size_t Index>
    constexpr const T& get() const {
        static_assert(Index < N, "StaticArray: Compile-time index out of bounds!");
        return data_[Index];
    }

    template <std::size_t Index>
    constexpr T& get() {
        static_assert(Index < N, "StaticArray: Compile-time index out of bounds!");
        return data_[Index];
    }
};
```

При спробі звернутися за межі допустимого діапазону:
```cpp
StaticArray<int, 4> sensors;
int val = sensors.get<5>(); // Помилка компіляції: static_assert failed "Compile-time index out of bounds!"
```
код взагалі не скомпілюється. Баг відловлюється до завантаження у мікроконтролер.

### Застосування у стандартній бібліотеці

Цей патерн є основою функції `std::get<I>(arr)` для стандартного контейнера `std::array` та кортежів `std::tuple` (згідно зі стандартом ISO/IEC 14882, `[array.element]`).[^iso-cpp-n4861]

Крім того, у C++14/C++17 самі функції можуть бути оголошені як `constexpr`, перевіряючи коректність індексів під час обчислення виразів:
```cpp
constexpr int get_calibrated_value(int channel) {
    constexpr int limits[] = { 10, 20, 30 };
    if (channel < 0 || channel >= 3) {
        // У constexpr контексті викидання винятку або виклик помилкової функції
        // зупиняє компіляцію з детальною діагностикою
        throw "Channel out of range"; 
    }
    return limits[channel];
}

constexpr int ch = get_calibrated_value(1); // OK
// constexpr int bad = get_calibrated_value(5); // Помилка компіляції під час обчислення константи
```

### Валідація апаратних конфігурацій без коду у Flash

В embedded-проєктах багато параметрів прив’язані до конкретної схеми підключення: номери каналів АЦП, пріоритети переривань NVIC (від 0 до 15 у Cortex-M), подільники частоти таймерів. Використання `constexpr` валідаторів усуває потребу в коді обробки помилок у самій прошивці:

```cpp
constexpr bool is_valid_nvic_priority(uint32_t prio) {
    return prio <= 15;
}

template <uint32_t IrqNum, uint32_t Priority>
void configure_interrupt() {
    static_assert(is_valid_nvic_priority(Priority), "NVIC priority must be in range 0..15");
    // Безпосереднє налаштування регістрів без зайвих перевірок у runtime
}
```

### Переваги для систем реального часу

1. **Нульовий оверхед у бінарнику:** скомпільований код не містить жодної інструкції порівняння чи умовного переходу (`CMP`, `BHI`).
2. **Гарантія безпеки пам’яті:** виключається ймовірність пошкодження пам’яті або спрацьовування MPU через помилковий індекс.
3. **Економія пам’яті рядків:** немає потреби зберігати рядки повідомлень assert у flash-пам’яті мікроконтролера.

### Типові помилки та обмеження

- **Спроба передати динамічну змінну в NTTP:** індекс для `get<Index>()` повинен бути константним виразом часу компіляції (`constexpr`). Якщо індекс приходить по UART у runtime, слід використовувати звичайну функцію перевірки меж поверненням `std::optional` або коду помилки.
- **Ігнорування signed/unsigned різниці:** перевірка `Index < N` для знакових типів вимагає додаткової перевірки `Index >= 0`, щоб уникнути неявного перетворення від’ємних чисел у великі беззнакові значення.
