---
id: emb-cppoop-0030
title: "Чому private-члени важливі для коректної роботи з регістрами?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-class-access
    title: "C++ working draft: Member access control, general ([class.access.general])"
    url: https://eel.is/c++draft/class.access.general
  - source_id: cpp-draft-expr-assign
    title: "C++ working draft: Assignment and compound assignment operators ([expr.assign])"
    url: https://eel.is/c++draft/expr.assign
  - source_id: tm4c123-datasheet
    title: "Tiva TM4C123GH6PM Microcontroller Data Sheet (SPMS376E)"
    url: https://www.ti.com/lit/ds/symlink/tm4c123gh6pm.pdf
---

## Short answer

**`private` не дає зовнішньому коду звертатися до регістра напряму:** `private`-член можна назвати лише в членах і friends класу, тож сирий read-modify-write ззовні через клас не виконається.[^cpp-draft-class-access] Увесь доступ іде через методи (`set`/`clear`/`read`), які в одному місці формують маску й зберігають інваріанти класу. Це захист рівня мови, а не апаратний: інший вказівник на ту саму адресу його обходить, а `|=` усередині методу – це `*odr_ = *odr_ | mask`, тобто read-modify-write,[^cpp-draft-expr-assign] і щодо ISR він не атомарний.

## Detailed explanation

Регістр периферії – спільний стан, і змінити в ньому один біт зазвичай означає read-modify-write: прочитати регістр, змінити біт, записати назад. Вираз `*reg |= mask` робить саме це, адже за стандартом `E1 op= E2` еквівалентне `E1 = E1 op E2` з одноразовим обчисленням `E1`.[^cpp-draft-expr-assign] Якщо вказівник на регістр публічний, будь-який код може записати довільну маску: затерти чужі біти, записати «сире» значення замість зміни одного біта або зіпсувати біти, які мають зберігатися. Datasheet TM4C123, наприклад, вимагає зберігати значення reserved-бітів через read-modify-write.[^tm4c123-datasheet]

`private` закриває цю дірку на рівні компіляції. Приватний член можна назвати лише в членах і friends класу, тож якщо `odr_` приватний, ззовні немає виразу, яким можна записати в регістр повз клас.[^cpp-draft-class-access] Увесь доступ іде через `set`, `clear` і `read`, а це єдине місце, де можна відкинути біти поза допустимою маскою, зберегти reserved-біти й зафіксувати порядок операцій. Інваріант класу має сенс лише тоді, коли шлях запису один.

Ілюстративний приклад:

```cpp
#include <cstdint>

class Gpio {
public:
  explicit Gpio(volatile std::uint32_t *odr) : odr_{odr} {}
  void set(std::uint32_t mask)   { *odr_ |= mask; }
  void clear(std::uint32_t mask) { *odr_ &= ~mask; }
  std::uint32_t read() const     { return *odr_; }

private:
  volatile std::uint32_t *odr_;
};

void use(Gpio &g) {
  g.set(1u << 5);
  // *g.odr_ = 0;  // помилка компіляції: odr_ є private
}
```

Межі в цього захисту такі. По-перше, це контроль доступу на рівні мови, а не апаратний: `friend` має доступ до приватних членів,[^cpp-draft-class-access] а інший вказівник на ту саму адресу чи `reinterpret_cast` узагалі не проходять через клас. По-друге, `private` не робить read-modify-write атомарним: якщо ISR змінить той самий регістр між читанням і записом у методі, її зміну буде загублено. Розв’язки – критична секція або регістри, які дозволяють змінити біт без читання. Наприклад, у TM4C123 GPIODATA приймає маску в бітах [9:2] адреси, тож окремі піни змінюються одним записом, без read-modify-write.[^tm4c123-datasheet] Клас-обгортка може сховати таку специфіку за тим самим інтерфейсом `set`/`clear`.

**Типові помилки:**

- Додати getter, що повертає сирий вказівник на регістр: інкапсуляція втрачена.
- Вважати `private` апаратним захистом або захистом від ISR чи DMA.
- Реалізувати `set` як `*odr_ = mask` замість зміни одного біта: решта біт регістра затирається.
- Лишити `set`/`clear` без перевірки маски: приватність сама по собі некоректні значення не відсіває.
