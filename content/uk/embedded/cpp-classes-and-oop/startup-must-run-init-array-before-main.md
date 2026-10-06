---
id: emb-cppoop-0008
title: "Trap: коли запускаються глобальні конструктори і що має зробити startup?"
description: "Конструктори глобальних об’єктів викликає прохід по `.init_array`; на bare-metal його має виконати startup перед main()."
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
    applicability: "У розділі Top-level static object construction: кожна translation unit дає фрагмент constructor vector у секції .init_array (SHT_INIT_ARRAY), елемент – адреса функції void(void), що конструює глобальні об’єкти цієї TU; run-time support code проходить вектор за зростанням адрес; порядок між TU ABI не задає; елементи можуть бути й self-relative. Це ABI для Arm; інші архітектури й тулчейни можуть відрізнятися."
  - source_id: cpp-draft-basic-start-static
    title: "C++ working draft: Static initialization ([basic.start.static])"
    url: https://eel.is/c++draft/basic.start.static
    accessed: 2026-10-06
    kind: spec
    version: "working draft"
    applicability: "Каже, що змінна зі static storage duration або constant-initialized, або zero-initialized, і що вся static initialization строго передує будь-якій dynamic initialization. Не каже, хто й коли викликає dynamic initialization."
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
  - source_id: gnu-ld-manual-sections
    title: "GNU ld manual: SECTIONS and input section description"
    url: https://sourceware.org/binutils/docs/ld.html
    accessed: 2026-10-06
    kind: official
    version: "current"
    applicability: "Описує секції .init_array.NNNNN і .ctors.NNNNN (NNNNN пов’язане з GCC init_priority) та KEEP() для секцій, які не можна прибирати при --gc-sections (приклади – .init, .ctors). Не задає, який саме linker script має проєкт."
  - source_id: gcc-int-initialization
    title: "GCC Internals: How Initialization Functions Are Handled"
    url: https://gcc.gnu.org/onlinedocs/gccint/Initialization.html
    accessed: 2026-10-06
    kind: official
    version: "current"
    applicability: "Каже, що функції ініціалізації, які генерує компілятор, мають бути викликані до main, і що традиційні механізми GCC – секції .ctors/.dtors та .init, а за їх відсутності виклик __main. Не згадує .init_array."
---

## Short answer

<span class="warn">Конструктори глобальних об’єктів, яким потрібна dynamic initialization, виконують функції з секції `.init_array`; run-time support code (на bare-metal – твій startup) має пройти цей масив до `main()`.</span>[^arm-cpp-abi] Якщо цього не зробити, такий об’єкт лишається лише zero-initialized, а vptr поліморфного об’єкта зазвичай виставляє саме конструктор.[^cpp-draft-basic-start-static][^itanium-abi-ctor-vptr] Сам стандарт залишає на розсуд реалізації (implementation-defined), чи виконується ця ініціалізація до першого оператора `main()`.[^cpp-draft-basic-start-dynamic]

Захист: переконайся, що startup ітерує `.init_array` перед `main()`; це частий баг при портуванні C++ на голе залізо.

## Detailed explanation

Статична ініціалізація в C++ має дві стадії. Змінна зі static storage duration або ініціалізується константою (constant initialization, наприклад об’єкт із `constexpr` конструктором), або спершу заповнюється нулями; усе, що потребує виконання коду, отримує dynamic initialization – справжній виклик конструктора під час роботи програми. Стандарт вимагає, щоб уся static initialization (нулі й константи) відбулася раніше за будь-яку dynamic.[^cpp-draft-basic-start-static] Тому на bare-metal глобальний об’єкт із «живим» конструктором після копіювання `.data` і обнулення `.bss` – це ще лише нулі.

Хто викликає ці конструктори – питання ABI, а не мови. Arm C++ ABI вимагає, щоб кожна translation unit поклала в секцію `.init_array` (тип `SHT_INIT_ARRAY`) вказівники на функції `void(void)`, що конструюють її глобальні об’єкти, а run-time support code пройшов цей вектор за зростанням адрес і викликав кожну функцію; порядок між translation units ABI не задає.[^arm-cpp-abi] GNU ld знає також `.init_array.NNNNN` для `init_priority` та старіші `.ctors`,[^gnu-ld-manual-sections] але суть та сама: це масив вказівників, який хтось мусить пройти. На bare-metal цим «кимось» є твій startup-код (або glue з libc): linker script збирає секцію й дає символи її початку та кінця, а reset handler після ініціалізації `.data` і `.bss` викликає цикл. Секцію варто обгорнути в `KEEP()`, бо саме для секцій, які не можна прибирати, його призначено при `--gc-sections`.[^gnu-ld-manual-sections]

Стандарт не гарантує навіть того, що dynamic initialization виконається до першого оператора `main()`: це implementation-defined, її дозволено відкласти.[^cpp-draft-basic-start-dynamic] Але тулчейни задумані так, що згенеровані функції ініціалізації викликаються до `main`,[^gcc-int-initialization] тож «до `main()`» – це практична вимога до startup-коду, а не гарантія мови. Якщо конструктори чіпають периферію, цикл треба запускати після налаштування тактування, але до вмикання переривань, чиї обробники користуються цими об’єктами.

Найвідоміший наслідок пропущеного циклу – vptr. За Itanium C++ ABI vptr виставляє конструктор класу;[^itanium-abi-ctor-vptr] у `.bss` він нульовий, тож перший virtual-виклик піде за нульовою адресою, і зазвичай це закінчується fault. Ілюстративний цикл startup-коду (імена символів задає linker script):

```c
extern void (*__init_array_start[])(void);
extern void (*__init_array_end[])(void);

static void call_static_constructors(void)
{
    for (void (**fn)(void) = __init_array_start; fn < __init_array_end; ++fn) {
        (*fn)();
    }
}
```

Цей варіант припускає, що елементи вектора – абсолютні адреси; Arm C++ ABI допускає й self-relative елементи, і тоді обхід інший.[^arm-cpp-abi]

**Типові помилки:**

- Узяти startup від C-проєкту без циклу по `.init_array`: глобальні C++-об’єкти «працюють», доки не знадобиться vptr чи непорожній стан.
- Не захистити `.init_array` через `KEEP()` у linker script зі `--gc-sections`.
- Викликати цикл до ініціалізації `.data` і `.bss` або до налаштування тактування, коли конструктор уже чіпає периферію.
- Покладатися на порядок конструювання глобалів між різними `.cpp` (див. `qid:emb-cppoop-0010`).

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
