---
id: emb-cppoop-0027
title: "Чи є оверхед від virtual-функцій, якщо клас узагалі їх не має?"
description: "Ні – без virtual-функцій і virtual-баз клас не має ні vtable, ні vptr."
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
  - source_id: cpp-draft-expr-sizeof
    title: "C++ working draft: [expr.sizeof] Sizeof"
    url: https://eel.is/c++draft/expr.sizeof
    accessed: 2026-10-06
    kind: spec
    version: "working draft"
    applicability: "Каже, що для класу sizeof дає кількість байтів в об’єкті цього класу разом із padding, потрібним для розміщення таких об’єктів у масиві, і що кількість та розташування padding визначає реалізація. Конкретних значень не дає."
  - source_id: iso-tr-18015
    title: "ISO/IEC TR 18015:2006 Technical Report on C++ Performance"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/TR18015.pdf
    accessed: 2026-10-06
    kind: spec
    version: "TR 18015:2006"
    applicability: "У розділі 5.3.1 каже, що клас без virtual-функції потребує стільки ж місця, скільки struct з тими самими полями (поза можливим padding), non-virtual функція місця в об’єкті не займає, а поліморфний клас платить одним вказівником на об’єкт плюс таблицею на клас. У 5.3.6: virtual base додає накладні порівняно зі звичайною базою (позиція підоб’єкта динамічна, зазвичай через вказівник). Звіт 2006 року: розміри залежать від реалізації."
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
    accessed: 2026-10-06
    kind: spec
    version: null
    applicability: "Визначає dynamic class (з virtual-функціями чи virtual-базами, власними або успадкованими) як клас, що потребує virtual table pointer; отже клас без них його не має. Це ABI, а не стандарт мови: інші ABI можуть відрізнятися в деталях."
---

## Short answer

**Ні – клас, у якого немає (і який не успадковує) ні virtual-функцій, ні virtual-баз, не має ні vptr, ні vtable.**[^itanium-cxx-abi] Його об’єкт займає стільки ж місця, скільки C-struct із тими самими полями (з можливим padding), а non-virtual метод нічого не додає в об’єкт.[^iso-tr-18015] Оверхед з’являється з першою virtual-функцією чи virtual-базою: vptr у кожному об’єкті та vtable на клас. Правило: інкапсулюй вільно; платиш за поліморфізм, лише коли оголошуєш `virtual`.

## Detailed explanation

Вартість `virtual` має дві частини: вказівник у кожному об’єкті та таблиця на клас. Звіт TR 18015 описує це так: клас без virtual-функції потребує стільки ж місця, скільки struct з тими самими даними, non-virtual функція місця в об’єкті не займає, а поліморфний клас платить одним вказівником на об’єкт плюс таблицею на клас.[^iso-tr-18015] Itanium ABI визначає dynamic class як клас, що потребує virtual table pointer, тож клас без відповідних ознак не має ні vptr, ні vtable.[^itanium-cxx-abi] Виклик його non-virtual методу зазвичай є звичайним прямим викликом, який оптимізатор може інлайнити (див. `qid:emb-cppoop-0001`).

Умова точніша, ніж «жодної virtual-функції». За Itanium ABI клас є dynamic, якщо він сам або його бази мають virtual-функції чи virtual-бази.[^itanium-cxx-abi] З цього випливають два наслідки. По-перше, клас із virtual-базою має vptr, навіть якщо не має жодної virtual-функції; TR 18015 додає, що virtual-база коштує дорожче за звичайну, бо позицію її підоб’єкта доводиться визначати динамічно, зазвичай через вказівник.[^iso-tr-18015] По-друге, клас, який успадковує поліморфну базу, платить за vptr, навіть якщо сам нічого не оголошує як `virtual`.

Формула «`sizeof` = сума полів + padding» теж лише наближення: кількість і розташування padding визначає реалізація,[^cpp-draft-expr-sizeof] тому для оцінки RAM краще перевіряти `sizeof` у `static_assert`, а не рахувати вручну. Для класу без virtual-функцій TR 18015 каже саме про рівність розміру з відповідною struct, поза можливим padding.[^iso-tr-18015]

```cpp
// Ілюстративний фрагмент; точні розміри залежать від ABI.
#include <cstdint>

struct Plain  { std::uint32_t a; std::uint16_t b; void set(std::uint32_t v) { a = v; } };
struct CPlain { std::uint32_t a; std::uint16_t b; };       // аналог C-struct
struct Poly   : Plain { virtual void f(); };               // є virtual-функція
struct VBase  { std::uint32_t x; };
struct VDer   : virtual VBase { std::uint16_t b; };        // virtual-функцій немає, але є virtual-база
struct NDer   : VBase { std::uint16_t b; };                // звичайна база

static_assert(sizeof(Plain) == sizeof(CPlain));   // метод розмір не змінює
static_assert(sizeof(Poly) > sizeof(Plain));      // додався vptr
static_assert(sizeof(VDer) > sizeof(NDer));       // vptr через virtual-базу
```

**Типові помилки:**

- Вважати, що vptr дають лише virtual-функції: virtual-база теж робить клас dynamic.
- Додавати `virtual` деструктор «про всяк випадок» у клас, який ніколи не видаляють через вказівник на базу: клас стає поліморфним і платить vptr та vtable (коли він потрібен, див. `qid:emb-cppoop-0017`).
- Рахувати `sizeof` як просту суму полів: padding і вирівнювання задає реалізація.

## Sources

<!-- generated from frontmatter -->
