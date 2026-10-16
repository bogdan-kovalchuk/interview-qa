---
id: emb-raii-0032
title: "Чому `unique_ptr` вважають дефолтним smart pointer для embedded?"
track: embedded
section: raii-and-smart-pointers
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-unique-ptr-single
    title: "C++ working draft: unique_ptr for single objects ([unique.ptr.single])"
    url: https://eel.is/c++draft/unique.ptr.single
  - source_id: cpp-draft-unique-ptr-dltr-dflt
    title: "C++ working draft: default_delete ([unique.ptr.dltr.dflt])"
    url: https://eel.is/c++draft/unique.ptr.dltr.dflt
  - source_id: cppcg-r21
    title: "C++ Core Guidelines: R.21 – Prefer unique_ptr over shared_ptr unless you need to share ownership"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r21-prefer-unique_ptr-over-shared_ptr-unless-you-need-to-share-ownership
  - source_id: cpp-draft-util-smartptr-shared-create
    title: "C++ working draft: shared_ptr creation ([util.smartptr.shared.create])"
    url: https://eel.is/c++draft/util.smartptr.shared.create
---

## Short answer

**Доступ як у raw pointer, ексклюзивне володіння, явна передача через move, підтримка custom deleter під HAL.**

`unique_ptr` з default deleter зберігає вказівник і `default_delete` без даних-членів, тож у типових реалізаціях його розмір дорівнює розміру raw pointer, а `*` і `->` розіменовують той самий вказівник.[^cpp-draft-unique-ptr-dltr-dflt][^cpp-draft-unique-ptr-single] Для більшості сценаріїв володіння цього достатньо: на відміну від `shared_ptr`, він не веде лічильника посилань.[^cppcg-r21]

Правило: починай з `unique_ptr`; переходь на `shared_ptr` лише тоді, коли справді потрібне спільне володіння.[^embeddedinterviewlab]

## Detailed explanation

`unique_ptr<T, D>` зберігає вказівник і deleter `D`. Копіювання вимкнено, тож володіння переходить лише переміщенням, а джерело після переміщення має `get() == nullptr`. Деструктор, якщо вказівник ненульовий, викликає deleter для нього; default deleter `default_delete<T>` виконує `delete`.[^cpp-draft-unique-ptr-single][^cpp-draft-unique-ptr-dltr-dflt] Отже, це RAII-обгортка навколо тієї самої пари «виділити / звільнити», що й `new` і `delete`.

Накладні витрати зосереджені в розмірі об’єкта. Default deleter не має даних, тому в libstdc++ з GCC 13 розмір `unique_ptr<T>` дорівнює розміру вказівника. Це варто перевірити `static_assert` і на своєму тулчейні. Deleter зі станом, наприклад вказівник на функцію або лямбда із захопленням, зберігається в об’єкті й збільшує його розмір. Тому deleter для HAL-ресурсу краще робити порожнім функтором, як у прикладі нижче.

```cpp
#include <memory>

struct SpiHandle;
SpiHandle* hal_spi_open(int bus);   // illustrative HAL API
void hal_spi_close(SpiHandle* h);

struct SpiCloser {
  void operator()(SpiHandle* h) const { hal_spi_close(h); }
};

using SpiPtr = std::unique_ptr<SpiHandle, SpiCloser>;
static_assert(sizeof(SpiPtr) == sizeof(SpiHandle*));

void transfer(int bus) {
  SpiPtr spi(hal_spi_open(bus));  // closed automatically on every exit
  // ...
}
```

`unique_ptr` сам нічого не виділяє: він приймає вже отриманий вказівник і віддає його deleter-у. Якщо heap заборонено, `new` не викликають; тоді deleter повертає блок у статичний пул або викликає HAL-функцію, а явна передача володіння через move лишається.[^cpp-draft-unique-ptr-single] `shared_ptr` неявно веде лічильник посилань,[^cppcg-r21] а службові структури для нього можуть вимагати пам’яті понад `sizeof(T)`; стандарт радить (should) робити `make_shared` не більше ніж однією алокацією.[^cpp-draft-util-smartptr-shared-create] Ця вартість зайва, якщо власник один.

**Типові помилки:**

- Вважати, що deleter з станом не збільшує розміру: вказівник на функцію або захоплювальна лямбда зберігаються в `unique_ptr`.
- Розіменовувати джерело після того, як його переміщено (move-конструктором чи присвоєнням): його `get()` дорівнює `nullptr`, а `operator*` має precondition `get() != nullptr`, тож таке розіменування є undefined behavior.[^cpp-draft-unique-ptr-single]
- Брати `shared_ptr` «на всяк випадок»: це додає лічильник і спільне володіння, яких немає в задачі.
