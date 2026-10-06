---
id: emb-cppoop-0035
title: "Чи можна вибрати поліморфізм без RAM-оверхеду на vptr?"
description: "Так – CRTP (Curiously Recurring Template Pattern, compile-time) або просто templates/композиція."
track: embedded
section: cpp-classes-and-oop
level: junior
type: concept
tags: []
status: published
updated: 2026-10-06
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
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-06; це джерело не є доказом тверджень."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C++; freestanding і вендорські тулчейни можуть відрізнятися."
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
    accessed: 2026-10-06
    kind: spec
    version: null
    applicability: "Визначає dynamic class (з virtual-функціями чи virtual-базами) як клас, що потребує virtual table pointer; отже клас без них його не потребує; vtable описано як таблицю на клас. У правилах розміщення (розділ 2.4) для порожнього базового класу спершу пробує offset zero. Це ABI, а не стандарт мови: інші ABI можуть відрізнятися в деталях."
  - source_id: cpp-draft-expr-static-cast
    title: "C++ working draft: Static cast ([expr.static.cast])"
    url: https://eel.is/c++draft/expr.static.cast
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Визначає, що static_cast вказівника на base у вказівник на похідний клас коректний, лише якщо цей base справді є підоб’єктом об’єкта похідного типу; інакше undefined behavior. Компілятор цього не перевіряє."
  - source_id: cpp-draft-temp-inst
    title: "C++ working draft: Implicit instantiation ([temp.inst])"
    url: https://eel.is/c++draft/temp.inst
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що неявна інстанціація специфікації класового шаблону інстанціює оголошення, але не визначення member-функцій, а специфікація member-функції інстанціюється, коли її визначення потрібне. Про розмір коду не йдеться."
  - source_id: cpp-draft-intro-object
    title: "C++ working draft: Object model ([intro.object])"
    url: https://eel.is/c++draft/intro.object
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що об’єкт класу з virtual-функціями чи virtual-базами має ненульовий розмір, а базовий підоб’єкт standard-layout класу без нестатичних даних – нульовий; в інших випадках нульовий розмір – implementation-defined. Конкретний розмір sizeof залежить від ABI."
---

## Short answer

**Так – CRTP (Curiously Recurring Template Pattern, compile-time) або просто templates/композиція.**

CRTP-база не має virtual-функцій, тож це не dynamic class і vptr не потрібен;[^itanium-cxx-abi] її `static_cast` до похідного типу коректний, лише якщо об’єкт справді має тип `D`.[^cpp-draft-expr-static-cast] Ціна: набір типів фіксується на етапі компіляції, а код бази інстанціюється для кожного `D`.[^cpp-draft-temp-inst]

Правило: поліморфізм над типами, відомими на етапі компіляції, де vptr × багато об’єктів забагато за RAM -> CRTP чи templates, а не virtual.

## Detailed explanation

Ціна virtual по RAM така: клас із virtual-функціями (dynamic class) потребує virtual table pointer, тож кожен його об’єкт містить vptr, а vtable одна на клас (див. `qid:emb-cppoop-0013`).[^itanium-cxx-abi] На 32-bit Arm вказівник зазвичай займає 4 байти: 100 однакових об’єктів датчиків дають 400 B RAM лише на vptr, а на MCU з 4 KB RAM це майже 10 %. Для кількох об’єктів це дрібниця, тож питання варто ставити, коли об’єктів багато або RAM дуже мало.

Поліморфізм без vptr можна отримати двома способами. Перший – CRTP: `SensorBase<D>` не має virtual-функцій і викликає реалізацію похідного класу через `static_cast<D*>(this)->read_impl()`. Це не dynamic class, тож vptr не потрібен,[^itanium-cxx-abi] а компілятор бачить цільову функцію й може її інлайнити (див. `qid:emb-cppoop-0020`). `static_cast` від бази до похідного класу коректний, лише якщо ця база справді є підоб’єктом об’єкта типу `D`; інакше це undefined behavior.[^cpp-draft-expr-static-cast] Другий спосіб – звичайні templates: функція чи клас приймає будь-який тип із потрібними методами, без спільної бази взагалі, а «композиція» тут означає, що клас тримає такий компонент як член чи template-параметр.

Порожня CRTP-база розміру не додає: стандарт допускає нульовий розмір базового підоб’єкта без даних,[^cpp-draft-intro-object] а Itanium ABI для порожньої бази спершу пробує offset zero.[^itanium-cxx-abi] Тому `sizeof(Temp)` у прикладі дорівнює розміру власних даних, тоді як з virtual до нього додався б vptr. Це не стосується бази, у якій є дані.

CRTP не універсальний: вибір типу відбувається на етапі компіляції, тож `SensorBase<Temp>` і `SensorBase<Pressure>` – різні класи без спільної бази: їх не покласти в один масив і не передати як один `SensorBase&`. Якщо тип обирається в runtime (за конфігурацією чи протоколом), потрібен virtual (див. `qid:emb-cppoop-0021`). До того ж кожна специфікація шаблону інстанціюється окремо,[^cpp-draft-temp-inst] тож код методів бази дублюється для кожного `D` (див. `qid:emb-cppoop-0022`): CRTP міняє RAM на об’єкт на ROM на тип. Виграш там, де об’єктів багато, а типів мало; для небагатьох об’єктів багатьох різних типів може бути гірше, тож перевіряй map file.

```cpp
#include <cstdint>

// Ілюстративно.
template <typename D>
class SensorBase {                       // без virtual і без даних
public:
    std::int16_t read() { return static_cast<D*>(this)->read_impl(); }
};

class Temp final : public SensorBase<Temp> {
    friend class SensorBase<Temp>;       // база викликає приватний read_impl
    std::int16_t read_impl() { return last_; }
    std::int16_t last_ = 0;
};
// Порожня база не збільшує об’єкт (так на GCC/Clang за Itanium ABI).
static_assert(sizeof(Temp) == sizeof(std::int16_t));

template <typename S>                    // templates: будь-який тип з методом read()
std::int16_t poll(S& s) { return s.read(); }
```

**Типові помилки:**

- Вважати CRTP повною заміною virtual: коли тип відомий лише в runtime, спільного base немає, і потрібен virtual.
- Не рахувати ROM: кожен `D` дає власні копії методів бази.[^cpp-draft-temp-inst]
- Успадкувати від `SensorBase<Інший>`: `static_cast` на неправильний тип – undefined behavior.[^cpp-draft-expr-static-cast]
- Додати дані в CRTP-базу й чекати, що вона лишиться «безкоштовною»: порожньою базою вона більше не є, і розмір об’єкта зросте.

## Sources

<!-- generated from frontmatter -->
