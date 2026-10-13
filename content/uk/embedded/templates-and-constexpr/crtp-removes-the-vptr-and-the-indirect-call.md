---
id: emb-tmplcx-0012
title: "Які переваги CRTP над virtual dispatch?"
description: "Немає обов’язкового vptr (virtual pointer), немає indirect call і простіше аналізувати WCET (worst-case execution time)."
track: embedded
section: templates-and-constexpr
level: junior
type: concept
tags: []
status: published
updated: 2026-10-13
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
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-13; це джерело не є доказом тверджень."
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
    accessed: 2026-10-13
    kind: spec
    version: null
    applicability: "Визначає dynamic class (з virtual-функціями чи virtual-базами) як клас, що потребує virtual table pointer; отже клас без них його не потребує. Це ABI, а не стандарт мови: інші ABI можуть відрізнятися в деталях."
  - source_id: cpp-draft-class-virtual
    title: "C++ working draft: Virtual functions ([class.virtual])"
    url: https://eel.is/c++draft/class.virtual
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Примітка в розділі каже, що виклик virtual-функції визначається dynamic type об’єкта, а виклик non-virtual – static type вказівника чи посилання. Механізм vptr/vtable тут не заданий."
  - source_id: cpp-draft-temp-inst
    title: "C++ working draft: Implicit instantiation ([temp.inst])"
    url: https://eel.is/c++draft/temp.inst
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що специфікація шаблону функції чи member-функції інстанціюється, коли її визначення потрібне; неявна інстанціація класового шаблону інстанціює лише оголошення членів. Про розмір коду не йдеться."
  - source_id: cpp-draft-expr-static-cast
    title: "C++ working draft: Static cast ([expr.static.cast])"
    url: https://eel.is/c++draft/expr.static.cast
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Визначає, що static_cast вказівника на base у вказівник на похідний клас коректний, лише якщо цей base справді є підоб’єктом об’єкта похідного типу; інакше undefined behavior."
---

## Short answer

**Немає обов’язкового vptr (virtual pointer), немає indirect call і простіше аналізувати WCET (worst-case execution time).** Клас без virtual-функцій і virtual-баз за Itanium ABI не потребує vptr,[^itanium-cxx-abi] а виклик non-virtual функції визначається статичним типом, тож він прямий.[^cpp-draft-class-virtual] Розмір vptr залежить від ABI (application binary interface) і ширини вказівника.

Правило: CRTP – коли тип відомий на етапі компіляції; virtual – коли тип обирається під час виконання (плагіни, динамічне завантаження драйверів).

## Detailed explanation

Virtual-функція викликається через механізм, який стандарт описує поведінково: виклик визначається dynamic type об’єкта, а не типом вказівника.[^cpp-draft-class-virtual] Конкретну реалізацію задає ABI. В Itanium ABI клас із virtual-функціями чи virtual-базами є dynamic class і потребує vptr, тобто вказівника на таблицю віртуальних функцій.[^itanium-cxx-abi] Типова реалізація читає vptr з об’єкта, бере адресу з таблиці і викликає функцію через неї. Тому такий об’єкт несе додаткове поле, а цільова адреса в загальному випадку відома лише під час виконання.

CRTP (curiously recurring template pattern) задає базу `Base<Derived>`, яка викликає `static_cast<Derived*>(this)->impl()`. Тип `Derived` відомий компілятору, тож `impl` є невіртуальним викликом: його ціль визначається статичним типом, а не динамічним, і компілятор може вбудувати його в тіло функції.[^cpp-draft-class-virtual] Базовий клас без virtual-функцій не має vptr, тож об’єкт не отримує поля для диспетчеризації.[^itanium-cxx-abi] Водночас `static_cast` коректний лише тоді, коли об’єкт справді є `Derived`; інакше поведінка не визначена.[^cpp-draft-expr-static-cast]

Перевага для WCET (worst-case execution time) інженерна, а не стандартна: виклик з відомою цільовою функцією простіше аналізувати статично, бо інструменту не треба припускати, куди веде вказівник. Це не гарантує конкретного часу. Він залежить від процесора, компілятора, пам’яті та кешу, тож його треба міряти або аналізувати на цільовій платформі.

Відсутній метод у CRTP дає помилку компіляції, але лише тоді, коли виклик справді інстанціюється: член шаблону інстанціюється, коли його визначення потрібне.[^cpp-draft-temp-inst] Головний компроміс інший. `Base<Adc>` і `Base<Dac>` – різні типи без спільного базового класу, тож їх не покласти в один масив за одним типом вказівника. Для такого потрібен інший механізм, наприклад `std::variant` або type erasure, і він коштує пам’яті чи викликів.

Virtual-диспетчеризація потрібна, коли конкретний тип обирається під час виконання, наприклад драйвер, вибраний з конфігурації. Для малого фіксованого набору типів CRTP або звичайний `switch` зазвичай простіші; рішення варто підтвердити вимірюванням на цільовій платформі.

**Типові помилки:**

- Вважати, що CRTP завжди швидший: він прибирає runtime-диспетчеризацію, але не замінює вимірювання.
- Приводити `static_cast` до `Derived` для об’єкта іншого типу.
- Очікувати, що об’єкти різних `Derived` можна зберігати в одному масиві без спільного базового типу.

## Sources

<!-- generated from frontmatter -->
