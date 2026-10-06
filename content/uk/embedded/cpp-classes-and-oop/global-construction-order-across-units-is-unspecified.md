---
id: emb-cppoop-0010
title: "Trap: чому залежність між глобальними об’єктами у різних `.cpp` небезпечна?"
description: "Стандарт C++ не визначає порядок конструювання глобалів між translation units (static initialization order fiasco)."
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
  - source_id: cpp-draft-basic-start-dynamic
    title: "C++ working draft: Dynamic initialization of non-block variables ([basic.start.dynamic])"
    url: https://eel.is/c++draft/basic.start.dynamic
    accessed: 2026-10-06
    kind: spec
    version: "working draft"
    applicability: "Визначає порядок dynamic initialization: у межах однієї translation unit – за порядком визначень; для змінних, визначених у різних translation units, упорядкування немає (indeterminately sequenced, якщо немає інших потоків). Для inline-змінних і специалізацій шаблонів правила інші (partially-ordered, unordered). Не стосується порядку виклику в конкретному startup-коді."
  - source_id: cpp-draft-basic-start-static
    title: "C++ working draft: Static initialization ([basic.start.static])"
    url: https://eel.is/c++draft/basic.start.static
    accessed: 2026-10-06
    kind: spec
    version: "working draft"
    applicability: "Каже, що змінна зі static storage duration або constant-initialized, або zero-initialized, і що вся static initialization строго передує будь-якій dynamic initialization."
  - source_id: cpp-draft-basic-life
    title: "C++ working draft: Object lifetime ([basic.life])"
    url: https://eel.is/c++draft/basic.life
    accessed: 2026-10-06
    kind: spec
    version: "working draft"
    applicability: "Каже, що lifetime об’єкта починається, коли його ініціалізацію завершено, і що звернення до нестатичного члена чи виклик нестатичної member-функції через вказівник або glvalue до початку lifetime – undefined behavior. Не описує, що саме побачить програма в пам’яті."
  - source_id: cpp-draft-stmt-dcl
    title: "C++ working draft: Declaration statement ([stmt.dcl])"
    url: https://eel.is/c++draft/stmt.dcl
    accessed: 2026-10-06
    kind: spec
    version: "working draft"
    applicability: "Каже, що dynamic initialization block-змінної зі static storage duration виконується, коли керування вперше проходить її оголошення; паралельний вхід чекає завершення; рекурсивний вхід – undefined behavior."
  - source_id: cpp-draft-dcl-constinit
    title: "C++ working draft: The constinit specifier ([dcl.constinit])"
    url: https://eel.is/c++draft/dcl.constinit
    accessed: 2026-10-06
    kind: spec
    version: "working draft"
    applicability: "Каже, що змінна з constinit, яка мала б dynamic initialization, робить програму ill-formed, тож constinit гарантує ініціалізацію під час static initialization. Це C++20; у старіших стандартах specifier'а немає."
  - source_id: gcc-cxx-init-priority
    title: "GCC: C++ Attributes, init_priority"
    url: https://gcc.gnu.org/onlinedocs/gcc/C_002b_002b-Attributes.html#index-init_005fpriority
    accessed: 2026-10-06
    kind: official
    version: "current"
    applicability: "Каже, що в стандартному C++ порядок ініціалізації в одній translation unit відповідає порядку визначень, а між translation units гарантій немає; атрибут init_priority – розширення GNU C++ для керування порядком, і деякі таргети його відхиляють з помилкою."
  - source_id: gcc-cxx-threadsafe-statics
    title: "GCC: C++ Dialect Options, -fno-threadsafe-statics"
    url: https://gcc.gnu.org/onlinedocs/gcc/C_002b_002b-Dialect-Options.html#index-fthreadsafe-statics
    accessed: 2026-10-06
    kind: official
    version: "current"
    applicability: "Каже, що -fno-threadsafe-statics прибирає додатковий код потокобезпечної ініціалізації local static за C++ ABI і трохи зменшує розмір коду, якщо потокобезпека не потрібна. Точного виграшу в байтах не наводить."
  - source_id: arm-cpp-abi
    title: "C++ ABI for the Arm Architecture (CPPABI32)"
    url: https://raw.githubusercontent.com/ARM-software/abi-aa/main/cppabi32/cppabi32.rst
    accessed: 2026-10-06
    kind: spec
    version: null
    applicability: "У розділі Top-level static object construction каже, що ABI не специфікує спосіб керувати порядком ініціалізації translation units. Це ABI для Arm; інші таргети можуть мати власні правила."
