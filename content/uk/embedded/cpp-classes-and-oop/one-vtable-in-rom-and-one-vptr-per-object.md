---
id: emb-cppoop-0013
title: "Скільки коштує virtual-функція по пам’яті?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-class-virtual
    title: "C++ working draft: Virtual functions ([class.virtual])"
    url: https://eel.is/c++draft/class.virtual
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
  - source_id: arm-cpp-abi
    title: "C++ ABI for the Arm Architecture (CPPABI32)"
    url: https://raw.githubusercontent.com/ARM-software/abi-aa/main/cppabi32/cppabi32.rst
---

## Short answer

**Зазвичай vtable – одна на polymorphic class у ROM (read-only memory, `.rodata`), vptr – один прихований pointer на кожен polymorphic object у RAM (random-access memory).**

Спрощена оцінка: vtable ≈ кількість virtual functions × розмір pointer-а плюс службові слоти ABI (offset-to-top, typeinfo), а virtual destructor займає дві entries; vptr ≈ один pointer на екземпляр, хоча кілька polymorphic баз додають ще vptr-и.[^itanium-cxx-abi] Це деталі ABI, а не стандарту C++; для Arm інших правил не заявлено.[^arm-cpp-abi]

Правило: vtable рахуй приблизно на клас (ROM), vptr – на екземпляр (RAM); при сотнях об’єктів RAM-вартість стає відчутною.

## Detailed explanation

Стандарт C++ описує поведінку: virtual-функція дає dynamic binding, а клас з нею називається polymorphic.[^cpp-draft-class-virtual] Як саме це реалізовано, залежить від ABI. В Itanium C++ ABI, на якому базується й Arm C++ ABI,[^arm-cpp-abi] клас із virtual-функціями (dynamic class) має vtable – таблицю для виклику virtual-функцій, доступу до virtual base і RTTI. Усі об’єкти того самого найпохідного класу вказують на той самий набір таблиць,[^itanium-cxx-abi] тому вартість таблиці платиться один раз на клас, а не на об’єкт.

Таблиця трохи більша, ніж «кількість функцій × розмір pointer-а». Для кожної virtual-функції є слот у порядку оголошення, але ще завжди присутні offset-to-top і typeinfo pointer, а virtual destructor займає пару entries: complete object destructor і deleting destructor.[^itanium-cxx-abi] Тому для n virtual-функцій і pointer-а розміром p оцінка ближча до `(n + 2) * p`, а з virtual destructor додається ще один слот. Для співбесіди `n * p` – прийнятна перша оцінка, але варто знати поправку.

vptr живе в самому об’єкті: якщо в класу немає primary base, ABI розміщує його на offset 0, і `sizeof` зростає на розмір pointer-а з урахуванням вирівнювання.[^itanium-cxx-abi] Primary base ділить vptr із похідним класом, а кожна інша dynamic base приносить власний, тому множинне успадкування від кількох polymorphic класів збільшує об’єкт сильніше.[^itanium-cxx-abi]

Чи лежить vtable саме в ROM, ABI не визначає. Це const-дані, і тулчейн зазвичай кладе їх у read-only секцію (`.rodata`, у flash), але остаточне розміщення задають компілятор і linker script; у збірках із relocation вона може опинитися в іншій секції. Перевіряй у map file.

```cpp
// Illustrative: типово на 32-bit Arm
struct Sensor {
    virtual int16_t read();
    virtual ~Sensor();
    int16_t last;
};
// sizeof(Sensor) == 8: vptr (4) + last (2) + padding (2);
// без virtual було б 2. Сама vtable в об’єкт не входить: вона одна на клас.
```

**Типові помилки:**

- Рахувати vtable на кожен об’єкт, а vptr – на клас: навпаки, таблиця одна на клас, а vptr є в кожному екземплярі.
- Не враховувати службові слоти й дві entries для virtual destructor, коли оцінюють ROM.
- Вважати, що vptr обов’язково один і завжди 4 байти: розмір залежить від target, а множинне успадкування може додати ще.
