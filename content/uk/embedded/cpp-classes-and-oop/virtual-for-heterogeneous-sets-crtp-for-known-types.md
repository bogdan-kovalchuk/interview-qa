---
id: emb-cppoop-0021
title: "CRTP vs virtual: коли що обирати?"
description: "Virtual – гетерогенні колекції (масив Base з різними типами), dispatch у runtime, одна копія base-коду."
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
  - source_id: cpp-draft-expr-call
    title: "C++ working draft: Function call ([expr.call])"
    url: https://eel.is/c++draft/expr.call
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що виклик virtual-функції виконує її final overrider у dynamic type об’єкта; сам механізм (vptr/vtable) стандарт не задає."
  - source_id: cpp-draft-temp-inst
    title: "C++ working draft: Implicit instantiation ([temp.inst])"
    url: https://eel.is/c++draft/temp.inst
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що неявна інстанціація специфікації класового шаблону інстанціює оголошення, але не визначення member-функцій, а специфікація member-функції інстанціюється, коли її визначення потрібне. Про розмір коду не йдеться."
  - source_id: cpp-draft-conv-ptr
    title: "C++ working draft: Pointer conversions ([conv.ptr])"
    url: https://eel.is/c++draft/conv.ptr
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Визначає, що вказівник на похідний клас можна перетворити на вказівник на його базовий клас; про те, які класи є базами, стандарт каже в інших розділах. Про virtual dispatch не йдеться."
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
    accessed: 2026-10-06
    kind: spec
    version: null
    applicability: "Визначає dynamic class (з virtual-функціями чи virtual-базами) як клас, що потребує virtual table pointer; отже клас без них його не потребує. Це ABI, а не стандарт мови: інші ABI можуть відрізнятися в деталях."
  - source_id: gcc-optimize-options
    title: "GCC 16.1.0: Optimize Options"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Optimize-Options.html
    accessed: 2026-10-06
    kind: official
    version: "16.1.0"
    applicability: "Документує -fdevirtualize (спроба перетворити виклики virtual-функцій на прямі; вмикається на -O2, -O3 і -Os) та -fipa-icf (злиття ідентичних функцій; вмикається на -O2 і -Os, ефективніше з LTO). Не гарантує результату для конкретного коду."
---

## Short answer

**Virtual** – гетерогенні колекції (масив `Base*` з різними типами) і dispatch за dynamic type у runtime;[^cpp-draft-expr-call] код base-класу існує в одній копії.

CRTP (Curiously Recurring Template Pattern) – коли типи відомі на етапі компіляції: виклик статичний, а vptr і vtable не потрібні.[^itanium-cxx-abi] Ціна – окрема інстанціація base-коду для кожного похідного типу.[^cpp-draft-temp-inst]

Правило: різні типи в одному контейнері – virtual; відомі типи й помітна вартість dispatch, підтверджена вимірюванням – CRTP.

## Detailed explanation

Virtual обирає реалізацію під час виконання за dynamic type об’єкта.[^cpp-draft-expr-call] Тому він підходить, коли набір типів відкритий: код, що працює через `Base*`, не змінюється, коли з’являється новий похідний клас. Base-клас, який не є шаблоном, існує в одній копії, а плата така: vptr в кожному об’єкті, vtable на клас і непрямий виклик (див. `qid:emb-cppoop-0013`).

CRTP фіксує похідний тип у шаблонному параметрі, тож виклик вирішується під час компіляції (див. `qid:emb-cppoop-0020`). Ціна – base-шаблон інстанціюється для кожного похідного типу, і використані member-функції отримують окремий код.[^cpp-draft-temp-inst] До того ж `SensorBase<Temp>` і `SensorBase<Pressure>` – різні класи без спільного base: вказівник на похідний клас можна перетворити на вказівник на його базовий клас,[^cpp-draft-conv-ptr] але `SensorBase<Pressure>` не є базою `Temp`, тож спільного типу вказівника для масиву немає (докладніше в `qid:emb-cppoop-0022`).

«CRTP швидший» – не закон. GCC на `-O2`, `-O3` і `-Os` намагається devirtualize virtual-виклики, коли може вивести dynamic type, а дублювання коду іноді зменшує Identical Code Folding (`-fipa-icf`, на `-O2` і `-Os`), але лише для функцій, що виявились ідентичними.[^gcc-optimize-options] Тому реальна різниця залежить від коду, ядра й налаштувань збірки: вибирай за вимогами (відкритий чи закритий набір типів) і міряй на цільовій платформі. Якщо потрібен лише спільний код для кількох відомих типів, іноді вистачає звичайної шаблонної функції без спільного base.

Ілюстративний приклад (`SensorBase` – з `qid:emb-cppoop-0020`, `Sensor` – віртуальний інтерфейс; це різні ієрархії):

```cpp
// virtual: відкритий набір типів, вибір за dynamic type
Sensor* all[] = { &v_temp, &v_pressure };
for (Sensor* s : all) s->read();

// CRTP: тип відомий на етапі компіляції, виклик статичний
template <typename D>
std::int16_t poll(SensorBase<D>& s) { return s.read(); }
// poll(c_temp) інстанціюється окремо для кожного D
```

**Типові помилки:**

- Вибирати CRTP «бо швидше» без вимірювання: virtual-виклик можуть devirtualize, а CRTP збільшує код.[^gcc-optimize-options]
- Брати virtual заради гнучкості там, де набір типів фіксований, а RAM під vptr обмежена.
- Очікувати від CRTP гетерогенний контейнер: для нього потрібен спільний base, тобто virtual чи інша форма type erasure.

## Sources

<!-- generated from frontmatter -->
