---
id: emb-cppoop-0037
title: "Що має сказати кандидат про C++ OOP в embedded?"
description: "OOP у embedded: клас без virtual не потребує vptr, virtual додає vptr (RAM) на об’єкт і vtable на клас (зазвичай ROM); CRTP дає compile-time polymorphism; композиція – типовий вибір за замовчуванням."
track: embedded
section: cpp-classes-and-oop
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
  - source_id: cpp-core-guidelines-in-aims
    title: "C++ Core Guidelines: In.aims"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#inaims-aims
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Формулює zero-overhead principle: що не використовуєш, за те не платиш, а правильно використана абстракція не гірша за ручний низькорівневий код. Це принцип проєктування, а не гарантія для кожного компілятора й коду."
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
    accessed: 2026-10-06
    kind: spec
    version: null
    applicability: "Визначає dynamic class (з virtual-функціями чи virtual-базами) як клас, що потребує virtual table pointer; отже клас без них його не має. Описує vtable як таблицю на клас. Це ABI, а не стандарт мови; секцію пам’яті для vtable не визначає."
  - source_id: arm-cpp-abi
    title: "C++ ABI for the Arm Architecture (CPPABI32)"
    url: https://raw.githubusercontent.com/ARM-software/abi-aa/main/cppabi32/cppabi32.rst
    accessed: 2026-10-06
    kind: spec
    version: null
    applicability: "У розділі Top-level static object construction: кожна translation unit дає фрагмент constructor vector у секції .init_array, елемент – адреса функції void(void), що конструює глобальні об’єкти цієї TU; run-time support code проходить вектор за зростанням адрес; порядок між TU ABI не задає. Це ABI для Arm; інші архітектури й тулчейни можуть відрізнятися."
  - source_id: itanium-abi-atexit
    title: "Itanium C++ ABI: DSO Object Destruction API"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html#dso-dtor-runtime-api
    accessed: 2026-10-06
    kind: spec
    version: null
    applicability: "У розділі 3.3.6.3 каже, що після конструювання глобального (або local static) об’єкта, який потребуватиме знищення при виході, реєструється функція завершення через __cxa_atexit. Це ABI, а не стандарт мови; розміру runtime не називає."
  - source_id: gcc-fexceptions
    title: "GCC 16.1.0: Code Gen Options, -fexceptions"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Code-Gen-Options.html#index-fexceptions
    accessed: 2026-10-06
    kind: official
    version: "16.1.0"
    applicability: "Каже, що -fexceptions вмикає обробку винятків і генерує додатковий код для їх поширення; для деяких таргетів GCC генерує frame unwind information для всіх функцій, що може давати значний data size overhead, хоч і не впливає на виконання; для C++ опція вмикається за замовчуванням. Конкретних розмірів не називає."
  - source_id: gcc-fno-rtti
    title: "GCC 16.1.0: C++ Dialect Options, -fno-rtti"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/C_002b_002b-Dialect-Options.html#index-fno-rtti
    accessed: 2026-10-06
    kind: official
    version: "16.1.0"
    applicability: "Каже, що -fno-rtti вимикає генерацію інформації про класи з virtual-функціями для dynamic_cast і typeid; dynamic_cast лишається для перетворень, яким RTTI не потрібна (до void* чи однозначної бази); змішування коду з -frtti і -fno-rtti може не працювати (наприклад, помилка link). Економії в байтах не називає."
  - source_id: libstdcxx-no-exceptions
    title: "libstdc++ manual: Doing without"
    url: https://gcc.gnu.org/onlinedocs/libstdc++/manual/using_exceptions.html#intro.using.exception.no
    accessed: 2026-10-06
    kind: official
    version: "current"
    applicability: "Каже, що -fno-exceptions ламає винятки, які проходять через такий код; код користувача з throw, try і catch у цьому режимі дає помилки; у libstdc++ точки throw для більшості виняткових класів замінено на abort(). Це про libstdc++; інші бібліотеки можуть поводитися інакше."
---

## Short answer

**Кандидат має називати ціну кожної C++-фічі, а не забороняти OOP цілком.**

Клас без `virtual` не потребує vptr; `virtual` додає vptr у кожен об’єкт і vtable на клас;[^itanium-cxx-abi] перший коштує RAM, друга зазвичай лежить у ROM. CRTP і templates дають compile-time polymorphism без vptr; композиція – типовий вибір за замовчуванням. Startup і runtime теж мають ціну: обхід `.init_array` на Arm,[^arm-cpp-abi] atexit-реєстрація деструкторів глобальних об’єктів[^itanium-abi-atexit] і наслідки `-fno-exceptions`/`-fno-rtti`.[^gcc-fexceptions][^gcc-fno-rtti]

