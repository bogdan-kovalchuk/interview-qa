---
id: emb-raii-0011
title: "Які конкретні витрати має `shared_ptr`?"
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
  - source_id: cppcg-r22
    title: "C++ Core Guidelines: R.22 – Use make_shared() to make shared_ptrs"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r22-use-make_shared-to-make-shared_ptrs
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