---

## Short answer

<span class="warn">Стандарт C++ не визначає порядок конструювання глобалів між translation units</span> (static initialization order fiasco): гарантовано лише порядок у межах одного TU.[^cpp-draft-basic-start-dynamic][^gcc-cxx-init-priority]

Якщо глобал з `a.cpp` у своєму constructor використовує глобал з `b.cpp`, той може бути ще не сконструйований, а звернення до об’єкта до початку його lifetime – undefined behavior.[^cpp-draft-basic-life]

Захист: уникай між-модульних залежностей глобалів; використовуй function-local static (lazy init при першому проході керування через оголошення),[^cpp-draft-stmt-dcl] `constinit`-об’єкти (C++20)[^cpp-draft-dcl-constinit] або явну init-послідовність.

## Detailed explanation

У межах однієї translation unit dynamic initialization глобалів іде в порядку їхніх визначень. Для змінних із різних translation units стандарт нічого не впорядковує: їхні ініціалізації indeterminately sequenced, тобто одна відбувається перед іншою, але в якому порядку – не сказано.[^cpp-draft-basic-start-dynamic] GCC документує те саме,[^gcc-cxx-init-priority] а Arm C++ ABI не пропонує способу керувати порядком між translation units.[^arm-cpp-abi] Фактичний порядок – деталь реалізації, тож він може змінитися після додавання файлу чи іншого порядку лінкування.

Чому це баг, а не лише «невідомо що перше». Вся static initialization (нулі й constant initialization) строго передує будь-якій dynamic,[^cpp-draft-basic-start-static] тому «ще не сконструйований» глобал – це не сміття, а нульові байти: нульові вказівники, нульові лічильники, нульовий vptr. Але lifetime об’єкта класу починається, лише коли його ініціалізацію завершено, а виклик нестатичної member-функції чи доступ до члена до цього моменту – undefined behavior.[^cpp-draft-basic-life] Тож помилка може «спрацьовувати» на одній збірці й ламатися на іншій.

Виправлень кілька. Function-local static ініціалізується, коли керування вперше проходить його оголошення, тож залежність створюється за першим викликом, незалежно від порядку TU;[^cpp-draft-stmt-dcl] ціна – guard-код (GCC дозволяє прибрати додатковий код потокобезпечної ініціалізації через `-fno-threadsafe-statics`, якщо потоків немає[^gcc-cxx-threadsafe-statics]) і реєстрація деструктора, якщо він non-trivial (див. `qid:emb-cppoop-0009`). `constinit` (C++20) робить програму ill-formed, якщо змінна потребувала б dynamic initialization, тож об’єкт гарантовано готовий ще на стадії static initialization.[^cpp-draft-dcl-constinit] Третій шлях – зробити конструктори глобалів тривіальними й викликати `init()` із `main()` у відомому порядку (див. `qid:emb-cppoop-0011`). Нарешті, GNU C++ має атрибут `init_priority`, але це розширення, і деякі таргети його відхиляють.[^gcc-cxx-init-priority]

```cpp
// clock.cpp
Clock& sys_clock() {
    static Clock instance;     // constructed the first time control reaches here
    return instance;
}

// driver.cpp
Driver::Driver() {
    sys_clock().enable();      // safe regardless of translation-unit order
}
Driver driver;
```

**Типові помилки:**

- Перевірити на одній збірці й вважати порядок «з’ясованим»: після зміни складу файлів чи порядку лінкування він може стати іншим.
- Переносити правила звичайних глобалів на inline-змінні та статичні члени шаблонів: для них порядок partially-ordered або unordered.[^cpp-draft-basic-start-dynamic]
- Лишити перший виклик function-local static на ISR: паралельний вхід у таку ініціалізацію чекає її завершення,[^cpp-draft-stmt-dcl] тож краще викликати її вперше з `main()`.
- Покладатися на `init_priority` як на переносне рішення.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
