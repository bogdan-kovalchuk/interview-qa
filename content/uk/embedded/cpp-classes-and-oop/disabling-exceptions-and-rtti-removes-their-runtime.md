---
id: emb-cppoop-0025
title: "Навіщо в embedded C++ використовують `-fno-exceptions` і `-fno-rtti`?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: gcc-fexceptions
    title: "GCC: Options for Code Generation Conventions (-fexceptions)"
    url: https://gcc.gnu.org/onlinedocs/gcc/Code-Gen-Options.html#index-fexceptions
  - source_id: gcc-fno-rtti
    title: "GCC: C++ Dialect Options (-fno-rtti)"
    url: https://gcc.gnu.org/onlinedocs/gcc/C_002b_002b-Dialect-Options.html#index-fno-rtti
  - source_id: iso-tr-18015
    title: "ISO/IEC TR 18015:2006 Technical Report on C++ Performance"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/TR18015.pdf
---

## Short answer

**`-fno-exceptions` не генерує код і дані, потрібні для поширення винятків, а `-fno-rtti` – type information для `dynamic_cast` і `typeid`.**[^gcc-fexceptions][^gcc-fno-rtti] Це зменшує бінарник, а час від `throw` до `catch` важко передбачити, тож для real-time винятки можуть не підходити.[^iso-tr-18015] Тому на таких цілях не використовуй `throw`, `typeid` і `dynamic_cast` із пониженням типу – покладайся на коди помилок і статичний поліморфізм.

## Detailed explanation

Прапорець `-fexceptions` змушує GCC генерувати додатковий код для поширення винятків, а на деяких цілях – і unwind-інформацію для всіх функцій, що дає помітний data size overhead; для C++ він увімкнений за замовчуванням, тож `-fno-exceptions` знімає ці витрати.[^gcc-fexceptions] ISO TR 18015 описує table-модель обробки винятків: поки виняток не кинуто, run-time накладних немає, але статичні таблиці бувають великими, і це відчутно для деяких embedded-систем.[^iso-tr-18015] Тобто виграш – передусім розмір, а не швидкість звичайного шляху.

Другий аргумент – передбачуваність. Той самий звіт каже, що час від `throw` до відповідного `catch` важко передбачити, бо треба знищити автоматичні об’єкти й звернутися до таблиць, тож для real-time реалізації винятків можуть не підходити; водночас за статичного дерева викликів його принципово можна проаналізувати.[^iso-tr-18015] Тому «винятки недетерміновані» – не закон, а характеристика типових реалізацій і складності аналізу; у проєктах із жорсткими вимогами до часу зазвичай переходять на коди помилок.

`-fno-rtti` вимикає генерацію інформації про класи з virtual-функціями, потрібної для `dynamic_cast` і `typeid`; якщо ці можливості не використовуються, це економить місце. Обмеження точніше, ніж «dynamic_cast не можна»: GCC дозволяє `dynamic_cast` там, де RTTI не потрібна, – до `void*` чи до однозначної бази, а інформацію для винятків генерує за потреби.[^gcc-fno-rtti] Пониження типу й `typeid` недоступні: GCC 13.3 відхиляє їх помилкою компіляції, так само як `throw` за `-fno-exceptions`. TR 18015 оцінює type information приблизно в 40 байтів на клас, але це дані 2006 року, а реальний розмір залежить від реалізації.[^iso-tr-18015] Змішувати код із `-frtti` і `-fno-rtti` ризиковано: компонування може не вдатися, якщо клас, зібраний із `-fno-rtti`, став базою для класу з `-frtti`.[^gcc-fno-rtti]

```cpp
// Ілюстративний фрагмент; збирається GCC з -fno-exceptions -fno-rtti.
#include <cstdint>

struct Base { virtual ~Base() = default; };
struct Derived : Base {};

const void* whole(Base* b) { return dynamic_cast<const void*>(b); }  // дозволено: до void*
Base* up(Derived* d)       { return dynamic_cast<Base*>(d); }        // дозволено: до бази
// Derived* down(Base* b) { return dynamic_cast<Derived*>(b); }      // помилка: потрібна RTTI

enum class Status : std::uint8_t { ok, timeout, bus_error };
Status read_reg(std::uint8_t reg, std::uint8_t& out);                // збій – значення, а не throw
```

Вимоги конкретного coding standard – окрема підстава вимикати ці можливості; їх треба брати з тексту стандарту, що діє в проєкті.

**Типові помилки:**

- Очікувати, що `-fno-exceptions` пришвидшить звичайний шлях: у table-моделі без `throw` накладних на виконання немає, виграш – у розмірі та прогнозованості.
- Вимкнути RTTI, але лишити в коді пониження типу через `dynamic_cast` чи `typeid`: GCC їх відхилить.
- Лишити конструктори, що можуть впасти: конструктор не повертає код помилки, тож потрібен інший шлях (див. qid:emb-cppoop-0011).
- Змішувати об’єкти, зібрані з `-frtti` і `-fno-rtti`: можливі помилки компонування.
