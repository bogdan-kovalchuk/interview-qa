---
id: emb-cppoop-0006
title: "Навіщо потрібен member initialization list у конструкторі?"
description: "Ініціалізує бази й члени до входу в тіло конструктора; для const і reference членів зі значенням із параметрів конструктора – єдиний шлях."
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
  - source_id: cpp-draft-class-base-init
    title: "C++ working draft: Initializing bases and members ([class.base.init])"
    url: https://eel.is/c++draft/class.base.init
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Визначає порядок ініціалізації (бази, потім члени в порядку оголошення, потім тіло), роль default member initializer і заборону прив’язувати temporary до reference-члена; не оцінює ефективність."
  - source_id: cpp-draft-dcl-type-cv
    title: "C++ working draft: The cv-qualifiers ([dcl.type.cv])"
    url: https://eel.is/c++draft/dcl.type.cv
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що визначення const-об’єкта чи підоб’єкта має мати ініціалізатор або підлягати default-initialization, і що зміна const-підоб’єкта є помилкою."
  - source_id: cpp-draft-dcl-init-ref
    title: "C++ working draft: References ([dcl.init.ref])"
    url: https://eel.is/c++draft/dcl.init.ref
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що reference має бути ініціалізований і не може бути переприв’язаний; для члена класу ініціалізатор у самому оголошенні можна опустити."
  - source_id: cpp-draft-expr-assign
    title: "C++ working draft: Assignment and compound assignment operators ([expr.assign])"
    url: https://eel.is/c++draft/expr.assign
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Вимагає modifiable lvalue як лівий операнд присвоєння; звідси помилка присвоєння const-члену в тілі конструктора."
  - source_id: cppcg-c47-member-init-order
    title: "C++ Core Guidelines: C.47 – Define and initialize data members in the order of member declaration"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c47-define-and-initialize-data-members-in-the-order-of-member-declaration
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Настанова з прикладом помилки через порядок у списку; не є вимогою мови."
  - source_id: cppcg-c49-init-not-assign
    title: "C++ Core Guidelines: C.49 – Prefer initialization to assignment in constructors"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c49-prefer-initialization-to-assignment-in-constructors
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Каже, що ініціалізація може бути елегантнішою й ефективнішою за default-конструювання з наступним присвоєнням і запобігає використанню до встановлення; приклад – клас std::string, для скалярів вигоду не стверджує."
  - source_id: gcc-cpp-dialect-options
    title: "GCC 16.1.0: Options Controlling C++ Dialect (-Wreorder)"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/C_002b_002b-Dialect-Options.html#index-Wreorder
    accessed: 2026-10-06
    kind: official
    version: "16.1.0"
    applicability: "Документує -Wreorder: попередження, коли порядок mem-initializer не збігається з порядком виконання; увімкнено через -Wall. Специфічно для GCC."
---

## Question code

```c
Gpio(uint32_t base, uint8_t pin)
  : odr_{(volatile uint32_t*)(base + 0x14)}, pin_{pin} {}
```

## Short answer

**Ініціалізує бази й члени до входу в тіло конструктора, тож `const` і reference члени, значення яких надходить із параметрів, можна задати лише тут.**[^cpp-draft-class-base-init] У тілі `pin_ = pin` було б присвоєнням, і воно не компілюється: ліва частина має бути modifiable lvalue.[^cpp-draft-expr-assign] Для сталих значень замість списку підійде default member initializer. Для класових членів прямий ініціалізатор також може бути ефективнішим за «default + присвоєння».[^cppcg-c49-init-not-assign] Члени ініціалізуються в порядку оголошення в класі, а не в порядку списку.[^cpp-draft-class-base-init]

## Detailed explanation

Створення об’єкта проходить у чіткому порядку: спочатку віртуальні й прямі бази, потім нестатичні члени в порядку їх оголошення в класі, і лише тоді виконується тіло конструктора.[^cpp-draft-class-base-init] Тому до першого рядка тіла кожен член уже має бути ініціалізований, а mem-initializer-list – це місце, де ви вказуєте, чим саме. Для `const`-члена це критично: визначення об’єкта чи підоб’єкта з `const`-типом має мати ініціалізатор або підлягати default-initialization,[^cpp-draft-dcl-type-cv] а reference взагалі має бути ініціалізований і потім не може бути переприв’язаний.[^cpp-draft-dcl-init-ref] У тілі конструктора члени вже існують, тож `pin_ = pin;` – це не ініціалізація, а присвоєння, яке для `const uint8_t pin_` не компілюється.[^cpp-draft-expr-assign]

Твердження «єдиний спосіб» точне лише для значень, що надходять із параметрів. Якщо значення відоме наперед, `const`- чи reference-член можна задати default member initializer у самому оголошенні (`const uint8_t pin_ = 5;`); коли для члена є й він, і mem-initializer, діє mem-initializer, а default member initializer ігнорується.[^cpp-draft-class-base-init] Список також потрібен, коли член чи база класового типу не мають default-конструктора: без явного ініціалізатора код не скомпілюється.[^cpp-draft-class-base-init] У прикладі з питання `odr_` і `pin_` отримують значення з `base` і `pin`, тож саме список є правильним місцем.

Щодо ефективності: Core Guidelines кажуть, що ініціалізація замість присвоєння в конструкторі може бути елегантнішою й ефективнішою, і що вона запобігає помилкам «використано до встановлення».[^cppcg-c49-init-not-assign] Основний виграш – для класових членів, які інакше спершу default-конструюються, а потім присвоюються. Для простих скалярів, як `uint8_t`, на це не варто покладатися без перевірки асемблера.

Окрема пастка – порядок. Члени ініціалізуються в порядку оголошення, незалежно від порядку в списку,[^cpp-draft-class-base-init] тож «логічна» послідовність у списку нічого не змінює. Ілюстративний приклад із Core Guidelines:[^cppcg-c47-member-init-order]

```cpp
class Foo {
  int m1;
  int m2;
public:
  Foo(int x) : m2{x}, m1{++x} {}   // m1 ініціалізується першим
};
// Foo f(1): m1 == m2 == 2, а не m2 == 1
```

GCC попереджає про такий розбіг прапорцем `-Wreorder`, який вмикає `-Wall`.[^gcc-cpp-dialect-options]

**Типові помилки:**

- Писати `pin_ = pin;` у тілі для `const` чи reference члена замість запису у списку.
- Писати список в іншому порядку, ніж оголошено члени, і залежати від порядку: один член використовує інший, ще не ініціалізований.
- Прив’язувати reference-член у mem-initializer до тимчасового об’єкта: це ill-formed.[^cpp-draft-class-base-init]
- Вважати, що список завжди швидший: для скалярів різницю дає лише асемблер.

## Sources

<!-- generated from frontmatter -->
