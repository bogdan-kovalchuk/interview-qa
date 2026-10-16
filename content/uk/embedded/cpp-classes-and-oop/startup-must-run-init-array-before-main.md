---
id: emb-cppoop-0008
title: "Trap: коли запускаються глобальні конструктори і що має зробити startup?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: arm-cpp-abi
    title: "C++ ABI for the Arm Architecture (CPPABI32)"
    url: https://raw.githubusercontent.com/ARM-software/abi-aa/main/cppabi32/cppabi32.rst
  - source_id: cpp-draft-basic-start-static
    title: "C++ working draft: Static initialization ([basic.start.static])"
    url: https://eel.is/c++draft/basic.start.static
  - source_id: cpp-draft-basic-start-dynamic
    title: "C++ working draft: Dynamic initialization of non-block variables ([basic.start.dynamic])"
    url: https://eel.is/c++draft/basic.start.dynamic
  - source_id: itanium-abi-ctor-vptr
    title: "Itanium C++ ABI: Virtual tables During Object Construction"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html#vtable-ctor-general
  - source_id: gnu-ld-manual-sections
    title: "GNU ld manual: SECTIONS and input section description"
    url: https://sourceware.org/binutils/docs/ld.html
  - source_id: gcc-int-initialization
    title: "GCC Internals: How Initialization Functions Are Handled"
    url: https://gcc.gnu.org/onlinedocs/gccint/Initialization.html
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
- Покладатися на порядок конструювання глобалів між різними `.cpp` (див. qid:emb-cppoop-0010).
