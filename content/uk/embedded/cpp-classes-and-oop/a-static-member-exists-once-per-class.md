---
id: emb-cppoop-0028
title: "Що таке static member класу і де він живе?"
description: "Static data member – спільний для всіх екземплярів; існує в одному примірнику, а не в кожному об’єкті."
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
  - source_id: cpp-draft-class-static
    title: "C++ working draft: Static members ([class.static])"
    url: https://eel.is/c++draft/class.static
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що static data member не входить до підоб’єктів класу, що він існує в одному примірнику на всі об’єкти (для thread_local – по одному на потік), що оголошення non-inline static data member у класі не є визначенням і що inline static member є визначенням. Не визначає розміщення в секціях пам’яті."
  - source_id: cpp-draft-basic-stc-static
    title: "C++ working draft: Static storage duration ([basic.stc.static])"
    url: https://eel.is/c++draft/basic.stc.static
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що змінні, вперше оголошені зі static (і не thread-local), мають static storage duration, тобто пам’ять існує протягом усієї програми. Не говорить про секції .data чи .bss."
  - source_id: cpp-draft-dcl-inline-variable
    title: "C++ working draft: The inline specifier ([dcl.inline])"
    url: https://eel.is/c++draft/dcl.inline
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що inline-змінна з external linkage може бути визначена в кількох translation unit і є однією сутністю з однією адресою. Не стосується розміщення в секціях."
  - source_id: gcc-zero-bss
    title: "GCC 16.1.0: Optimize Options – -fno-zero-initialized-in-bss"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Optimize-Options.html
    accessed: 2026-10-06
    kind: official
    version: "16.1.0"
    applicability: "Описує типове розміщення нульово ініціалізованих globals у BSS в GCC та прапорець, що його змінює; не описує всі компілятори чи linkers."
---

## Question code

```cpp
class Counter {
  static uint32_t count_; // одна на клас
};
```

## Short answer

**Static data member належить класу, а не об’єкту:** один примірник спільний для всіх екземплярів (для `thread_local` – по одному на потік), і він не входить до підоб’єктів класу, тож не збільшує `sizeof`.[^cpp-draft-class-static] Він має static storage duration,[^cpp-draft-basic-stc-static] тому в GCC лежить поза об’єктом: у `.bss` для нульового початкового значення, інакше в data section.[^gcc-zero-bss] Non-inline static member визначається один раз поза класом; `inline static` є визначенням у самому класі.[^cpp-draft-class-static]

## Detailed explanation

Звичайний нестатичний член входить до кожного об’єкта: `sizeof` його враховує, і кожен екземпляр має власну копію. Static data member – інша сутність. За стандартом він не є частиною підоб’єктів класу, і якщо він не `thread_local`, існує одна копія, спільна для всіх об’єктів класу; зі `thread_local` буде по одній копії на потік.[^cpp-draft-class-static] Тому до нього звертаються через ім’я класу, `Counter::count_`, без жодного об’єкта, а після визначення він існує, навіть якщо жодного екземпляра ще не створено.[^cpp-draft-class-static]

Змінна зі static storage duration живе протягом усієї програми.[^cpp-draft-basic-stc-static] Мова при цьому нічого не каже про секції `.data` і `.bss`: це справа тулчейна. GCC за замовчуванням кладе нульово ініціалізовані змінні в BSS, якщо ціль підтримує такий розділ,[^gcc-zero-bss] решту – у data section; на bare-metal за підготовку обох областей до `main()` зазвичай відповідає startup-код. Тому «живе в `.data`/`.bss`» – типова практика, а не правило мови.

Оголошення non-inline static data member у класі не є визначенням, тож потрібне ще й визначення в namespace scope, рівно одне на програму (зазвичай в одному `.cpp`).[^cpp-draft-class-static] `inline static` об’єднує оголошення й визначення: така змінна може бути визначена в кількох translation unit і лишається однією сутністю з однією адресою,[^cpp-draft-dcl-inline-variable] тому її безпечно тримати в заголовку. Вона потребує режиму C++17 або новішого.

Ілюстративний приклад (компілюється з `-std=c++17`):

```cpp
#include <cstdint>

class Counter {
public:
  Counter() { ++count_; }
  ~Counter() { --count_; }
  static std::uint32_t alive() { return count_; }

private:
  static inline std::uint32_t count_ = 0;  // одна копія на програму
  std::uint8_t id_ = 0;                    // власне поле кожного об’єкта
};
// sizeof(Counter) не включає count_
```

Спільність означає спільний змінюваний стан. Якщо `count_` змінюють і основний код, і ISR, потрібен окремий захист (критична секція чи атомарний тип): `++` – це read-modify-write, а `volatile` атомарності не додає.

**Типові помилки:**

- Оголосити non-inline static data member і не визначити його в жодному `.cpp`: зазвичай це undefined reference під час лінкування.
- Визначити його в заголовку без `inline`: кожен translation unit дістане своє визначення, а має бути рівно одне.[^cpp-draft-class-static]
- Очікувати власну копію на кожен об’єкт або вважати, що зі `thread_local` копія все одно одна.
- Вважати лічильник на кшталт `count_` безпечним для ISR лише тому, що він `static`.

## Sources

<!-- generated from frontmatter -->
