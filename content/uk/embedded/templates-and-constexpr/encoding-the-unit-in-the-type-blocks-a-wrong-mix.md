---
id: emb-tmplcx-0020
title: "Як шаблони дають type-safe фізичні одиниці?"
description: "Одиниця закодована в тип – неявне змішування несумісних величин дає помилку компіляції."
track: embedded
section: templates-and-constexpr
level: junior
type: mechanism
tags: []
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 3
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-13; це джерело не є доказом тверджень."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C++; freestanding і вендорські тулчейни можуть відрізнятися."
  - source_id: cpp-core-guidelines-i4
    title: "C++ Core Guidelines: I.4 (make interfaces precisely and strongly typed)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#i4-make-interfaces-precisely-and-strongly-typed
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Приклад change_speed(Speed) відхиляє значення без одиниці (error: no unit); це рекомендація проєктування, а не поведінка конкретного компілятора."
  - source_id: cpp-draft-temp-inst
    title: "C++ working draft: Implicit instantiation ([temp.inst])"
    url: https://eel.is/c++draft/temp.inst
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Визначає, коли шаблон функції чи класу неявно інстанціюється: коли на нього посилаються в контексті, що вимагає визначення. Не визначає розмір бінарника чи розміщення коду."
---

## Question code

```cpp
template<typename Unit, typename Rep = int32_t>
struct Quantity { Rep value; };
using Millivolt = Quantity<MillivoltTag>;
using Milliamp  = Quantity<MilliampTag>;
```

## Short answer

**Одиниця закодована в тип – неявно змішати несумісні величини не можна (помилка компіляції).** `set_led_current(read_battery())` не скомпілюється, бо `Millivolt` і `Milliamp` – різні типи без неявного перетворення. `Quantity` зберігає лише `Rep value`, тож tag-тип не займає місця в об’єкті. Правило: інтерфейс з одиницею в типі відхиляє значення без одиниці вже на етапі компіляції.[^cpp-core-guidelines-i4]

## Detailed explanation

Одиниця стає частиною типу: `Quantity<MillivoltTag>` і `Quantity<MilliampTag>` – різні специалізації одного шаблону, тож функція, що приймає `Milliamp`, не прийме `Millivolt`. Core Guidelines (I.4) показує ту саму ідею: `change_speed(2.3)` без одиниці має бути помилкою, якщо параметр має тип `Speed`.[^cpp-core-guidelines-i4]

Ілюстративний приклад (рядок з `read_battery()` закоментовано, бо він не компілюється):

```cpp
#include <cstdint>

// Illustrative: tag types carry no data and are never stored in Quantity.
struct MillivoltTag {};
struct MilliampTag {};

template<typename Unit, typename Rep = int32_t>
struct Quantity { Rep value; };

using Millivolt = Quantity<MillivoltTag>;
using Milliamp  = Quantity<MilliampTag>;

void set_led_current(Milliamp);
Millivolt read_battery();

void f() {
    set_led_current(Milliamp{120});    // OK: aggregate initialization of value
    // set_led_current(read_battery()); // compile error: no conversion Millivolt -> Milliamp
}
```

Тег не зберігається: `Quantity` містить лише `Rep value`, тож тип-тег не додає полів. На звичайних ABI `sizeof(Milliamp)` дорівнює `sizeof(int32_t)`; це можна зафіксувати `static_assert` на цільовій платформі.

Тег не додає витрат і в згенерованому коді. Функція `Milliamp add(Milliamp a, Milliamp b) { return {a.value + b.value}; }` у GCC 13 з `-O2` для x86-64 компілюється в ту саму інструкцію `leal`, що й додавання двох `int32_t`. У цьому прикладі безпека одиниць не коштує нічого під час виконання порівняно з голим `int32_t`.

Обмеження: кожен `Quantity<Tag>` – окрема специалізація, тож шаблонні функції інстанціюються окремо для кожної одиниці;[^cpp-draft-temp-inst] при багатьох одиницях це може збільшити код. Перетворення між одиницями (наприклад, мВ у В) треба писати явно, а `.value` дає прямий доступ до числа й обходить перевірку.

**Типові помилки:**

- Передавати одиниці як голий `int32_t` або `double`: тип тоді нічого не перевіряє, а саме цю помилку радить усувати I.4.[^cpp-core-guidelines-i4]
- Вважати, що тег захищає від переповнення: `Rep = int32_t` має той самий діапазон, що й голий `int32_t`.
- Очікувати, що phantom type знає коефіцієнти перетворення (мВ у В): такого перетворення в коді немає, його треба записати явно.

## Sources

<!-- generated from frontmatter -->
