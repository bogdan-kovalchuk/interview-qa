---
id: emb-cppoop-0014
title: "Порахуй спрощену вартість: 3 класи, по 5 virtual-методів. Скільки ROM на vtables?"
description: "Оцінка лише для entries: 60 байт ROM (read-only memory), тобто 3 vtables × 5 entries × 4 байти на 32-bit target; реальна vtable більша через службові слоти ABI."
track: embedded
section: cpp-classes-and-oop
level: junior
type: mechanism
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
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
    accessed: 2026-10-06
    kind: spec
    version: null
    applicability: "У розділах 2.4 і 2.5 описує vtable як послідовність offset-ів і function pointer-ів із розміром та вирівнюванням pointer-а, обов’язкові слоти offset-to-top і typeinfo pointer, entry на кожну virtual-функцію, пару entries для virtual destructor і vptr на offset 0 dynamic class без primary base. Це ABI, а не стандарт мови; конкретний розмір pointer-а задає платформа."
  - source_id: arm-cpp-abi
    title: "C++ ABI for the Arm Architecture (CPPABI32)"
    url: https://raw.githubusercontent.com/ARM-software/abi-aa/main/cppabi32/cppabi32.rst
    accessed: 2026-10-06
    kind: spec
    version: null
    applicability: "Називає generic (Itanium) C++ ABI базовим стандартом для Arm; у зведенні відмінностей від нього layout vtable (розділ 2.5) не згадано, тож для Arm відхилень у layout vtable там не заявлено. Не визначає, де лінкер розміщує vtable."
---

## Short answer

**Оцінка лише для function-pointer entries: 60 байт ROM (read-only memory)**: 3 vtables × 5 entries × 4 байти на 32-bit target.

Реальна vtable в Itanium-подібному ABI має ще два слоти (offset-to-top і typeinfo pointer), тож вийде 3 × (5 + 2) × 4 = 84 байти, а virtual destructor додає ще слот.[^itanium-cxx-abi] У RAM (random-access memory) додатково – vptr на кожен об’єкт: 100 об’єктів × 4 байти = 400 байт RAM лише на vptr.

Правило: vtable рахуй приблизно на клас, vptr – на екземпляр; на малому MCU (microcontroller unit) вартість vptr помітна, коли об’єктів багато.

## Detailed explanation

Спрощений розрахунок виходить із трьох припущень: кожен із трьох класів має власну vtable, у кожній по п’ять virtual-функцій, а pointer на 32-bit target займає 4 байти. Тоді entries займають `3 * 5 * 4 = 60` байт. Це оцінка знизу для самих function pointer-ів, а не повний розмір таблиць: vtable в Itanium C++ ABI – це послідовність offset-ів і pointer-ів із розміром і вирівнюванням pointer-а, а Arm C++ ABI бере цей ABI за базу й не заявляє іншого layout vtable.[^itanium-cxx-abi][^arm-cpp-abi]

Різниця виникає зі службових слотів. У таблиці завжди є offset-to-top і typeinfo pointer, тому на кожен клас додається ще два слоти, і маємо `3 * (5 + 2) * 4 = 84` байти.[^itanium-cxx-abi] Якщо один із п’яти методів – virtual destructor, він займає не один слот, а пару (complete object destructor і deleting destructor), тож таблиця стає ще на 4 байти більшою. Для множинного успадкування додаються ще secondary vtables. Точний розмір видно в map file або через `nm -S` на своєму тулчейні.

RAM рахується інакше. Таблиці лежать поза об’єктами, а кожен об’єкт зберігає один vptr незалежно від кількості virtual-методів:[^itanium-cxx-abi] додавання шостого методу збільшує ROM на один слот на клас, але не збільшує `sizeof` об’єкта. Для 100 об’єктів маємо `100 * 4 = 400` байт RAM, тобто більше, ніж 60 чи 84 байти ROM. Якщо порівнювати лише розміри, vptr-и зрівнюються з таблицями вже приблизно на 21 об’єкті (`84 / 4 = 21`); а RAM на малому MCU зазвичай дефіцитніша за flash.

```cpp
// Illustrative: оцінка для 32-bit target
constexpr unsigned p = 4, classes = 3, methods = 5;
constexpr unsigned entries_only = classes * methods * p;        // 60
constexpr unsigned with_slots   = classes * (methods + 2) * p;  // 84
constexpr unsigned vptr_ram     = 100 * p;                      // 400
```

Ця арифметика не враховує код: виклик через vtable і запис vptr у конструкторі теж коштують flash і такти. Вона також нічого не каже про те, чи лінкер справді поклав таблиці у flash.

**Типові помилки:**

- Називати 60 байт повним розміром vtables і забувати про offset-to-top, typeinfo pointer і destructor entries.
- Множити розмір vtable на кількість об’єктів, а не на кількість класів.
- Вважати, що кожен новий virtual-метод збільшує RAM кожного об’єкта: росте ROM таблиць, а об’єкт лишається з одним vptr.

## Sources

<!-- generated from frontmatter -->
