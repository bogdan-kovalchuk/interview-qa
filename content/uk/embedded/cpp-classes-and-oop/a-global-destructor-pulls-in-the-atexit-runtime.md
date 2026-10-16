---
id: emb-cppoop-0009
title: "Trap: чому просте оголошення деструктора може «роздути» ROM?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: itanium-abi-atexit
    title: "Itanium C++ ABI: DSO Object Destruction API"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html#dso-dtor-runtime-api
  - source_id: arm-cpp-abi
    title: "C++ ABI for the Arm Architecture (CPPABI32)"
    url: https://raw.githubusercontent.com/ARM-software/abi-aa/main/cppabi32/cppabi32.rst
  - source_id: cpp-draft-basic-start-term
    title: "C++ working draft: Termination ([basic.start.term])"
    url: https://eel.is/c++draft/basic.start.term
  - source_id: cpp-draft-class-dtor
    title: "C++ working draft: Destructors ([class.dtor])"
    url: https://eel.is/c++draft/class.dtor
  - source_id: cpp-draft-basic-life
    title: "C++ working draft: Object lifetime ([basic.life])"
    url: https://eel.is/c++draft/basic.life
  - source_id: gcc-cxx-cxa-atexit
    title: "GCC: C++ Dialect Options, -fuse-cxa-atexit"
    url: https://gcc.gnu.org/onlinedocs/gcc/C_002b_002b-Dialect-Options.html#index-fuse-cxa-atexit
  - source_id: gcc-int-init-macros
    title: "GCC Internals: Macros Controlling Initialization Routines"
    url: https://gcc.gnu.org/onlinedocs/gccint/Macros-for-Initialization.html
---

## Short answer

<span class="warn">Глобальний об’єкт із non-trivial деструктором змушує компілятор зареєструвати його знищення на старті (`__cxa_atexit`, на Arm – `__aeabi_atexit`), що може підтягнути atexit-runtime – зайві байти ROM.</span>[^itanium-abi-atexit][^arm-cpp-abi] Деструктор виконується лише при `exit` чи поверненні з `main`,[^cpp-draft-basic-start-term] а в firmware `main()` зазвичай не повертається, тож ця інфраструктура марна. Прапорець `-fno-use-cxa-atexit` лише змінює механізм, тому ефект залежить від таргета.[^gcc-cxx-cxa-atexit]

Захист: зроби деструктор trivial (`= default`, без `virtual`)[^cpp-draft-class-dtor] або створи об’єкт у статичному буфері через placement new і не знищуй його.

## Detailed explanation

За стандартом об’єкти зі static storage duration знищуються лише як частина виклику `std::exit`, а повернення з `main` саме його й викликає; `std::abort` деструкторів не виконує.[^cpp-draft-basic-start-term] Щоб `exit` знав, що і в якому порядку знищувати, кожен такий об’єкт треба зареєструвати. Тому після конструювання глобального (або local static) об’єкта, який потребуватиме знищення при виході, згенерований код викликає `__cxa_atexit(f, p, d)`;[^itanium-abi-atexit] Arm C++ ABI замість нього вимагає `__aeabi_atexit` і допускає, що список знищень виділяється статично, а його довжина дорівнює кількості місць виклику.[^arm-cpp-abi]

Звідси й «роздуття ROM». Реєстрація – це виклик функції з runtime, яка веде таблицю знищень, а сам деструктор стає досяжним кодом, бо на нього тепер є вказівник. У firmware `main()` зазвичай не повертається, тож жоден із цих деструкторів не виконається, але лінкер цього довести не може, і runtime разом із деструкторами лишається в образі. Скільки це байтів, залежить від libc і тулчейна, тому міряй за map-файлом, а не вгадуй.

`-fno-use-cxa-atexit` тут не панацея. GCC описує `-fuse-cxa-atexit` як вибір між `__cxa_atexit` і `atexit` та зазначає, що він потрібен для повністю стандартної поведінки статичних деструкторів;[^gcc-cxx-cxa-atexit] а внутрішній target hook визначає, чи деструктори ставляться в чергу на `__cxa_atexit`, чи збираються нативним механізмом таргета.[^gcc-int-init-macros] Тож що саме зміниться на твоєму таргеті, видно лише з map-файла чи дизасемблера.

Надійніше не мати чого реєструвати. Деструктор trivial, якщо він не user-provided, не virtual, а деструктори баз і членів теж trivial.[^cpp-draft-class-dtor] Отже `~Uart() = default` підходить, а `~Uart() {}` чи `virtual ~Uart() = default` – ні. Якщо деструктор потрібен, а знищувати об’єкт при виході ти не збираєшся, створи його в статичному буфері через placement new: стандарт дозволяє завершити lifetime об’єкта класу без виклику деструктора, хоч коректність програми часто від нього залежить.[^cpp-draft-basic-life]

```cpp
#include <new>

struct Uart {
    Uart();
    ~Uart();                                   // non-trivial: releases the peripheral
};

alignas(Uart) static unsigned char uart_storage[sizeof(Uart)];
Uart& uart = *new (uart_storage) Uart;         // constructed at startup, never destroyed
```

**Типові помилки:**

- Вважати, що `-fno-use-cxa-atexit` гарантовано прибирає реєстрацію, не глянувши на map-файл свого таргета.
- Писати порожнє тіло `~T() {}` замість `= default` або робити virtual деструктор у класі, який створюють глобально: такий деструктор non-trivial за визначенням,[^cpp-draft-class-dtor] а virtual-деструктори типові для інтерфейсів (див. qid:emb-cppoop-0017).
- Забувати, що local static із non-trivial деструктором теж реєструється, а не лише глобал.[^itanium-abi-atexit]
- Розраховувати, що деструктор глобала відпустить периферію «при вимкненні»: у firmware виходу зазвичай не буває.
