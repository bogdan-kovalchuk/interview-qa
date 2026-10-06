---
id: emb-raii-0011
title: "Які конкретні витрати має `shared_ptr`?"
description: "Control block зі strong/weak лічильниками, зазвичай atomic increments/decrements, динамічна алокація (одна з `make_shared`) і момент знищення, що залежить від останнього власника."
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
    applicability: "Описує реалізацію libstdc++: shared_ptr містить pointer на об’єкт і pointer на control block; control block веде strong/weak лічильники, а deleter та allocator зберігають похідні класи; лічильники оновлюються atomic-операціями (політики atomic, mutex, single), а в однопотоковій програмі – дешевшими non-atomic; make_shared може покласти об’єкт і control block в один блок. Стосується лише libstdc++; інші бібліотеки можуть відрізнятися."
  - source_id: cpp-draft-util-smartptr-shared
    title: "C++ working draft: Class template shared_ptr ([util.smartptr.shared])"
    url: https://eel.is/c++draft/util.smartptr.shared
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що останній власник, який лишився, відповідає за знищення об’єкта; що member-функції для визначення data race зачіпають лише самі shared_ptr і weak_ptr, а не об’єкти, на які вони вказують; що зміни use_count() не відображають модифікацій, які можуть спричинити data race. Розкладку control block і вартість операцій не задає."
  - source_id: cpp-draft-util-smartptr-shared-create
    title: "C++ working draft: shared_ptr creation ([util.smartptr.shared.create])"
    url: https://eel.is/c++draft/util.smartptr.shared.create
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що реалізації make_shared і allocate_shared мають (should) виконувати не більше однієї алокації, що allocate_shared використовує копію переданого allocator-а і що ці функції зазвичай алокують більше за sizeof(T) для службових структур, як-от лічильники. Одного блоку не гарантує."
  - source_id: cppcg-r21
    title: "C++ Core Guidelines: R.21 – Prefer unique_ptr over shared_ptr unless you need to share ownership"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r21-prefer-unique_ptr-over-shared_ptr-unless-you-need-to-share-ownership
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Настанова: unique_ptr простіший, передбачуваніший (відомо, коли відбудеться знищення) і швидший, бо не веде use count; shared_ptr, чий лічильник ніколи не перевищує 1, веде його даремно. Це настанова, а не вимір швидкодії."
  - source_id: cppcg-r22
    title: "C++ Core Guidelines: R.22 – Use make_shared() to make shared_ptrs"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r22-use-make_shared-to-make-shared_ptrs
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Настанова: make_shared дає змогу прибрати окрему алокацію для лічильників, розмістивши їх поруч з об’єктом; також забезпечує exception safety у складних виразах до C++17. Про розмір чи вартість лічильників не каже."
---

## Short answer

**Control block із лічильниками, зазвичай atomic increments/decrements, динамічна алокація та знищення, коли останній власник відпускає об’єкт.**

У libstdc++ `shared_ptr` тримає pointer-и на object і на control block (strong/weak counters, deleter/allocator state); лічильники оновлюються atomic-операціями (в однопотоковій програмі – дешевшими non-atomic).[^libstdcxx-memory] Стандарт рекомендує, щоб `make_shared` робив щонайбільше одну алокацію, але control block лишається.[^cpp-draft-util-smartptr-shared-create]

Правило: називай категорії витрат, а не лише «shared_ptr повільний»; для одного власника `unique_ptr` простіший і швидший.[^cppcg-r21]

## Detailed explanation

Стандарт описує `shared_ptr` як тип зі shared ownership: останній власник, що лишився, відповідає за знищення об’єкта.[^cpp-draft-util-smartptr-shared] Розкладку стандарт не задає, тож конкретні витрати залежать від реалізації. У libstdc++ `shared_ptr<T>` складається з pointer-а на `T` і pointer-а на control block; базовий клас control block веде strong і weak counters, а похідні зберігають pointer, deleter та allocator.[^libstdcxx-memory] Тому сам `shared_ptr` займає два pointer-и, а кожен керований об’єкт отримує ще й control block.

**Алокація.** Якщо `shared_ptr` будують з pointer-а, який уже дав `new`, control block потребує окремої алокації; `make_shared` дає змогу прибрати її, поклавши лічильники поруч з об’єктом.[^cppcg-r22] Стандарт лише рекомендує не більше однієї алокації, а `allocate_shared` бере переданий allocator, наприклад над статичним pool-ом.[^cpp-draft-util-smartptr-shared-create] Зворотний бік одного блоку: control block мусить жити, доки є weak-посилання, тож пам’ять під об’єкт повертається лише після останнього `weak_ptr`, хоча destructor об’єкта викликається раніше.[^libstdcxx-memory]

```cpp
// Ілюстративно: типово два блоки проти одного (залежить від реалізації).
auto a = std::shared_ptr<Buf>(new Buf{});   // об’єкт і control block окремо
auto b = std::make_shared<Buf>();           // об’єкт і control block разом
```

**Лічильники.** Копіювання збільшує лічильник, знищення зменшує. Стандарт не вважає зміни `use_count()` модифікаціями, що можуть створити data race,[^cpp-draft-util-smartptr-shared] тому реалізація мусить оновлювати лічильники коректно навіть тоді, коли різні `shared_ptr` на один об’єкт живуть у різних потоках. libstdc++ робить це atomic-операціями (за відсутності atomic builtins – через mutex), а коли в програмі лише один потік, обирає дешевші non-atomic.[^libstdcxx-memory] Скільки це коштує на конкретному ядрі, залежить від цілі й тулчейна, тож це треба вимірювати.

**Момент знищення.** Об’єкт знищує той власник, який відпустить його останнім, тож `~T` і deleter виконуються там, де це трапилось, а не у відомому scope. Якщо останню копію відпускає критична секція чи обробник переривання, туди ж потрапляє й вартість знищення. У `unique_ptr` момент знищення відомий наперед, і це одна з причин, чому Core Guidelines радять його, коли ділити володіння не потрібно.[^cppcg-r21]

**Типові помилки:**

- Брати `shared_ptr` як «безкоштовний» `unique_ptr`: лічильник і control block з’являються, навіть коли use count ніколи не перевищує 1.[^cppcg-r21]
- Думати, що `make_shared` прибирає control block: він прибирає лише окрему алокацію, а службові структури лишаються.[^cpp-draft-util-smartptr-shared-create]
- Вважати atomic-лічильники захистом самого об’єкта: стандарт говорить про data race лише для самих `shared_ptr` і `weak_ptr`, а не для об’єктів, на які вони вказують.[^cpp-draft-util-smartptr-shared]
- Передавати `shared_ptr` за значенням у кожну функцію, яка лише використовує об’єкт: кожна така копія – це зайвий increment і decrement.

## Sources

<!-- generated from frontmatter -->
