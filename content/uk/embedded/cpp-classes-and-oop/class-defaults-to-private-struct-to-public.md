---
id: emb-cppoop-0002
title: "Чим `class` відрізняється від `struct` у C++?"
description: "Головна відмінність – доступ за замовчуванням: class – private, struct – public."
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
  - source_id: cpp-draft-class-access-general
    title: "C++ working draft: [class.access.general] Member access control, General"
    url: https://eel.is/c++draft/class.access.general
    accessed: 2026-10-06
    kind: spec
    version: "working draft"
    applicability: "Підтверджує: члени класу, визначеного з class, за замовчуванням private, а визначеного з struct або union – public. Не стосується доступу до баз (це [class.access.base])."
  - source_id: cpp-draft-class-access-base
    title: "C++ working draft: [class.access.base] Accessibility of base classes and base class members"
    url: https://eel.is/c++draft/class.access.base
    accessed: 2026-10-06
    kind: spec
    version: "working draft"
    applicability: "Підтверджує: якщо для бази не вказано access-specifier, береться public для struct і private для class."
  - source_id: cpp-draft-class-prop
    title: "C++ working draft: [class.prop] Properties of classes"
    url: https://eel.is/c++draft/class.prop
    accessed: 2026-10-06
    kind: spec
    version: "working draft"
    applicability: "Визначає standard-layout клас: серед умов – однаковий access control для всіх нестатичних даних; standard-layout struct і class означені однаково, ключове слово не впливає."
  - source_id: cpp-core-guidelines
    title: "C++ Core Guidelines: C.2 (class or struct)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#rc-struct
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Правило C.2: class, якщо є інваріант, struct, якщо дані змінюються незалежно. Це конвенція стилю, а не вимога мови; сусіднє правило C.8 радить class, якщо є не-public член."
---

## Short answer

**Головна відмінність – доступ за замовчуванням: `class` – private, `struct` – public.**[^cpp-draft-class-access-general]

Так само відрізняється доступ до бази за замовчуванням: `class Derived : Base` успадковує private, а `struct Derived : Base` – public.[^cpp-draft-class-access-base] В іншому вони однакові: методи, конструктори й успадкування можливі в обох.

Правило: за C++ Core Guidelines `struct` – коли дані змінюються незалежно, `class` – коли є інваріант.[^cpp-core-guidelines]

## Detailed explanation

Ключові слова `class` і `struct` означають той самий вид типу, а відрізняються лише двома значеннями за замовчуванням. Перше – доступ до членів: у `class` вони private, а в `struct` (і в `union`) – public.[^cpp-draft-class-access-general] Друге – доступ до бази, коли `public`, `protected` чи `private` перед нею не написано: для `struct` береться public, для `class` – private.[^cpp-draft-class-access-base] Усе інше однаково: і той, і той тип може мати методи, конструктори, деструктор, шаблони, virtual-функції та успадкування.

Друга відмінність частіше ламає код. Якщо написати `class Derived : Base` без `public`, то `Base` стане private base: ззовні не спрацює неявне перетворення `Derived*` у `Base*`, а члени бази недоступні користувачам похідного класу. Така помилка зазвичай з’являється під час компіляції, але її легко прийняти за помилку в самому `Base`.

```cpp
class A  { int x; };      // x – private
struct B { int x; };      // x – public

class  D1 : B {};         // B – private base
struct D2 : B {};         // B – public base

void use(D1* d1, D2* d2)
{
    B* p2 = d2;           // OK
    // B* p1 = d1;        // помилка: B – private base класу D1
}
```

Ключове слово не впливає на розташування даних. Standard-layout означено однаково для struct і class, а серед його умов є однаковий access control для всіх нестатичних даних.[^cpp-draft-class-prop] Тому `struct`, у якій частину полів зроблено `private:`, уже не standard-layout, що важливо для сумісності з C і для накладення структури на регістри периферії.

Вибір між ключовими словами – справа конвенції. C++ Core Guidelines радять `class`, коли тип має інваріант, який підтримують конструктори й методи, і `struct`, коли дані змінюються незалежно одне від одного.[^cpp-core-guidelines] У embedded це зазвичай `struct` для кадрів повідомлень, конфігурацій і register maps та `class` для драйверів зі станом.

**Типові помилки:**

- Писати `class Derived : Base` і дивуватися, що `Base` – private base.
- Вважати `struct` швидшою чи «C-сумісною» лише за ключовим словом: на код і розташування даних воно не впливає.
- Додавати `private:` у `struct`, яка має відповідати C-структурі або регістровій карті, і втрачати standard-layout.

## Sources

<!-- generated from frontmatter -->
