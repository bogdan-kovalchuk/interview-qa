---
id: emb-cppoop-0037
title: "Що має сказати кандидат про C++ OOP в embedded?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-core-guidelines-in-aims
    title: "C++ Core Guidelines: In.aims"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#inaims-aims
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
  - source_id: arm-cpp-abi
    title: "C++ ABI for the Arm Architecture (CPPABI32)"
    url: https://raw.githubusercontent.com/ARM-software/abi-aa/main/cppabi32/cppabi32.rst
  - source_id: itanium-abi-atexit
    title: "Itanium C++ ABI: DSO Object Destruction API"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html#dso-dtor-runtime-api
  - source_id: gcc-fexceptions
    title: "GCC 16.1.0: Code Gen Options, -fexceptions"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Code-Gen-Options.html#index-fexceptions
  - source_id: gcc-fno-rtti
    title: "GCC 16.1.0: C++ Dialect Options, -fno-rtti"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/C_002b_002b-Dialect-Options.html#index-fno-rtti
  - source_id: libstdcxx-no-exceptions
    title: "libstdc++ manual: Doing without"
    url: https://gcc.gnu.org/onlinedocs/libstdc++/manual/using_exceptions.html#intro.using.exception.no
---

## Short answer

**Кандидат має називати ціну кожної C++-фічі, а не забороняти OOP цілком.**

Клас без `virtual` не потребує vptr; `virtual` додає vptr у кожен об’єкт і vtable на клас;[^itanium-cxx-abi] перший коштує RAM, друга зазвичай лежить у ROM. CRTP і templates дають compile-time polymorphism без vptr; композиція – типовий вибір за замовчуванням. Startup і runtime теж мають ціну: обхід `.init_array` на Arm,[^arm-cpp-abi] atexit-реєстрація деструкторів глобальних об’єктів[^itanium-abi-atexit] і наслідки `-fno-exceptions`/`-fno-rtti`.[^gcc-fexceptions][^gcc-fno-rtti]

Правило: називай ціну в байтах і тактах, а не лише синтаксис.

## Detailed explanation

Відповіді «C++ в embedded – це важко» і «усе можна» однаково слабкі: сильна відповідь називає ціну кожної фічі. C++ Core Guidelines формулюють zero-overhead principle: за те, чим не користуєшся, не платиш, а правильно використана абстракція не гірша за ручний низькорівневий код;[^cpp-core-guidelines-in-aims] це принцип проєктування, а не гарантія для кожного компілятора. Клас без `virtual` не потребує vptr,[^itanium-cxx-abi] тож за розміром і викликами він зазвичай близький до C-struct із вільними функціями, якщо оптимізатор бачить тіла методів (див. qid:emb-cppoop-0001).

`virtual` додає vptr у кожен об’єкт і vtable на клас (див. qid:emb-cppoop-0013).[^itanium-cxx-abi] vptr коштує RAM на екземпляр: на 32-bit Arm вказівник зазвичай займає 4 байти, тож 50 об’єктів дають 200 B. vtable – це const-дані, їх зазвичай кладуть у read-only секцію (flash), але остаточне розміщення задають компілятор і linker script, тому перевіряй map file. Якщо поліморфізм потрібен над типами, відомими на етапі компіляції, CRTP чи templates обходяться без vptr (див. qid:emb-cppoop-0020 і qid:emb-cppoop-0021). Композиція – типовий вибір за замовчуванням, бо успадкування реалізації зв’язує класи тісніше (див. qid:emb-cppoop-0023); це рекомендація стилю, а не закон.

Startup і runtime теж мають ціну. Конструктори глобальних об’єктів хтось мусить викликати до `main`: Arm C++ ABI описує вектор у секції `.init_array`, який run-time support code проходить за зростанням адрес, а порядок між translation units ABI не задає.[^arm-cpp-abi] На інших таргетах механізм може відрізнятися (див. qid:emb-cppoop-0008). Деструктори глобальних об’єктів зазвичай реєструються через atexit-механізм (в Itanium ABI – `__cxa_atexit`),[^itanium-abi-atexit] а це може тягнути runtime-код і пам’ять навіть тоді, коли прошивка ніколи не завершується (див. qid:emb-cppoop-0009).

Прапорці `-fno-exceptions` і `-fno-rtti` прибирають частину runtime, але змінюють, що можна писати. У GCC `-fexceptions` для C++ увімкнено за замовчуванням, і на деяких таргетах він генерує unwind-інформацію для всіх функцій, що дає помітний data size overhead.[^gcc-fexceptions] Без нього `throw`, `try` і `catch` у твоєму коді не компілюються, а точки `throw` у libstdc++ переважно перетворюються на `abort()`.[^libstdcxx-no-exceptions] `-fno-rtti` вимикає інформацію про типи для `dynamic_cast` і `typeid`; `dynamic_cast` лишається лише для перетворень, яким RTTI не потрібна (до `void*` чи однозначної бази), а змішування коду з `-frtti` і `-fno-rtti` може не злінкуватися.[^gcc-fno-rtti] Докладніше – qid:emb-cppoop-0025.

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