Правило: називай ціну в байтах і тактах, а не лише синтаксис.

## Detailed explanation

Відповіді «C++ в embedded – це важко» і «усе можна» однаково слабкі: сильна відповідь називає ціну кожної фічі. C++ Core Guidelines формулюють zero-overhead principle: за те, чим не користуєшся, не платиш, а правильно використана абстракція не гірша за ручний низькорівневий код;[^cpp-core-guidelines-in-aims] це принцип проєктування, а не гарантія для кожного компілятора. Клас без `virtual` не потребує vptr,[^itanium-cxx-abi] тож за розміром і викликами він зазвичай близький до C-struct із вільними функціями, якщо оптимізатор бачить тіла методів (див. `qid:emb-cppoop-0001`).

`virtual` додає vptr у кожен об’єкт і vtable на клас (див. `qid:emb-cppoop-0013`).[^itanium-cxx-abi] vptr коштує RAM на екземпляр: на 32-bit Arm вказівник зазвичай займає 4 байти, тож 50 об’єктів дають 200 B. vtable – це const-дані, їх зазвичай кладуть у read-only секцію (flash), але остаточне розміщення задають компілятор і linker script, тому перевіряй map file. Якщо поліморфізм потрібен над типами, відомими на етапі компіляції, CRTP чи templates обходяться без vptr (див. `qid:emb-cppoop-0020` і `qid:emb-cppoop-0021`). Композиція – типовий вибір за замовчуванням, бо успадкування реалізації зв’язує класи тісніше (див. `qid:emb-cppoop-0023`); це рекомендація стилю, а не закон.

Startup і runtime теж мають ціну. Конструктори глобальних об’єктів хтось мусить викликати до `main`: Arm C++ ABI описує вектор у секції `.init_array`, який run-time support code проходить за зростанням адрес, а порядок між translation units ABI не задає.[^arm-cpp-abi] На інших таргетах механізм може відрізнятися (див. `qid:emb-cppoop-0008`). Деструктори глобальних об’єктів зазвичай реєструються через atexit-механізм (в Itanium ABI – `__cxa_atexit`),[^itanium-abi-atexit] а це може тягнути runtime-код і пам’ять навіть тоді, коли прошивка ніколи не завершується (див. `qid:emb-cppoop-0009`).

Прапорці `-fno-exceptions` і `-fno-rtti` прибирають частину runtime, але змінюють, що можна писати. У GCC `-fexceptions` для C++ увімкнено за замовчуванням, і на деяких таргетах він генерує unwind-інформацію для всіх функцій, що дає помітний data size overhead.[^gcc-fexceptions] Без нього `throw`, `try` і `catch` у твоєму коді не компілюються, а точки `throw` у libstdc++ переважно перетворюються на `abort()`.[^libstdcxx-no-exceptions] `-fno-rtti` вимикає інформацію про типи для `dynamic_cast` і `typeid`; `dynamic_cast` лишається лише для перетворень, яким RTTI не потрібна (до `void*` чи однозначної бази), а змішування коду з `-frtti` і `-fno-rtti` може не злінкуватися.[^gcc-fno-rtti] Докладніше – `qid:emb-cppoop-0025`.

```cpp
#include <cstdint>

// Ілюстративно: ціна virtual – вказівник у кожному об’єкті (Itanium ABI).
struct Plain { std::uint32_t x; void set(std::uint32_t v) { x = v; } };
struct Virt  { std::uint32_t x; virtual void set(std::uint32_t v) { x = v; } };

static_assert(sizeof(Plain) == sizeof(std::uint32_t));
static_assert(sizeof(Virt) >= sizeof(std::uint32_t) + sizeof(void*));
```

**Типові помилки:**

- Відповідати «C++ в embedded повільний і великий» загалом: ціну дають конкретні фічі (virtual, винятки, RTTI, heap, глобальні об’єкти), а не клас як такий.[^cpp-core-guidelines-in-aims]
- Вимкнути exceptions чи RTTI, не перевіривши код і бібліотеки: `throw` перестане компілюватися, а місця `throw` у libstdc++ перейдуть в `abort()`.[^libstdcxx-no-exceptions]
- Забути про startup: без обходу `.init_array` конструктори глобальних об’єктів на Arm не виконаються.[^arm-cpp-abi]
- Стверджувати, що vtable «завжди в ROM», не глянувши map file.

## Sources

<!-- generated from frontmatter -->
