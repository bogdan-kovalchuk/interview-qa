---
id: emb-tmplcx-0023
title: "Як шаблон над регістром дає compile-time захист доступу?"
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

**Шаблон може заборонити запис у read-only або читання write-only регістра – на етапі компіляції.**

Кодуючи права доступу в тип (напр. `Register<Addr, ReadOnly>`), спроба `reg.write()` для RO (read-only) стає compile error. Сирий `#define` такого не вміє.

Правило: типізована обгортка регістра ловить помилки доступу ще до запуску, на відміну від макросів.[^embeddedinterviewlab]

## Detailed explanation

### Проблема C-макросів та сирих покажчиків

У класичному C-підході (наприклад, у бібліотеках CMSIS) регістри мікроконтролера описуються макросами або структурами з нетипізованим доступом:
```c
#define USART1_ISR (*(volatile uint32_t*)(0x40013800 + 0x1C))
```
У такій моделі компілятор сприймає будь-який регістр просто як комірку `volatile uint32_t`. Програміст може випадково записати значення в read-only статусний регістр або зчитати write-only регістр даних:
- Запис у read-only регістр може призвести до мовчазного ігнорування або апаратного збою шини.
- Читання з write-only регістра може очистити апаратні прапорці периферії або повернути непередбачувані дані.
Усі ці помилки виявляються лише під час тестування на реальній платі або призводять до спорадичних збоїв у полі.

### Типізований захист через шаблони та політики доступу

У C++ права доступу до апаратного регістра можна закодувати безпосередньо в систему типів за допомогою шаблонів із Non-Type Template Parameters (NTTP) та патерну Policy-Based Design:[^iso-cpp-n4861]

```cpp
#include <cstdint>

// Теги політик доступу
struct ReadOnly {};
struct WriteOnly {};
struct ReadWrite {};

// Базовий шаблон регістра
template <uintptr_t Address, typename AccessPolicy>
class Reg;

// Спеціалізація для Read-Only: є тільки метод read()
template <uintptr_t Address>
class Reg<Address, ReadOnly> {
public:
    static uint32_t read() {
        return *reinterpret_cast<volatile uint32_t*>(Address);
    }
    // Метод write() повністю відсутній у класі
};

// Спеціалізація для Write-Only: є тільки метод write()
template <uintptr_t Address>
class Reg<Address, WriteOnly> {
public:
    static void write(uint32_t val) {
        *reinterpret_cast<volatile uint32_t*>(Address) = val;
    }
    // Метод read() повністю відсутній у класі
};

// Спеціалізація для Read-Write: доступні обидві операції
template <uintptr_t Address>
class Reg<Address, ReadWrite> {
public:
    static uint32_t read() {
        return *reinterpret_cast<volatile uint32_t*>(Address);
    }
    static void write(uint32_t val) {
        *reinterpret_cast<volatile uint32_t*>(Address) = val;
    }
};
```

### Перевірка на етапі компіляції

При спробі несанкціонованого доступу компілятор відхиляє збирання проєкту ще до формування двійкового файлу:

```cpp
using UsartIsr = Reg<0x4001381C, ReadOnly>;
using UsartTdr = Reg<0x40013828, WriteOnly>;

void test() {
    uint32_t status = UsartIsr::read(); // OK: читання дозволено
    // UsartIsr::write(0x12);            // Помилка компіляції: 'write' is not a member of 'Reg<..., ReadOnly>'
    
    UsartTdr::write(0x55);             // OK: запис дозволено
    // uint32_t x = UsartTdr::read();    // Помилка компіляції: 'read' is not a member of 'Reg<..., WriteOnly>'
}
```

Повідомлення про помилку з’являється в IDE на етапі редагування або компіляції (`fail-fast at build time`).

### Нульова вартість абстракції (Zero-Cost Abstraction)

Оскільки адреса регістра `Address` передається як NTTP константа часу компіляції, а методи оголошені як статичні `inline`, оптимізатор компілятора повністю усуває шаблонні класи. Виклик `UsartIsr::read()` розгортається в одну асемблерну інструкцію:
```assembly
LDR r0, =0x4001381C
LDR r0, [r0]
```
Ніяких об’єктів у RAM не створюється, немає викликів функцій і немає додаткових переходів за адресою.

### Типові помилки реалізації

- **Збереження адреси як поля об’єкта:** якщо передавати адресу в конструктор `Reg reg(0x4000);`, об’єкт займе 4 байти в RAM і вимагатиме непрямого читання. Адреса завжди повинна бути параметром шаблону (NTTP).
- **Забутий `volatile`:** без специфікатора `volatile` оптимізатор може закешувати значення регістра в регістрі процесора або взагалі викинути запис як непотрібний.
- **Стан гонитви при Read-Modify-Write (RMW):** для регістрів статусу, де біти очищаються записом 1 (Write 1 to clear), шаблон повинен надавати спеціалізований метод `clear_flags()`, щоб уникнути випадкового скидання сусідніх прапорців переривань.
