---
id: emb-cppstl-0028
title: "Як замінити `std::map` без heap?"
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

**Відсортований `std::array` пар + binary search (`std::lower_bound`).**

`std::map` алокує вузли в купі на кожну вставку. Якщо набір ключів відомий на етапі компіляції, `constexpr` відсортований масив дає O(log n) пошук без жодної алокації.

Правило: статичні lookup-таблиці – sorted `array` + binary search замість `map`.[^embeddedinterviewlab]

## Detailed explanation

### Чому `std::map` неприйнятний у bare-metal прошивках

Контейнер `std::map` у стандартній бібліотеці C++ реалізовано як збалансоване червоно-чорне дерево пошуку (Red-Black tree)[^iso-cpp-n4861]. Така структура має фундаментальні недоліки для систем із жорсткими ресурсами:
- **Динамічне виділення пам’яті (Heap overhead)**: кожен окремий елемент дерева зберігається у вузлі (`Node`), який виділяється через `operator new` або налаштований алокатор. Це спричиняє фрагментацію оперативної пам’яті (RAM) та недетермінований час вставки.
- **Накладні витрати пам’яті на покажчики**: кожен вузол дерева зобов’язаний зберігати три покажчики (`parent`, `left`, `right`), колір вузла та вирівнювання (padding). На 32-бітній архітектурі ARM Cortex-M це додає щонайменше 16 байтів службових даних на кожен елемент поверх корисного навантаження.
- **Погана локальність даних (Cache / Prefetch unfriendly)**: вузли дерева розкидані по різних адресах купи. На мікроконтролерах із Flash-акселераторами (наприклад, ART Accelerator у STM32) або кешем інструкцій/даних стрибки за випадковими покажчиками призводять до постійних промахів кешу та простою конвеєра процесора.

### Патерн Flat Map: відсортований масив і двійковий пошук

Якщо набір ключів фіксований або відомий на етапі збирання (наприклад, таблиця команд AT-парсера, конфігурація регістрів датчика або відповідність ID повідомлень CAN їхнім обробникам), `std::map` замінюють структурою «плоского словника» (Flat Map):
1. **Зберігання**: послідовний масив пар `std::array<std::pair<Key, Value>, N>`, розташований у неперервному блоці пам’яті.
2. **Пошук**: алгоритм `std::lower_bound` зі стандартного заголовка `<algorithm>`, що забезпечує часову складність O(log N) за допомогою двійкового пошуку (binary search)[^iso-cpp-n4861].

Завдяки послідовному розташуванню елементів у пам’яті prefetch-буфер процесора завчасно підтягує сусідні елементи, що робить бінарний пошук по невеликому масиву (до кількох сотень елементів) навіть швидшим за обхід дерева.

### Розміщення у Flash через constexpr

Найбільша інженерна перевага відсортованого масиву – можливість повної ініціалізації та сортування під час компіляції:
```cpp
#include <array>
#include <algorithm>
#include <string_view>

struct CommandEntry {
    std::string_view name;
    void (*handler)();
};

constexpr std::array<CommandEntry, 3> command_table = {{
    {"reboot", &handle_reboot},
    {"status", &handle_status},
    {"version", &handle_version}
}};

const CommandEntry* find_command(std::string_view cmd) {
    auto it = std::lower_bound(
        command_table.begin(), command_table.end(), cmd,
        [](const CommandEntry& entry, std::string_view val) {
            return entry.name < val;
        }
    );
    if (it != command_table.end() && it->name == cmd) {
        return &(*it);
    }
    return nullptr;
}
```
Оголошення таблиці як `constexpr` або `const` гарантує, що компілятор помістить її в секцію `.rodata` пам’яті Flash. Таблиця споживає рівно **0 байтів RAM** і не потребує жодного коду ініціалізації під час запуску мікроконтролера.

### Динамічні сценарії: C++23 std::flat_map та Embedded Template Library

Якщо таблиця формується динамічно під час запуску пристрою, але без виділення купи, застосовують такі рішення:
- **C++23 `std::flat_map`**: стандартний адаптер контейнерів, побудований на двох паралельних послідовних контейнерах (для ключів та значень).
- **Embedded Template Library (ETL)**: класи `etl::flat_map<Key, Value, MAX_SIZE>`, які виділяють фіксований буфер пам’яті всередині об’єкта (на стеку або статично в `.bss`), запобігаючи виходу за межі пам’яті та динамічним алокаціям.
