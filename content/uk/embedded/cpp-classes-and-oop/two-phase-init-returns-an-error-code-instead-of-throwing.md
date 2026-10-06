---
id: emb-cppoop-0011
title: "Як ініціалізувати об’єкт, коли exceptions вимкнені (`-fno-exceptions`)?"
description: "Two-phase init: простий конструктор, що не може впасти, + окремий init() із кодом помилки; ціна – об’єкт до init() ще не готовий."
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
  - source_id: cpp-draft-class-ctor-general
    title: "C++ working draft: Constructors ([class.ctor.general])"
    url: https://eel.is/c++draft/class.ctor.general
    accessed: 2026-10-06
    kind: spec
    version: "working draft"
    applicability: "Каже, що в оголошенні конструктора допустимі лише decl-specifier friend, inline, constexpr, consteval і explicit (тобто типу, що повертається, немає) і що return у тілі конструктора не може повертати значення. Не каже, як сигналізувати про збій без exceptions."
  - source_id: cppcg-c41
    title: "C++ Core Guidelines: C.41 – A constructor should create a fully initialized object"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c41-a-constructor-should-create-a-fully-initialized-object
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Настанова: після конструктора об’єкт має бути придатним до використання; приклад із init(), який треба викликати перед іншими функціями, подано як поганий; виняток – якщо валідний об’єкт не можна зручно створити конструктором, використати factory function. Це настанова, а не вимога стандарту."
  - source_id: cppcg-c42
    title: "C++ Core Guidelines: C.42 – If a constructor cannot construct a valid object, throw an exception"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c42-if-a-constructor-cannot-construct-a-valid-object-throw-an-exception
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Настанова: кидати exception, а не лишати невалідний об’єкт; для змінної немає виклику, з якого можна повернути код помилки; для hard-real-time доменів, де exceptions непередбачувані, допускає is_valid(), яку треба перевіряти послідовно й одразу; радить уникати post-constructor чи two-stage initialization, а за потреби дивитися на factory functions."
  - source_id: cppcg-c44
    title: "C++ Core Guidelines: C.44 – Prefer default constructors to be simple and non-throwing"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c44-prefer-default-constructors-to-be-simple-and-non-throwing
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Настанова: default constructor має бути простим і non-throwing, щоб встановлення «значення за замовчуванням» не включало операцій, що можуть впасти. Не стосується init()."
  - source_id: cppcg-e27
    title: "C++ Core Guidelines: E.27 – If you can't throw exceptions, use error codes systematically"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#e27-if-you-cant-throw-exceptions-use-error-codes-systematically
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Настанова: без exceptions використовувати коди помилок систематично; показує повернення результату разом з індикатором помилки (pair, спеціальний тип) або valid() у самого об’єкта. Не є вимогою стандарту."
  - source_id: cpp-draft-dcl-attr-nodiscard
    title: "C++ working draft: Nodiscard attribute ([dcl.attr.nodiscard])"
    url: https://eel.is/c++draft/dcl.attr.nodiscard
    accessed: 2026-10-06
    kind: spec
    version: "working draft"
    applicability: "Каже, що виклик функції з nodiscard як discarded-value expression не рекомендований, і реалізація має видавати warning. Це рекомендована практика, а не помилка компіляції."
---

## Short answer

**Two-phase init: простий конструктор, що не може впасти, + окремий метод `init()`, який повертає код помилки.** Конструктор не може повернути код помилки, а exceptions вимкнені,[^cpp-draft-class-ctor-general] тому все, що може впасти, переходить в `err_t init()`, який викликач мусить перевірити. Ціна – до `init()` об’єкт ще непридатний,[^cppcg-c41] тож Core Guidelines віддають перевагу factory function, що повертає значення разом з помилкою.[^cppcg-c42][^cppcg-e27]

Правило: конструктор простий (no-fail), fallible-логіка – в окремому init з return code, а його результат перевіряй завжди.

## Detailed explanation

Конструктор не має імені й типу, що повертається: у його оголошенні дозволені лише `friend`, `inline`, `constexpr`, `consteval` та `explicit`, а `return` у тілі не може нести значення.[^cpp-draft-class-ctor-general] Без exceptions у нього лишаються здебільшого стан самого об’єкта чи вихідний параметр. Core Guidelines пояснюють проблему: для змінної немає виклику, з якого можна було б повернути код помилки, а невалідний об’єкт, що покладається на `is_valid()`, – це нудно й ненадійно.[^cppcg-c42]

Звідси two-phase init. Конструктор лише виставляє члени в безпечні початкові значення: без доступу до апаратури, heap чи будь-чого, що може впасти, – так, як C.44 радить для default constructor.[^cppcg-c44] Усе fallible (тактування, ініціалізація пінів і регістрів, перевірка пристрою) робить `init()`, який повертає код помилки. Для embedded є й практична причина: конструктори глобалів виконуються у startup до `main()` у неспецифікованому порядку (див. `qid:emb-cppoop-0008`, `qid:emb-cppoop-0010`), тому торкатися периферії там небезпечно; `init()` викликають із `main()` у відомому порядку.

Ціна патерну – проміжний стан. Core Guidelines наводять саме `init()` як поганий приклад: компілятор не читає коментарів, тож виклик методу до `init()` дає збій чи сміття.[^cppcg-c41] Тому недостатньо мати `init()`: кожен метод має або перевіряти стан готовності й повертати помилку, або мати чітко описану передумову. Атрибут `[[nodiscard]]` на `init()` допомагає, бо стандарт не рекомендує відкидати такий результат і радить реалізаціям давати warning.[^cpp-draft-dcl-attr-nodiscard] А ще Core Guidelines радять не вдаватися до two-stage init, якщо є вибір, і дивитися на factory function; вона може повертати результат разом з індикатором помилки.[^cppcg-c42][^cppcg-e27] Для hard-real-time вони прямо допускають `is_valid()`, але вимагають перевіряти її послідовно й одразу.[^cppcg-c42]

```cpp
enum class Err : std::uint8_t { ok, not_ready, bad_clock, bus_error };

class Spi {
public:
    constexpr Spi() = default;                 // no hardware access, cannot fail

    [[nodiscard]] Err init(std::uint32_t hz);  // may fail: the caller must check
    [[nodiscard]] Err write(const std::uint8_t* data, std::size_t n);

private:
    bool ready_ = false;
};

Spi spi;                                       // safe as a global: nothing can fail yet

Err Spi::write(const std::uint8_t*, std::size_t) {
    if (!ready_) { return Err::not_ready; }    // explicit "not initialised" state
    /* ... start the transfer ... */
    return Err::ok;
}
```

Фрагмент ілюстративний (потрібні `<cstdint>` і `<cstddef>`, а `init()` визначається окремо).

**Типові помилки:**

- Ігнорувати результат `init()` або взагалі не викликати його, а `write()` чи інші методи – викликати до готовності.
- Не мати явного стану «не ініціалізовано»: методи працюють із нульовим станом об’єкта.
- Робити в конструкторі «просто спробувати» й ховати збій у прапорі, який ніхто не перевіряє.
- Застосовувати two-phase init за звичкою, коли краще підходить factory function з поверненням результату разом з помилкою.

## Sources

<!-- generated from frontmatter -->
