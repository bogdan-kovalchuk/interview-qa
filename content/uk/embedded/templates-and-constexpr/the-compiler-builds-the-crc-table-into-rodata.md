---
id: emb-tmplcx-0006
title: "Як згенерувати CRC-32 (cyclic redundancy check) таблицю на етапі компіляції?"
track: embedded
section: templates-and-constexpr
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-dcl-constexpr
    title: "C++ working draft: The constexpr specifier ([dcl.constexpr])"
    url: https://eel.is/c++draft/dcl.constexpr
  - source_id: cpp-draft-basic-start-static
    title: "C++ working draft: Static initialization ([basic.start.static])"
    url: https://eel.is/c++draft/basic.start.static
---

## Question code

```cpp
constexpr auto make_crc_table() {
  std::array<uint32_t, 256> t{};
  for (uint32_t i = 0; i < 256; ++i)
    t[i] = crc32_for_byte(i);
  return t;
}
constexpr auto crc_table = make_crc_table();
```

## Short answer

**Таблиця CRC-32 на 256 записів `uint32_t` (1 КБ) обчислюється компілятором, якщо функція для одного байта і функція побудови таблиці є `constexpr`.**

Constexpr-змінна мусить бути constant-initializable,[^cpp-draft-dcl-constexpr] тож таблиця ініціалізується константно, і жоден цикл при старті її не заповнює.[^cpp-draft-basic-start-static]

Правило: великі незмінні таблиці (наприклад, CRC) генеруй через `constexpr`, а не рахуй при старті.

## Detailed explanation

Таблиця CRC-32 має 256 записів: для кожного байта `i` функція вісім разів зсуває значення на один біт і, якщо молодший біт був одиницею, виконує XOR із поліномом, записаним у коді. Щоб уся таблиця обчислювалась під час збирання, `crc32_for_byte` і `make_crc_table` мають бути `constexpr`. Тоді `constexpr auto crc_table = make_crc_table();` є константним ініціалізатором, і компілятор мусить обчислити його під час збирання.[^cpp-draft-dcl-constexpr]

Ілюстративний приклад, який компілюється як C++17:

```cpp
#include <array>
#include <cstdint>

constexpr std::uint32_t crc32_for_byte(std::uint32_t r) {
  for (int j = 0; j < 8; ++j)
    r = (r & 1u) ? (r >> 1) ^ 0xEDB88320u : (r >> 1);
  return r;
}

constexpr std::array<std::uint32_t, 256> make_crc_table() {
  std::array<std::uint32_t, 256> t{};
  for (std::uint32_t i = 0; i < 256; ++i)
    t[i] = crc32_for_byte(i);
  return t;
}

constexpr auto crc_table = make_crc_table();
static_assert(crc_table[1] == 0x77073096u, "table built at compile time");
static_assert(sizeof(crc_table) == 1024, "256 x 4 bytes");
```

`static_assert` на `crc_table[1]` перевіряє значення під час збирання; другий фіксує розмір 1024 байти. Якщо `make_crc_table` викличе не-constexpr функцію, збирання зупиниться з помилкою. Сама змінна `crc_table` має static storage duration і constant initialization, тож для неї немає динамічної ініціалізації під час запуску.[^cpp-draft-basic-start-static] Розміщення в пам’яті (read-only дані чи RAM) визначають компілятор і скрипт лінкера цільової плати, а не сам `constexpr`.

**Типові помилки:**

- Оголосити таблицю звичайною змінною і заповнювати її в `main` або `init()`: тоді цикл виконується при кожному запуску.
- Викликати в `make_crc_table` функцію, яка не є `constexpr` (наприклад, з I/O): збирання зупиниться з помилкою.
- Вважати, що `constexpr` сам кладе таблицю у Flash: місце в пам’яті задають ціль і скрипт лінкера.
