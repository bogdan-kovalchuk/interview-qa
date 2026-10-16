---
id: emb-tmplcx-0021
title: "Чому `Quantity<Tag>` не має runtime-оверхеду?"
track: embedded
section: templates-and-constexpr
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-temp-inst
    title: "C++ working draft: Implicit instantiation ([temp.inst])"
    url: https://eel.is/c++draft/temp.inst
---

## Short answer

**Tag-тип не має полів і не зберігається в об’єкті – у цьому дизайні він існує лише як аргумент шаблону.** Кожен `Quantity<Tag>` інстанціюється окремо.[^cpp-draft-temp-inst] `Quantity` містить тільки `Rep value` (напр. `int32_t`), тож розмір об’єкта визначається `Rep`, а не тегом. Правило: phantom types дають безпеку одиниць без додаткової ціни в runtime порівняно з голим `Rep`.

## Detailed explanation

Тег – це аргумент шаблону, а не член класу. `Quantity` оголошує лише `Rep value`, тож порожня структура-тег ніколи не потрапляє до даних об’єкта: вона змінює тип `Quantity<MilliampTag>`, але не його пам’ять.

Ілюстративний приклад:

```cpp
#include <cstdint>

// Illustrative: MilliampTag is an empty struct and is never stored in Quantity.
struct MilliampTag {};

template<typename Unit, typename Rep = int32_t>
struct Quantity { Rep value; };

using Milliamp = Quantity<MilliampTag>;

static_assert(sizeof(Milliamp) == sizeof(int32_t));   // holds on common ABIs
Milliamp add(Milliamp a, Milliamp b) { return {a.value + b.value}; }
```

У GCC 13 з `-O2` для x86-64 функція `add` компілюється в ту саму інструкцію `leal`, що й додавання двох `int32_t`, тобто для тега немає жодних додаткових операцій. Перевірка сумісності одиниць відбувається під час перекладу, тож у бінарнику від неї нічого не лишається.

Обмеження: кожен `Quantity<Tag>` – окремий тип, тож шаблонні функції для кожної одиниці інстанціюються окремо;[^cpp-draft-temp-inst] при багатьох одиницях це може збільшити код. Тег не змінює арифметики: `a.value + b.value` – це звичайне додавання `int32_t` з його діапазоном.

**Типові помилки:**

- Вважати, що тег захищає від переповнення діапазону: `Rep = int32_t` має той самий діапазон, що й голий `int32_t`.
- Очікувати, що phantom type сам знає коефіцієнти перетворення (мВ у В): такого перетворення в коді немає, його треба записати явно.
- Вважати, що перевірку одиниць неможливо обійти: `.value` або явна конверсія її обходять.
