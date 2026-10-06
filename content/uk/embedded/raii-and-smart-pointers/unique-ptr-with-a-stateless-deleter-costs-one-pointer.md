---
id: emb-raii-0008
title: "Який оверхед у `unique_ptr` порівняно з сирим вказівником?"
description: "Зі stateless deleter unique_ptr зазвичай має розмір одного raw pointer-а."
track: embedded
section: raii-and-smart-pointers
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
  - source_id: cpp-draft-unique-ptr-general
    title: "C++ working draft: Unique-ownership pointers, General ([unique.ptr.general])"
    url: https://eel.is/c++draft/unique.ptr.general
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Визначає unique pointer як об’єкт, що зберігає вказівник і розпоряджається ним через associated deleter при власному знищенні, зі strict ownership; unique_ptr не копіюється, але переміщується. Не каже нічого про розмір unique_ptr."
  - source_id: cpp-draft-unique-ptr-single
    title: "C++ working draft: unique_ptr for single objects ([unique.ptr.single])"
    url: https://eel.is/c++draft/unique.ptr.single
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Визначає деструктор unique_ptr (`if (get()) get_deleter()(get());`) і те, що unique_ptr зберігає вказівник та deleter. Розмір unique_ptr і inlining не регулює."
  - source_id: cpp-draft-lambda-closure
    title: "C++ working draft: Closure types ([expr.prim.lambda.closure])"
    url: https://eel.is/c++draft/expr.prim.lambda.closure
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що closure type не є aggregate і не є final, а реалізація може визначити його інакше, зокрема змінивши size і alignment. Тож розмір closure type стандарт не фіксує."
  - source_id: cpp-draft-lambda-capture
    title: "C++ working draft: Lambda captures ([expr.prim.lambda.capture])"
    url: https://eel.is/c++draft/expr.prim.lambda.capture
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що для кожної сутності, захопленої за копією, у closure type оголошується безіменний нестатичний член, а для захоплених за посиланням це unspecified. Не визначає sizeof closure type чи unique_ptr."
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
    accessed: 2026-10-06
    kind: spec
    version: null
    applicability: "Розділ 3.1.2.3: параметр класу, який non-trivial for the purposes of calls (зокрема з нетривіальним destructor), caller передає за посиланням на тимчасовий об’єкт і сам викликає його destructor після повернення, а не за правилами базового C ABI, наприклад у регістрі. Це ABI, що його використовує GCC на x86-64; для інших платформ, зокрема Arm, правила треба перевіряти в ABI їхнього тулчейна."
  - source_id: cppcg-r21-prefer-unique-ptr
    title: "C++ Core Guidelines: R.21 – Prefer unique_ptr over shared_ptr unless you need to share ownership"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r21-prefer-unique_ptr-over-shared_ptr-unless-you-need-to-share-ownership
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Настанова: unique_ptr простіший, передбачуваніший і швидший, бо не веде use count. Це рекомендація, а не вимога мови, і вона не стосується випадків, коли власність справді спільна."
  - source_id: cppcg-f7-smart-pointer-params
    title: "C++ Core Guidelines: F.7 – For general use, take T* or T& arguments rather than smart pointers"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#f7-for-general-use-take-t-or-t-arguments-rather-than-smart-pointers
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Настанова: функція, що не керує часом життя, має брати `T*` чи `T&`, а smart pointer у параметрі означає передачу або поділ власності. Про ціну передачі `unique_ptr` за значенням на рівні ABI не йдеться."
---

## Short answer

**Зі stateless deleter `unique_ptr` зазвичай має розмір одного raw pointer-а, але стандарт цього не гарантує.** `unique_ptr` має strict ownership і не копіюється, тож не потребує ні control block, ні reference counting.[^cpp-draft-unique-ptr-general] Deleter type відомий на compile time, тому з оптимізацією компілятор зазвичай інлайнить виклик teardown. Якщо deleter має стан або є function pointer, `sizeof(unique_ptr)` зазвичай зростає. Правило: `unique_ptr` – типовий вибір для одного власника; тримай його deleter stateless.[^cppcg-r21-prefer-unique-ptr]

## Detailed explanation

`unique_ptr` зберігає вказівник і deleter, лічильників у ньому немає: власник один, а копіювання заборонене.[^cpp-draft-unique-ptr-general] Скільки місця займає ця пара, стандарт не фіксує: навіть розмір closure type лямбди реалізація може визначити по-своєму.[^cpp-draft-lambda-closure] Практично, якщо deleter порожній, типові реалізації не виділяють йому окремого місця, і `sizeof(unique_ptr)` збігається з розміром вказівника. Порожній він тоді, коли немає стану: для лямбди нестатичні члени з’являються лише для захоплених сутностей.[^cpp-draft-lambda-capture] Function pointer, навпаки, треба зберігати, бо його значення може бути різним у різних об’єктів. Вимір у GCC 13 з libstdc++ на x86-64 дав такі розміри в байтах: сирий вказівник 8, `unique_ptr` з `default_delete` 8, з лямбдою без capture чи порожнім functor 8, з function pointer 16, з лямбдою, що захоплює змінну за посиланням, 16.

Виклик deleter теж безкоштовний лише за певних умов. Тип deleter входить у тип `unique_ptr`, тож деструктор викликає відомий на етапі компіляції `operator()`, і компілятор може його інлайнити.[^cpp-draft-unique-ptr-single] З оптимізацією (перевірено на GCC 13, `-Os`) виклик `HAL_UART_DeInit` з’являється прямо у функції, а перевірка вказівника на нуль зникає, коли це адреса відомого об’єкта. На `-O0` та сама логіка розпадається на ланцюжок малих функцій, тому «нульовий оверхед» – властивість оптимізованої збірки.

Залишається ціна, якої немає в raw pointer. У Itanium C++ ABI клас із нетривіальним деструктором, як `unique_ptr`, передається за значенням через адресу тимчасового об’єкта в пам’яті, а не в регістрі, і caller потім його знищує.[^itanium-cxx-abi] В асемблері GCC на x86-64 це видно; на інших платформах правила треба перевіряти в ABI тулчейна. Тому функції, які лише використовують ресурс, варто віддавати `T*` або `T&`, а `unique_ptr` за значенням брати лише там, де функція приймає власність.[^cppcg-f7-smart-pointer-params]

```cpp
struct Del { void operator()(Uart* h) const { HAL_UART_DeInit(h); } };

// Перевірка для конкретного тулчейна, а не гарантія стандарту.
static_assert(sizeof(std::unique_ptr<Uart, Del>) == sizeof(Uart*),
              "stateless deleter має не збільшувати unique_ptr");
```

**Типові помилки:**

- Вважати розмір «рівним вказівнику» гарантією стандарту, а не властивістю реалізації: перевіряй `sizeof` на своєму тулчейні.
- Вважати «нульовий оверхед» справедливим для `-O0`: без оптимізації виклики не інлайняться.
- Брати як deleter function pointer, `std::function` чи лямбду з capture, коли стан не потрібен: він зберігається в `unique_ptr`.
- Передавати `unique_ptr` за значенням у функцію, яка лише читає ресурс: це і зайва ціна, і хибний сигнал про передачу власності.[^cppcg-f7-smart-pointer-params]

## Sources

<!-- generated from frontmatter -->
