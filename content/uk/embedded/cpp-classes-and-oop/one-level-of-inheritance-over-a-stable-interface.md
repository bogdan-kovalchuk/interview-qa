---
id: emb-cppoop-0012
title: "Коли успадкування доречне в embedded, а коли – ні?"
description: "Доречне: тонкий інтерфейс над кількома реалізаціями й стабільний контракт; уникай глибоких ієрархій і баз із даними; числа на кшталт 2–5 типів – лише орієнтир."
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
  - source_id: cppcg-c120
    title: "C++ Core Guidelines: C.120 – Use class hierarchies to represent concepts with inherent hierarchical structure (only)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c120-use-class-hierarchies-to-represent-concepts-with-inherent-hierarchical-structure-only
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Настанова: ієрархію класів використовувати лише для понять із внутрішньо ієрархічною структурою; база має точно відповідати всім нащадкам; якщо досить data member, успадкування не використовувати. Числових порогів (кількість типів чи рівнів) не задає."
  - source_id: cppcg-c121
    title: "C++ Core Guidelines: C.121 – If a base class is used as an interface, make it a pure abstract class"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c121-if-a-base-class-is-used-as-an-interface-make-it-a-pure-abstract-class
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Настанова: клас стабільніший, якщо не містить даних; інтерфейс складається з публічних pure virtual функцій і порожнього або default virtual-деструктора; без virtual-деструктора видалення через базу призводить до витоку."
  - source_id: cppcg-c122
    title: "C++ Core Guidelines: C.122 – Use abstract classes as interfaces when complete separation of interface and implementation is needed"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c122-use-abstract-classes-as-interfaces-when-complete-separation-of-interface-and-implementation-is-needed
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Настанова з прикладом Device із write/read: різні реалізації використовуються взаємозамінно через інтерфейс, і їх можна змінювати, поки доступ іде через нього. Це настанова, а не вимога стандарту."
  - source_id: cppcg-c129
    title: "C++ Core Guidelines: C.129 – When designing a class hierarchy, distinguish between implementation inheritance and interface inheritance"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c129-when-designing-a-class-hierarchy-distinguish-between-implementation-inheritance-and-interface-inheritance
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Настанова: розрізняти interface inheritance та implementation inheritance; реалізація й дані в базі роблять інтерфейс крихким (приклад: додавання даних у базу потребує перегляду й перекомпіляції всіх нащадків і користувачів); важливість зростає з розміром ієрархії, її віком і кількістю організацій, що нею користуються. Порогів у цифрах не дає."
  - source_id: itanium-abi-vtable-components
    title: "Itanium C++ ABI: Virtual Table Components and Order"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html#vtable-components
    accessed: 2026-10-06
    kind: spec
    version: null
    applicability: "У розділі 2.5.2 каже, що кожна vtable завжди містить offset-to-top і typeinfo pointer, далі – virtual function pointers для dispatch, а vptr об’єкта містить адресу в vtable. Це ABI, а не стандарт мови; розміру в байтах і секції пам’яті не задає."
---

## Short answer

**Доречне**: один рівень (інтерфейс-база + кілька реалізацій) зі стабільним інтерфейсом, коли різні типи використовують через одну базу, напр. драйвери за спільним `Device`.[^cppcg-c120][^cppcg-c122] <span class="warn">Уникай</span> глибоких ієрархій і баз із даними: зміна такої бази зачіпає всіх нащадків,[^cppcg-c129] а кожен поліморфний клас додає vtable, а кожен об’єкт – vptr.[^itanium-abi-vtable-components] Числа «2–5 типів» чи «3+ рівні» – лише орієнтири; для типів, відомих на етапі компіляції, достатньо композиції.

Правило: успадкування – для інтерфейсу, усе інше – композиція.[^cppcg-c120]

## Detailed explanation

Успадкування в C++ дає одне, чого не дає композиція: через посилання чи вказівник на базу можна однаково працювати з різними типами, а виклик піде в потрібну реалізацію під час виконання. У embedded це типовий шаблон для драйверів і HAL: різні реалізації за спільним інтерфейсом, як `Device` із `write` і `read` у Core Guidelines, де реалізації взаємозамінні й їх можна змінювати, поки весь доступ іде через інтерфейс.[^cppcg-c122] Інтерфейс найстабільніший, коли складається лише з публічних pure virtual функцій і virtual-деструктора, без даних.[^cppcg-c121] Саме це й описує «один рівень над стабільним інтерфейсом».

Ціна цієї гнучкості конкретна. За Itanium C++ ABI кожна vtable містить offset-to-top і typeinfo pointer та вказівники на virtual-функції, а об’єкт тримає vptr з адресою в ній;[^itanium-abi-vtable-components] отже, пам’ять витрачається на vtable кожного поліморфного класу й на один вказівник у кожному об’єкті, а virtual-виклик іде через vptr, тобто опосередковано. Скільки це важить на твоєму таргеті, показують map-файл і вимірювання, а не правило; деталі розкладки див. `qid:emb-cppoop-0013`.

Чому глибокі ієрархії й бази з даними – проблема, пояснює C.129: реалізація й дані в базі роблять інтерфейс крихким, бо, наприклад, додавання даних у базу потребує перегляду й перекомпіляції всіх нащадків і всього коду, що її використовує; важливість різниці між interface inheritance та implementation inheritance зростає з розміром ієрархії, її віком і кількістю організацій, що нею користуються.[^cppcg-c129] Прошивки часто живуть довго, тож ця вада тут відчутна. Числових порогів ні C.129, ні C.120 не дають: «2–5 типів» і «3+ рівні» з первинної відповіді – евристики, а не правила. Суть у тому, що база точно відповідає всім нащадкам, а якщо досить поля, успадкування не потрібне.[^cppcg-c120] Коли типи відомі на етапі компіляції, замість vptr можна взяти шаблони чи CRTP (див. `qid:emb-cppoop-0021`).

```cpp
class Transport {                              // interface: pure virtual functions, no data
public:
    virtual ~Transport() = default;
    virtual bool send(const std::uint8_t* data, std::size_t n) = 0;
};

class Uart final : public Transport { /* ... */ };
class Spi  final : public Transport { /* ... */ };

bool log_frame(Transport& out, const std::uint8_t* frame, std::size_t n) {
    return out.send(frame, n);                 // works with any transport
}
```

Фрагмент ілюстративний: `Uart` і `Spi` мають перевизначити `send` з `override`.

**Типові помилки:**

- Успадковувати заради повторного використання коду (наприклад, `Led : Gpio`), коли досить поля-члена.[^cppcg-c120]
- Класти в базу дані й не-pure реалізацію: така база крихка.[^cppcg-c129]
- Забути virtual-деструктор в інтерфейсі, коли об’єкти видаляють через базу: це undefined behavior, а на практиці зазвичай не виконується деструктор похідного класу.[^cppcg-c121] Про вплив virtual-деструктора на глобальні об’єкти див. `qid:emb-cppoop-0009`.
- Сприймати «2–5 типів» чи «3 рівні» як закон і не міряти реальну ціну на цільовій платформі.

## Sources

<!-- generated from frontmatter -->
