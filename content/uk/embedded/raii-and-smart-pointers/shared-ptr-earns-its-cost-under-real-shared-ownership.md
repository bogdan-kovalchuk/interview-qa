---
id: emb-raii-0012
title: "Коли `shared_ptr` все ж виправданий у embedded?"
track: embedded
section: raii-and-smart-pointers
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: libstdcxx-memory
    title: "The GNU C++ Library Manual: Memory – shared_ptr"
    url: https://gcc.gnu.org/onlinedocs/libstdc++/manual/memory.html#std.util.memory.shared_ptr
  - source_id: cpp-draft-util-smartptr-shared
    title: "C++ working draft: Class template shared_ptr ([util.smartptr.shared])"
    url: https://eel.is/c++draft/util.smartptr.shared
  - source_id: cpp-draft-util-smartptr-shared-create
    title: "C++ working draft: shared_ptr creation ([util.smartptr.shared.create])"
    url: https://eel.is/c++draft/util.smartptr.shared.create
  - source_id: cppcg-r21
    title: "C++ Core Guidelines: R.21 – Prefer unique_ptr over shared_ptr unless you need to share ownership"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r21-prefer-unique_ptr-over-shared_ptr-unless-you-need-to-share-ownership
  - source_id: cppcg-r24
    title: "C++ Core Guidelines: R.24 – Use std::weak_ptr to break cycles of shared_ptrs"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r24-use-stdweak_ptr-to-break-cycles-of-shared_ptrs
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
