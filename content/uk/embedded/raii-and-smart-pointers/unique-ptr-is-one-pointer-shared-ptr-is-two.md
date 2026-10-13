---
id: emb-raii-0022
title: "Яка різниця між `unique_ptr` і `shared_ptr` за розміром?"
description: "unique_ptr (зі stateless deleter) зазвичай = розмір сирого вказівника; shared_ptr зазвичай = два вказівники + окремий control block."
track: embedded
section: raii-and-smart-pointers
level: junior
type: concept
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
  - source_id: cpp-draft-unique-ptr-single
    title: "C++ working draft: unique_ptr for single objects ([unique.ptr.single])"
    url: https://eel.is/c++draft/unique.ptr.single
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Визначає, що unique_ptr зберігає вказівник і deleter, а його деструктор викликає deleter лише для ненульового вказівника; copy-операції видалені, move дозволені. Розміру об’єкта не задає."
  - source_id: cpp-draft-intro-object
    title: "C++ working draft: Object model ([intro.object])"
    url: https://eel.is/c++draft/intro.object
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що нульовий розмір має base-підоб’єкт standard-layout класу без нестатичних даних, а в інших випадках обставини нульового розміру визначає реалізація. Конкретних значень sizeof не задає."
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
    accessed: 2026-10-13
    kind: spec
    version: null
    applicability: "Розкладка класів: порожня база спершу розміщується на зміщенні нуль, якщо це можливо. Це ABI, а не стандарт C++; вендорські тулчейни й інші платформи можуть відрізнятися."
  - source_id: libstdcxx-memory
    title: "The GNU C++ Library Manual: Memory – shared_ptr"
    url: https://gcc.gnu.org/onlinedocs/libstdc++/manual/memory.html#std.util.memory.shared_ptr
    accessed: 2026-10-13
    kind: official
    version: "current"
    applicability: "Опис реалізації libstdc++: shared_ptr містить T* і __shared_count з вказівником на _Sp_counted_base; make_shared розміщує об’єкт і control block в одній алокації; оновлення лічильників атомарні або з м’ютексом залежно від політики. Стосується лише libstdc++."
  - source_id: cpp-draft-util-smartptr-shared-create
    title: "C++ working draft: shared_ptr creation ([util.smartptr.shared.create])"
    url: https://eel.is/c++draft/util.smartptr.shared.create
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що make_shared і allocate_shared мають (should) виконувати не більше однієї алокації; це рекомендація, а не гарантія. Розкладку control block не задає."
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

## Sources

<!-- generated from frontmatter -->
