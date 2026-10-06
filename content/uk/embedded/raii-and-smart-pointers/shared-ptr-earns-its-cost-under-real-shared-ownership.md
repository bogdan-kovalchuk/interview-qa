---
id: emb-raii-0012
title: "Коли `shared_ptr` все ж виправданий у embedded?"
description: "Коли є справжнє спільне володіння і прийнятні витрати на control block та лічильники; heap за замовчуванням потрібен, але `allocate_shared` дає змогу підставити власний allocator."
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
  - source_id: libstdcxx-memory
    title: "The GNU C++ Library Manual: Memory – shared_ptr"
    url: https://gcc.gnu.org/onlinedocs/libstdc++/manual/memory.html#std.util.memory.shared_ptr
    accessed: 2026-10-06
    kind: official
    version: "current"
    applicability: "Описує реалізацію libstdc++: політики лічильників atomic (за наявності atomic compare-and-swap builtin), mutex (без atomic builtins) і single (бібліотека зібрана без потоків); make_shared пересилає виклик у allocate_shared зі std::allocator; шаблон shared_ptr забезпечує thread safety на рівні вбудованих типів. Стосується лише libstdc++; інші бібліотеки можуть відрізнятися."
  - source_id: cpp-draft-util-smartptr-shared
    title: "C++ working draft: Class template shared_ptr ([util.smartptr.shared])"
    url: https://eel.is/c++draft/util.smartptr.shared
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що shared_ptr реалізує shared ownership і що останній власник, який лишився, відповідає за знищення об’єкта; що member-функції для визначення data race зачіпають лише самі shared_ptr і weak_ptr, а не об’єкти, на які вони вказують. Не радить, коли саме його застосовувати."
  - source_id: cpp-draft-util-smartptr-shared-create
    title: "C++ working draft: shared_ptr creation ([util.smartptr.shared.create])"
    url: https://eel.is/c++draft/util.smartptr.shared.create
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що allocate_shared виділяє пам’ять через копію переданого allocator-а, а реалізації make_shared і allocate_shared мають (should) виконувати не більше однієї алокації. Не описує, як побудувати pool-allocator."
  - source_id: cppcg-r21
    title: "C++ Core Guidelines: R.21 – Prefer unique_ptr over shared_ptr unless you need to share ownership"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r21-prefer-unique_ptr-over-shared_ptr-unless-you-need-to-share-ownership
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Настанова: unique_ptr простіший, передбачуваніший (відомо, коли відбудеться знищення) і швидший, бо не веде use count; shared_ptr, чий лічильник ніколи не перевищує 1, веде його даремно. Про конкретні embedded-сценарії не каже."
  - source_id: cppcg-r24
    title: "C++ Core Guidelines: R.24 – Use std::weak_ptr to break cycles of shared_ptrs"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r24-use-stdweak_ptr-to-break-cycles-of-shared_ptrs
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Настанова: shared_ptr спирається на use count, і для циклічної структури він ніколи не дійде до нуля, тож цикл треба розривати через weak_ptr. Про вартість чи embedded-контекст не каже."
---

## Short answer

**Коли є справжнє спільне володіння – немає одного власника, який переживає всіх користувачів, – і прийнятні витрати на control block та лічильники.**

Приклади: reference-counted buffers в embedded Linux userspace, plugin/модульні системи зі спільними config-блоками, об’єкти з lifetime, який справді не має одного власника. `make_shared` за замовчуванням алокує через `std::allocator`,[^libstdcxx-memory] а `allocate_shared` приймає власний allocator.[^cpp-draft-util-smartptr-shared-create] Для DMA (direct memory access) buffers у bare-metal частіше краще явний owner + borrowed views.

Правило: `shared_ptr` – лише для реального shared ownership, не «про всяк випадок».[^cppcg-r21]

## Detailed explanation

`shared_ptr` реалізує shared ownership: останній власник, що лишився, відповідає за знищення об’єкта.[^cpp-draft-util-smartptr-shared] Справжнє спільне володіння – це коли кілька учасників користуються об’єктом і жоден з них не може бути призначений власником, бо порядок, у якому вони завершать роботу, невідомий наперед. Типовий приклад – буфер повідомлення, який кілька споживачів читають і відпускають у довільному порядку. Якщо ж власник очевидний, а решта лише користується об’єктом, поки той живий, вистачає `unique_ptr` разом із non-owning pointer чи reference. `shared_ptr`, чий лічильник ніколи не перевищує 1, веде use count даремно.[^cppcg-r21]

**Умови в embedded.** В embedded Linux userspace є heap і потоки, тож вартість control block і лічильників зазвичай прийнятна. На bare-metal питання в пам’яті: за замовчуванням control block алокується динамічно, але `allocate_shared` бере копію переданого allocator-а,[^cpp-draft-util-smartptr-shared-create] тож його можна спрямувати на статичний pool фіксованого розміру. Atomics – це радше чинник вартості, ніж умова коректності: libstdc++ вибирає політику лічильників залежно від цілі – atomic за наявності atomic compare-and-swap builtin, mutex без нього, single у збірці без потоків.[^libstdcxx-memory]

```cpp
// Ілюстративно: два модулі ділять один незмінний конфіг.
auto cfg = std::make_shared<const Config>(Config{115200});
Logger logger{cfg};   // кожен модуль тримає власну копію shared_ptr
Uart   uart{cfg};     // Config живе, доки живе останній з них
```

**Спостерігачі й цикли.** Якщо частина учасників лише спостерігає й не повинна продовжувати життя об’єкта, їм дають `weak_ptr`. Він також розриває цикли: use count циклічної структури з `shared_ptr` ніколи не дійде до нуля.[^cppcg-r24]

**DMA-буфери.** Для DMA buffers на bare-metal зазвичай є природний owner – драйвер, який віддає буфер периферії й отримує його назад після завершення передачі. Явна передача володіння плюс view на час запису не потребує лічильника, тому це частіше простіший вибір; це міркування про дизайн, а не вимога стандарту.

**Типові помилки:**

- Брати `shared_ptr` «про всяк випадок» або щоб не думати про власника, хоча use count не перевищує 1.[^cppcg-r21]
- Тримати owning `shared_ptr` у обидва боки зв’язку: цикл не звільниться, один бік має бути `weak_ptr`.[^cppcg-r24]
- Вважати, що спільне володіння робить сам об’єкт thread-safe: для data race стандарт розглядає лише самі `shared_ptr` і `weak_ptr`, а не об’єкти, на які вони вказують.[^cpp-draft-util-smartptr-shared]
- Забувати, що на цілі без heap `shared_ptr` потребує pool-allocator-а через `allocate_shared`, інакше control block потрапляє на heap.

## Sources

<!-- generated from frontmatter -->
