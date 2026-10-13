---
id: emb-tmplcx-0017
title: "Trap: чому `std::function` може різко роздути Flash?"
description: "std::function – template-heavy type erasure; різні сигнатури й callable-типи можуть породити багато окремого коду."
track: embedded
section: templates-and-constexpr
level: junior
type: pitfall
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
  - source_id: cpp-draft-func-wrap-func
    title: "C++ working draft: Class template function ([func.wrap.func])"
    url: https://eel.is/c++draft/func.wrap.func
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Клас function – шаблон обгортки з викличною сигнатурою R(ArgTypes...). Розмір коду й використання Flash цей розділ не визначає."
  - source_id: cpp-draft-func-wrap-func-con
    title: "C++ working draft: Constructors and destructor ([func.wrap.func.con])"
    url: https://eel.is/c++draft/func.wrap.func.con
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Шаблонний конструктор приймає callable F і зберігає його як об’єкт типу decay_t<F>; динамічна пам’ять можлива (може кинути bad_alloc), а для малих callable-об’єктів стандарт рекомендує її уникати. Розмір коду цей розділ не визначає."
  - source_id: cpp-draft-temp-inst
    title: "C++ working draft: Implicit instantiation ([temp.inst])"
    url: https://eel.is/c++draft/temp.inst
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Визначає, коли шаблон функції чи класу неявно інстанціюється: коли на нього посилаються в контексті, що вимагає визначення. Не визначає розмір бінарника чи розміщення коду."
  - source_id: gnu-ld-print-map
    title: "GNU ld: Command-line options (-Map, --print-map)"
    url: https://sourceware.org/binutils/docs/ld/Options.html
    accessed: 2026-10-13
    kind: official
    version: "current"
    applicability: "Описує -Map=mapfile (link map у файл) і --print-map (вивід у stdout); вміст мапи залежить від linker script і тулчейна."
---

## Short answer

<span class="warn">`std::function` – template-heavy type erasure; різні сигнатури й callable-типи можуть породити багато окремого коду.</span>

Кожен callable-тип `F` зберігається як об’єкт типу `decay_t<F>`.[^cpp-draft-func-wrap-func-con] Його шаблонні обробники інстанціюються окремо для кожного такого типу.[^cpp-draft-temp-inst]

Захист: для простих callback'ів часто достатньо function pointer + `void* context`. На flash-обмежених MCU перевіряй розмір `std::function` через linker map.[^gnu-ld-print-map]

## Detailed explanation

`std::function<R(Args...)>` – шаблон класу з викличною сигнатурою `R(Args...)`, тому різні сигнатури дають різні типи, наприклад `std::function<void(int)>` і `std::function<int(int)>`.[^cpp-draft-func-wrap-func] Його шаблонний конструктор приймає будь-який callable `F` і створює ціль типу `decay_t<F>`, тож кожна лямбда чи функтор дає свій тип усередині `std::function`.[^cpp-draft-func-wrap-func-con]

Дві лямбди з однаковою сигнатурою – це два різні типи, хоча обидві змінні мають тип `std::function<void(int)>`:

```cpp
#include <functional>

void led_on(int);
void led_off(int);

std::function<void(int)> on  = [](int x) { led_on(x); };   // closure type #1
std::function<void(int)> off = [](int x) { led_off(x); };  // closure type #2, same signature
```

У libstdc++ (GCC 13, `-O0`) кожна така лямбда інстанціює власні шаблонні обробники: для неї з’являються окремі функції `_M_invoke` і `_M_manager` шаблону `_Function_handler`. Тобто для двох лямбд таких функцій удвічі більше, ніж для однієї.[^cpp-draft-temp-inst] Скільки коду це дає на конкретній платформі, залежить від реалізації, оптимізацій і кількості callable-типів, тому розмір треба виміряти, а не оцінювати на око.

Друга частина вартості – пам’ять. Реалізація може виділяти динамічну пам’ять для збереження цілі, і тоді конструювання може кинути `std::bad_alloc`; для малих callable-об’єктів стандарт рекомендує динамічну пам’ять уникати.[^cpp-draft-func-wrap-func-con] На системах без heap або з жорсткими вимогами до `new` `std::function` із великим захопленням – ризикований вибір незалежно від Flash.

Function pointer з `void* context` не створює окремого типу для кожного callable: тип визначає лише сигнатура, а контекст передається окремо. Ціна – ручне керування часом життя контексту і `void*`, який компілятор не перевіряє. Розмір перевіряй на цільовому тулчейні: `-Wl,-Map=app.map` записує link map у файл, `--print-map` виводить його в stdout; порівнюй мапи до і після переходу.[^gnu-ld-print-map]

**Типові помилки:**

- Вважати, що `std::function` завжди роздуває Flash: розмір залежить від кількості callable-типів, оптимізацій і тулчейна, його треба виміряти.
- Не врахувати динамічну пам’ять: `std::function` із великим захопленням на системі без heap може стати джерелом `std::bad_alloc`.
- Передавати `void* context` без перевірки типу: неправильний `static_cast` компілятор не виявить, і помилка проявиться лише під час виконання.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
