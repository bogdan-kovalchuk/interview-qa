---
id: emb-raii-0010
title: "Чому `shared_ptr` рідко використовують у embedded?"
track: embedded
section: raii-and-smart-pointers
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-shared-ptr-general
    title: "C++ working draft: shared_ptr, General ([util.smartptr.shared.general])"
    url: https://eel.is/c++draft/util.smartptr.shared.general
  - source_id: cpp-draft-shared-ptr-const
    title: "C++ working draft: shared_ptr constructors ([util.smartptr.shared.const])"
    url: https://eel.is/c++draft/util.smartptr.shared.const
  - source_id: cpp-draft-shared-ptr-dest
    title: "C++ working draft: shared_ptr destructor ([util.smartptr.shared.dest])"
    url: https://eel.is/c++draft/util.smartptr.shared.dest
  - source_id: cpp-draft-shared-ptr-create
    title: "C++ working draft: shared_ptr creation ([util.smartptr.shared.create])"
    url: https://eel.is/c++draft/util.smartptr.shared.create
  - source_id: cpp-draft-shared-ptr-obs
    title: "C++ working draft: shared_ptr observers ([util.smartptr.shared.obs])"
    url: https://eel.is/c++draft/util.smartptr.shared.obs
  - source_id: cpp-draft-memory-syn
    title: "C++ working draft: Header <memory> synopsis ([memory.syn])"
    url: https://eel.is/c++draft/memory.syn
  - source_id: cpp-draft-freestanding-item
    title: "C++ working draft: Freestanding items ([freestanding.item])"
    url: https://eel.is/c++draft/freestanding.item
  - source_id: cppcg-r21-prefer-unique-ptr
    title: "C++ Core Guidelines: R.21 – Prefer unique_ptr over shared_ptr unless you need to share ownership"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r21-prefer-unique_ptr-over-shared_ptr-unless-you-need-to-share-ownership
---

## Short answer

<span class="warn">Дорогий: спільний control block, reference counting на copy/assign/destroy і зазвичай heap allocation.</span> Конструктор з вказівником може кидати `bad_alloc`, а для `make_shared` стандарт радить не більше однієї алокації.[^cpp-draft-shared-ptr-const][^cpp-draft-shared-ptr-create] Об’єкт знищує останній власник, тож момент знищення не видно з локального коду.[^cpp-draft-shared-ptr-general] Правило: на bare-metal без heap уникай `shared_ptr`; для одного власника бери `unique_ptr`.[^cppcg-r21-prefer-unique-ptr]

## Detailed explanation

`shared_ptr` реалізує shared ownership: об’єкт знищує останній із власників.[^cpp-draft-shared-ptr-general] Щоб кілька `shared_ptr` ділили один об’єкт, лічильник власників і deleter не можуть лежати в самому `shared_ptr`: вони живуть у спільному блоці, який зазвичай називають control block. Стандарт цього терміна не вживає, але конструктори з вказівником чи з deleter можуть кидати `bad_alloc`, а версії з allocator беруть його копію для пам’яті «internal use».[^cpp-draft-shared-ptr-const] Тому `shared_ptr<T>(new T)` зазвичай робить дві алокації (об’єкт і control block), а `make_shared` об’єднує їх, і стандарт радить виконувати не більше однієї; `allocate_shared` дозволяє підставити власний allocator, наприклад пул.[^cpp-draft-shared-ptr-create] Розмір control block стандарт не фіксує, а сам `shared_ptr` у libstdc++ на x86-64 займає 16 байт, тобто два вказівники (об’єкт і control block), проти 8 у `unique_ptr`.

Кожна копія й присвоєння збільшують лічильник, а знищення зменшує: destructor нічого не робить, якщо є інші власники, і викликає deleter чи `delete`, коли власник останній.[^cpp-draft-shared-ptr-dest] Стандарт не враховує зміни `use_count()` при визначенні data race, тож реалізація мусить оновлювати спільний лічильник так, щоб копії в різних потоках не створювали гонки;[^cpp-draft-shared-ptr-general] зазвичай це atomic-операції, якщо збірка підтримує потоки, а їхня ціна залежить від ядра й бібліотеки. Перевіряй її на цільовій платформі. Значення `use_count()` при цьому лише наближене, коли його можуть змінювати кілька потоків.[^cpp-draft-shared-ptr-obs]

Невизначеність тут стосується місця, а не часу: deleter і destructor об’єкта виконуються в контексті того, хто знищить останню копію, а це може бути інший потік, task чи навіть ISR.[^cpp-draft-shared-ptr-dest] Із локального коду цього не видно, а в `unique_ptr` власник і момент знищення очевидні.[^cppcg-r21-prefer-unique-ptr] Є й проблема доступності: у поточному робочому draft `unique_ptr` позначений як freestanding, а `shared_ptr` ні,[^cpp-draft-memory-syn] тож на freestanding-тулчейні його може не бути.[^cpp-draft-freestanding-item]

```cpp
// Ілюстративний приклад; Packet – довільний тип.
static Packet g_pkt;

// Об’єкт статичний, але конструктор shared_ptr може кинути bad_alloc;
// у libstdc++ (GCC 13) він виконує одну алокацію під control block.
std::shared_ptr<Packet> s(&g_pkt, [](Packet*) {});

// unique_ptr з function pointer deleter нічого не алокує.
std::unique_ptr<Packet, void (*)(Packet*)> u(&g_pkt, [](Packet*) {});
```

**Типові помилки:**

- Брати `shared_ptr` «про всяк випадок», хоч власник один: `unique_ptr` простіший і дешевший.[^cppcg-r21-prefer-unique-ptr]
- Створювати через `shared_ptr<T>(new T)` замість `make_shared<T>()`: зазвичай це зайва алокація.[^cpp-draft-shared-ptr-create]
- Вважати, що для статичного об’єкта `shared_ptr` не потребує heap: його конструктор з deleter усе одно може кинути `bad_alloc`, а в libstdc++ реально виділяє пам’ять.[^cpp-draft-shared-ptr-const]
- Приймати рішення в багатопоточному коді за `use_count()`: результат наближений.[^cpp-draft-shared-ptr-obs]
