---
id: emb-cppoop-0005
title: "Чому методи доступу до апаратури часто позначають `const`, хоча вони змінюють регістр?"
description: "const стосується логічного стану об’єкта (його полів), а не апаратури, на яку вказує його вказівник."
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
  - source_id: cpp-draft-expr-ref
    title: "C++ working draft: Class member access ([expr.ref])"
    url: https://eel.is/c++draft/expr.ref
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Визначає тип виразу E1.E2 для нестатичного члена: cv-кваліфікація об’єкта додається до типу члена (крім mutable); не стосується того, на що вказує вказівник-член."
  - source_id: cpp-draft-dcl-type-cv
    title: "C++ working draft: The cv-qualifiers ([dcl.type.cv])"
    url: https://eel.is/c++draft/dcl.type.cv
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що const-кваліфікований шлях доступу не може змінити об’єкт, а зміна const-об’єкта – undefined behavior; пояснює різницю між const-вказівником і вказівником на const. Не визначає, який метод варто позначати const."
  - source_id: cpp-draft-expr-assign
    title: "C++ working draft: Assignment and compound assignment operators ([expr.assign])"
    url: https://eel.is/c++draft/expr.assign
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Вимагає modifiable lvalue як лівий операнд присвоєння й складеного присвоєння; звідси помилка компіляції при зміні поля в const-методі."
  - source_id: cppcg-con2-const-members
    title: "C++ Core Guidelines: Con.2 – By default, make member functions const"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#con2-by-default-make-member-functions-const
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Рекомендація проєктування: позначати метод const, якщо він не змінює спостережуваний стан об’єкта; прямо зауважує, що const-метод може змінювати те, що доступне через вказівник-член. Це настанова, а не вимога мови."
---

## Short answer

**`const` стосується логічного стану об’єкта (його полів), а не апаратури.** У `const`-методі члени об’єкта стають `const`, тож `odr_` має тип `volatile uint32_t *const`: незмінний сам вказівник, але не те, на що він вказує, і запис у регістр через нього дозволений.[^cpp-draft-expr-ref][^cpp-draft-dcl-type-cv] Core Guidelines радять позначати метод `const`, якщо він не змінює спостережуваний стан об’єкта, і прямо допускають зміну через вказівник-член.[^cppcg-con2-const-members] Чи вважати запис у регістр зміною «стану» об’єкта-handle – рішення дизайну, а не вимога мови.

## Detailed explanation

Кваліфікатор `const` після списку параметрів змінює тип `this` на «вказівник на `const X`». Через це кожен нестатичний член, до якого звертаються в тілі методу, набуває `const`: за правилом доступу до члена тип виразу `E1.E2` отримує cv-кваліфікацію об’єкта, якщо член не `mutable`.[^cpp-draft-expr-ref] Тому присвоїти полю такого об’єкта в `const`-методі не вийде: ліва частина присвоєння має бути modifiable lvalue,[^cpp-draft-expr-assign] а тут вона `const`. Так `const` захищає саме байти об’єкта `Gpio` – вказівник і номер піна.

Регістр у цей захист не потрапляє. Поле `odr_` має тип `volatile uint32_t *const`, тобто «constant pointer to volatile `uint32_t`». Верхній `const` робить незмінним сам вказівник, а `uint32_t`, на який він вказує, лишається не `const`. Стандарт каже, що саме const-кваліфікований шлях доступу не може змінити об’єкт;[^cpp-draft-dcl-type-cv] шлях `*odr_` такого не має, отже `*odr_ |= mask` коректний. Для порівняння, `const volatile uint32_t *` описував би read-only регістр, у який через цей вказівник писати не можна. Зверніть увагу: у `const`-методі кваліфікація додається до самого вказівника, тож `volatile uint32_t *odr_` без верхнього `const` теж дозволив би запис.

Ось ілюстративний контраст – що `const` ловить, а що ні:

```cpp
class Gpio {
  volatile uint32_t *const odr_;   // адреса регістра
public:
  explicit Gpio(volatile uint32_t *odr) : odr_{odr} {}
  void set() const { *odr_ |= 1u; }   // OK: міняється регістр, не поля *this
};

class Shadowed {
  uint32_t shadow_ = 0;               // копія значення прямо в об’єкті
public:
  void set() const { shadow_ |= 1u; } // помилка: shadow_ у const-методі const
};
```

Чи варто позначати `set()` як `const`, – питання дизайну. Core Guidelines формулюють критерій так: метод має бути `const`, якщо він не змінює спостережуваний стан об’єкта, і окремо зауважують, що `const`-метод може змінювати те, що доступне через вказівник-член.[^cppcg-con2-const-members] Об’єкт `Gpio` – це handle (адреса й номер піна), а рівень на виводі є станом апаратури; на цьому тримається аргумент «логічного const». Він дає змогу передавати handle як `const Gpio&`. Проти нього: `const` сигналізує читачу «нічого не змінюється», хоча виклик змінює вихід. Мова припускає обидва варіанти, тож це конвенція проєкту. З боку мови це безпечно навіть для `const Gpio`: undefined behavior виникає, коли змінюють const-об’єкт чи його підоб’єкт,[^cpp-draft-dcl-type-cv] а регістр підоб’єктом `Gpio` не є.

**Типові помилки:**

- Вважати `const`-метод «чистою» функцією без побічних ефектів: `const` обіцяє лише незмінність полів, а не відсутність запису в регістр чи пам’ять за вказівником.
- Позначати `const` метод, що читає статусний регістр із побічним ефектом (наприклад, скидання прапорців читанням – перевір datasheet): викликач вважатиме його безпечним.
- Плутати `volatile uint32_t *const` (константний вказівник на змінюваний регістр) і `const volatile uint32_t *` (вказівник на регістр лише для читання).
- Обходити помилку компіляції через `const_cast` замість того, щоб переглянути, чи метод справді має бути `const`.

## Sources

<!-- generated from frontmatter -->
