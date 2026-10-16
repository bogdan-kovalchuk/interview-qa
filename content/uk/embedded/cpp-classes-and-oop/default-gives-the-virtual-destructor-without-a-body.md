---
id: emb-cppoop-0034
title: "Чому в abstract base слід надавати `= default` для virtual destructor?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-expr-delete
    title: "C++ working draft: Delete ([expr.delete])"
    url: https://eel.is/c++draft/expr.delete
  - source_id: cpp-draft-class-virtual
    title: "C++ working draft: Virtual functions ([class.virtual])"
    url: https://eel.is/c++draft/class.virtual
  - source_id: cpp-draft-class-dtor
    title: "C++ working draft: Destructors ([class.dtor])"
    url: https://eel.is/c++draft/class.dtor
  - source_id: cpp-draft-dcl-fct-def-default
    title: "C++ working draft: Explicitly-defaulted functions ([dcl.fct.def.default])"
    url: https://eel.is/c++draft/dcl.fct.def.default
  - source_id: cpp-draft-class-copy-ctor
    title: "C++ working draft: Copy/move constructors ([class.copy.ctor])"
    url: https://eel.is/c++draft/class.copy.ctor
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
  - source_id: itanium-abi-atexit
    title: "Itanium C++ ABI: DSO Object Destruction API"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html#dso-dtor-runtime-api
  - source_id: cpp-core-guidelines-c35
    title: "C++ Core Guidelines: C.35 (base class destructor)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c35-a-base-class-destructor-should-be-either-public-and-virtual-or-protected-and-non-virtual
  - source_id: cpp-core-guidelines-c121
    title: "C++ Core Guidelines: C.121 (base class used as an interface)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c121-if-a-base-class-is-used-as-an-interface-make-it-a-pure-abstract-class
---

## Question code

```cpp
virtual ~Sensor() = default;
```

## Short answer

**Забезпечує коректне поліморфне знищення без ручного порожнього тіла.**

`= default` просить компілятор згенерувати destructor, а `virtual` робить його non-trivial за визначенням.[^cpp-draft-class-dtor] Без `virtual` `delete base_ptr` на об’єкті нащадка – undefined behavior,[^cpp-draft-expr-delete] а з ним destructor вибирається за dynamic type.[^cpp-draft-class-virtual]

Правило: якщо base можуть видаляти через вказівник на нього, пиши `public virtual ~T() = default;`, інакше – `protected` non-virtual destructor.[^cpp-core-guidelines-c35]

## Detailed explanation

Типовий сценарій: є інтерфейс `Sensor`, а об’єкти нащадків видаляють через `Sensor*`. Якщо static type видаленого об’єкта не збігається з dynamic type, стандарт вимагає, щоб static type був базою й мав virtual destructor, інакше поведінка не визначена.[^cpp-draft-expr-delete] На практиці зазвичай виконується лише `~Sensor()`, і ресурси нащадка (буфери, handle, RAII-об’єкти) не звільняються, але розраховувати на це не можна: це undefined behavior. З `virtual` виклик залежить від dynamic type,[^cpp-draft-class-virtual] тож знищується весь нащадок. Докладніше про цей випадок – qid:emb-cppoop-0017.

Чому `= default`, а не `{}`. Функція, explicitly defaulted на першому оголошенні, не є user-provided і неявно inline, а порожнє тіло `{}` – user-provided.[^cpp-draft-dcl-fct-def-default] Для порожнього destructor різниці в коді зазвичай немає, вона в наміру: `= default` каже «нічого особливого», і Core Guidelines описують інтерфейс саме як набір pure virtual функцій із default або порожнім virtual destructor.[^cpp-core-guidelines-c121] Водночас будь-який user-declared destructor, навіть `= default`, прибирає неявний move constructor, а неявне генерування copy constructor стає deprecated.[^cpp-draft-class-copy-ctor] Для інтерфейсу без даних це неважливо, а для base із даними краще явно описати всі special member functions.

Virtual destructor не безкоштовний, і в embedded це відчутно. Він завжди non-trivial, бо trivial destructor не може бути virtual.[^cpp-draft-class-dtor] Тому глобальний об’єкт такого класу потребує реєстрації знищення при виході (в Itanium ABI – через `__cxa_atexit`; див. qid:emb-cppoop-0009).[^itanium-abi-atexit] До того ж у vtable virtual destructor займає пару entries, одна з яких – deleting destructor, що викликає `operator delete`.[^itanium-cxx-abi] Тому об’єктний файл із таким класом зазвичай посилається на `operator delete`, навіть якщо `delete` у коді немає; на bare-metal це означає додатковий символ у link (перевіряй `nm` або map file свого тулчейна).

Якщо через base видаляти не потрібно (об’єкти статичні, heap немає), Core Guidelines дозволяють інший варіант: `protected` non-virtual destructor. Тоді `delete` через вказівник на base не скомпілюється,[^cpp-core-guidelines-c35] а non-virtual destructor не додає до vtable пари entries (перевіряй `nm` або map file).

```cpp
#include <cstdint>

// Ілюстративно: інтерфейс, який можуть видаляти через Sensor*.
struct Sensor {
    virtual std::int16_t read() = 0;
    virtual ~Sensor() = default;      // public virtual: delete через Sensor* коректний
};

// Варіант, якщо через base ніколи не видаляють (static-об’єкти, без heap).
struct StaticSensor {
    virtual std::int16_t read() = 0;
protected:
    ~StaticSensor() = default;        // non-virtual: delete через StaticSensor* не скомпілюється
};
```

**Типові помилки:**

- Забути `virtual` у base, який видаляють через вказівник на нього: це undefined behavior, а не «просто витік».[^cpp-draft-expr-delete]
- Думати, що `= default` швидший за `{}` чи робить destructor trivial: у virtual destructor він non-trivial в обох випадках.[^cpp-draft-class-dtor]
- Додавати virtual destructor у клас, який ніколи не видаляють через base: зайві entries у vtable, залежність від `operator delete` і реєстрація знищення глобальних об’єктів.
- Забути, що user-declared destructor (навіть `= default`) вимикає неявний move.[^cpp-draft-class-copy-ctor]
