---
id: emb-raii-0033
title: "Що має сказати кандидат про важливість RAII в embedded?"
track: embedded
section: raii-and-smart-pointers
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cppcg-r1-raii
    title: "C++ Core Guidelines: R.1 – Manage resources automatically using resource handles and RAII"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r1-manage-resources-automatically-using-resource-handles-and-raii-resource-acquisition-is-initialization
  - source_id: cpp-draft-stmt-jump
    title: "C++ working draft: Jump statements ([stmt.jump])"
    url: https://eel.is/c++draft/stmt.jump
  - source_id: cpp-draft-class-temporary
    title: "C++ working draft: Temporary objects ([class.temporary])"
    url: https://eel.is/c++draft/class.temporary
---

## Short answer

**Структура відповіді: принцип -> embedded-наслідок -> гарантія компілятора.**

Принцип: ctor бере ресурс, dtor його віддає.[^cppcg-r1-raii] Наслідок: немає OS, яка звільнить ресурси за тебе, тож leak або deadlock може лишитися до reset. Гарантія: dtor локального об’єкта викликається на кожному виході зі scope, включно з early return, крім завершення програми через `exit` чи `abort`.[^cpp-draft-stmt-jump]

Правило: підкреслюй, що RAII прибирає клас людських помилок, а не додає можливостей.[^embeddedinterviewlab]

## Detailed explanation

RAII (Resource Acquisition Is Initialization) прив’язує ресурс до часу життя об’єкта: конструктор захоплює ресурс, деструктор його звільняє.[^cppcg-r1-raii] Для локального об’єкта компілятор викликає деструктор при виході з scope незалежно від того, як цей вихід стався: через `return`, `break` чи кінець блоку.[^cpp-draft-stmt-jump] Тому звільнення більше не залежить від того, чи програміст пам’ятає кожен шлях.

В embedded ресурсом може бути не лише пам’ять, а й mutex, critical section, SPI-транзакція, DMA-канал чи живлення периферії. Без RAII типова помилка – ранній `return` в обробнику помилки, який минає `deinit()`: переривання лишаються вимкненими або канал зайнятим. Операційної системи, яка повернула б ресурси, немає, і єдиний спосіб відновитися – reset. Приклад з критичною секцією: деструктор відновлює попередній стан переривань на обох `return`.

```cpp
#include <cstdint>

// Illustrative: on a Cortex-M these wrap reads and writes of PRIMASK.
uint32_t enter_critical();          // disables IRQs, returns previous state
void exit_critical(uint32_t prev);  // restores previous state

class CriticalSection {
public:
  CriticalSection() : prev_(enter_critical()) {}
  ~CriticalSection() { exit_critical(prev_); }
  CriticalSection(const CriticalSection&) = delete;
  CriticalSection& operator=(const CriticalSection&) = delete;
private:
  uint32_t prev_;
};

int read_pair(const volatile int* src, int* out) {
  CriticalSection cs;
  if (src == nullptr) return -1;   // destructor runs here
  *out = *src;
  return 0;                        // and here
}
```

Межі гарантії: вона стосується локальних об’єктів, що виходять зі свого scope. Об’єкт, створений через `new` без власника, сам не звільниться. Локальні об’єкти не знищуються, коли програма завершується через `exit` чи `abort`, а reset MCU тим більше не викликає жодного деструктора.[^cpp-draft-stmt-jump] Тимчасовий об’єкт – окрема пастка: `CriticalSection{};` знищується в кінці повного виразу,[^cpp-draft-class-temporary] і код після нього вже виконується без захисту.

**Типові помилки:**

- Писати `CriticalSection{};` замість `CriticalSection cs;`: тимчасовий об’єкт знищується одразу.
- Вважати, що dtor спрацює після `exit()`, `abort()` або reset.
- Покладатися на ручний виклик `deinit()` у кожному `return`: саме це дисциплінарна проблема, яку RAII прибирає.
