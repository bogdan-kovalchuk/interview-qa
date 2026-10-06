---
id: emb-cppoop-0026
title: "Trap: бачиш null vptr у глобального об’єкта – у чому причина?"
description: "Найчастіше глобальні конструктори не виконано – startup не пройшов .init_array."
track: embedded
section: cpp-classes-and-oop
level: junior
type: pitfall
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
  - source_id: arm-cpp-abi
    title: "C++ ABI for the Arm Architecture (CPPABI32)"
    url: https://raw.githubusercontent.com/ARM-software/abi-aa/main/cppabi32/cppabi32.rst
    accessed: 2026-10-06
    kind: spec
    version: null
    applicability: "У розділі Top-level static object construction: кожна translation unit дає фрагмент constructor vector у секції .init_array (SHT_INIT_ARRAY), елемент – адреса функції void(void), що конструює глобальні об’єкти цієї TU; run-time support code проходить вектор за зростанням адрес; порядок між TU ABI не задає. Це ABI для Arm; інші архітектури й тулчейни можуть відрізнятися."
  - source_id: cpp-draft-basic-start-static
    title: "C++ working draft: Static initialization ([basic.start.static])"
    url: https://eel.is/c++draft/basic.start.static
    accessed: 2026-10-06
    kind: spec
    version: "working draft"
    applicability: "Каже, що змінна зі static storage duration або constant-initialized, або zero-initialized, і що вся static initialization строго передує будь-якій dynamic initialization. Про vptr, секції чи startup не каже."
  - source_id: cpp-draft-basic-start-dynamic
    title: "C++ working draft: Dynamic initialization of non-block variables ([basic.start.dynamic])"
    url: https://eel.is/c++draft/basic.start.dynamic
    accessed: 2026-10-06
    kind: spec
    version: "working draft"
    applicability: "Каже, що implementation-defined, чи dynamic initialization змінної зі static storage duration виконується до першого оператора main, чи відкладається. Не визначає механізм виклику (секції, startup-код)."
  - source_id: itanium-abi-ctor-vptr
    title: "Itanium C++ ABI: Virtual tables During Object Construction"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html#vtable-ctor-general
    accessed: 2026-10-06
    kind: spec
    version: null
    applicability: "У розділі 2.6.1 каже, що vptr об’єкта зазвичай виставляє конструктор класу (на vtable цього класу). Це ABI, а не стандарт мови; інші ABI можуть відрізнятися в деталях."
---

## Short answer

<span class="warn">Найчастіша причина – startup не виконав конструктори глобальних об’єктів із `.init_array`.</span>[^arm-cpp-abi] Об’єкт, якому потрібна dynamic initialization, без цього лишається лише zero-initialized, а vptr поліморфного об’єкта зазвичай виставляє саме конструктор,[^cpp-draft-basic-start-static][^itanium-abi-ctor-vptr] тож перший virtual-виклик іде за нульовим vptr – undefined behavior, на практиці зазвичай fault. Захист: переконайся, що startup проходить `.init_array` перед `main()`; null vptr буває й тоді, коли об’єкт використали до виконання його конструктора.

## Detailed explanation

Об’єкт зі static storage duration спершу проходить static initialization: або constant initialization, або zero-initialization. Конструктор, який не є constant expression, виконується пізніше, під час dynamic initialization, і вся static initialization строго передує будь-якій dynamic.[^cpp-draft-basic-start-static] Vptr поліморфного об’єкта зазвичай виставляє конструктор: кожен конструктор у ланцюгу класів записує в об’єкт адресу vtable свого класу.[^itanium-abi-ctor-vptr] Тому об’єкт, чий конструктор ще не виконався, лежить у зануленій пам’яті (типово `.bss`), і слот vptr у ньому нульовий.

Хто виконує ці конструктори, залежить від платформи. За Arm ABI кожна translation unit дає фрагмент у секції `.init_array` – адреси функцій `void(void)`, що конструюють її глобальні об’єкти, а run-time support code проходить цей вектор за зростанням адрес; порядок між translation units ABI не задає.[^arm-cpp-abi] Стандарт лишає на розсуд реалізації, чи dynamic initialization відбудеться до першого оператора `main`, чи буде відкладена.[^cpp-draft-basic-start-dynamic] На bare-metal цим «run-time support code» є ваш startup або бібліотека, яку він викликає. Якщо прохід пропущено (власний `Reset_Handler`, що одразу стрибає в `main`, або startup, портований із C-проєкту), конструктори не виконуються, а C-код при цьому працює, тож помилку легко не помітити (докладніше в `qid:emb-cppoop-0008`).

Не кожен null vptr означає пропущений `.init_array`. Якщо конструктор `constexpr` і об’єкт constant-initialized, vptr може бути записаний уже в образі, і виконувати нічого не треба. У прикладі GCC 13.3 (x86_64) кладе `d1` у `.bss`, а `c1` – у `.data` із готовим vptr. Є й інші причини: об’єкт використали раніше за його конструктор, бо порядок між translation units не заданий (`qid:emb-cppoop-0010`), або пам’ять об’єкта перезаписали (`memset`, вихід за межі сусіднього буфера). Тоді замість нуля там може бути й сміття.

```cpp
// Ілюстративний фрагмент.
struct Dev { constexpr Dev() = default; virtual int id() const { return 1; } int x = 0; };
struct Dyn : Dev { Dyn(int v); };                           // конструктор не constexpr
struct Cst : Dev { constexpr Cst(int v) { x = v; } };

Dyn d1(5);   // .bss: нулі, vptr == 0, доки не виконається конструктор з .init_array
Cst c1(7);   // .data: vptr і x задано вже в образі, .init_array не потрібен
```

Наслідок для коду: virtual-виклик читає vptr, а потім слот vtable за адресою `vptr + зсув`. З нульовим vptr це undefined behavior; на практиці зазвичай маємо fault (на Cortex-M це часто HardFault) або перехід за випадковою адресою.

**Типові помилки:**

- Вважати, що причина завжди в `.init_array`: перевір ще constant initialization, використання до конструктора й затирання пам’яті.
- Викликати virtual-метод глобального об’єкта з конструктора іншого глобального об’єкта: порядок між translation units не визначений.
- Писати власний startup без проходу `.init_array` і не помітити цього, поки в C++ немає глобальних об’єктів із конструкторами.
- Лікувати симптом перевіркою `vptr != 0` замість того, щоб знайти, чому конструктор не виконався.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
