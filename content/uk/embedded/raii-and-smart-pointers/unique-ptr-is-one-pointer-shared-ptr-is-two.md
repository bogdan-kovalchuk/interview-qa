---
id: emb-raii-0022
title: "Яка різниця між `unique_ptr` і `shared_ptr` за розміром?"
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
  - source_id: cpp-draft-intro-object
    title: "C++ working draft: Object model ([intro.object])"
    url: https://eel.is/c++draft/intro.object
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
  - source_id: libstdcxx-memory
    title: "The GNU C++ Library Manual: Memory – shared_ptr"
    url: https://gcc.gnu.org/onlinedocs/libstdc++/manual/memory.html#std.util.memory.shared_ptr
  - source_id: cpp-draft-util-smartptr-shared-create
    title: "C++ working draft: shared_ptr creation ([util.smartptr.shared.create])"
    url: https://eel.is/c++draft/util.smartptr.shared.create
---

## Short answer

**`unique_ptr` (зі stateless deleter) зазвичай = розмір сирого вказівника; `shared_ptr` зазвичай = два вказівники + окремий control block.**

`shared_ptr` зберігає вказівник на об’єкт і вказівник на control block з лічильниками; у libstdc++ `make_shared` розміщує об’єкт і control block в одній алокації.[^libstdcxx-memory] Точний розмір залежить від реалізації STL і ABI: порожня база за Itanium C++ ABI може розміщуватися на зміщенні нуль.[^itanium-cxx-abi]

Правило: один власник -> `unique_ptr`; спільний власник -> `shared_ptr`, якщо витрати на control block і лічильники прийнятні.[^libstdcxx-memory]

## Detailed explanation

Розмір `unique_ptr` визначається тим, що він зберігає. Стандарт вимагає, щоб `unique_ptr` тримав і вказівник, і deleter, а деструктор виконував `if (get()) get_deleter()(get())`.[^cpp-draft-unique-ptr-single] Стандарт не фіксує розміру цих класів, а обставини нульового розміру порожнього підоб’єкта визначає реалізація.[^cpp-draft-intro-object] Якщо deleter порожній (stateless lambda або empty functor), реалізація може зберегти його як порожню базу, і тоді `unique_ptr` лишається завбільшки з вказівник. Itanium C++ ABI спершу пробує розмістити порожню базу на зміщенні нуль, тож на таких платформах вона може не додавати байтів.[^itanium-cxx-abi]

`shared_ptr` тримає два вказівники: на об’єкт і на control block, де лічильники strong і weak. У libstdc++ клас містить `T*` і `__shared_count`, а той вказує на `_Sp_counted_base`, який веде лічильники й знищує ресурс.[^libstdcxx-memory] Тому в libstdc++ `shared_ptr` займає два вказівники незалежно від deleter-а, а control block розміщується або окремо від об’єкта, або разом з ним у випадку `make_shared`.

Стандарт рекомендує, щоб `make_shared` робив не більше однієї алокації; це дає ефективність, еквівалентну intrusive smart pointer, але це рекомендація, а не гарантія.[^cpp-draft-util-smartptr-shared-create] У libstdc++ `make_shared` так і працює: об’єкт і control block лежать в одній алокації, тож окремої алокації під лічильники немає. Конструкція `shared_ptr<T>(new T)` дає дві алокації: одну для об’єкта, другу для control block.[^libstdcxx-memory]

Вибір між `unique_ptr` і `shared_ptr` – це питання власності, а не розміру. Коли власник один, `unique_ptr` дешевший і простіший. Коли власність справді спільна, `shared_ptr` платить за control block і лічильники, які в libstdc++ оновлюються атомарними операціями або м’ютексом залежно від політики збірки. Конкретний розмір на цільовому тулчейні варто перевірити через `sizeof`, а не брати з цього тексту.

**Типові помилки:**

- Вважати, що `sizeof` однаковий на всіх платформах: розмір залежить від STL, ABI і типу deleter-а.
- Вважати, що `make_shared` завжди робить одну алокацію: стандарт лише рекомендує не більше однієї.[^cpp-draft-util-smartptr-shared-create]
- Брати `shared_ptr` там, де є один власник: платиш control block і лічильники без потреби.
