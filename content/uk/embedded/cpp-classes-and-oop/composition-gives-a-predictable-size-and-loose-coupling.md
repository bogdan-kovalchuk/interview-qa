---
id: emb-cppoop-0024
title: "Які переваги композиції в embedded?"
description: "Передбачуваний розмір, гнучка підміна, слабке зчеплення."
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
  - source_id: cpp-draft-expr-sizeof
    title: "C++ working draft: [expr.sizeof] Sizeof"
    url: https://eel.is/c++draft/expr.sizeof
    accessed: 2026-10-06
    kind: spec
    version: "working draft"
    applicability: "Каже, що для класу sizeof дає кількість байтів в об’єкті цього класу разом із padding, потрібним для розміщення таких об’єктів у масиві, і що кількість та розташування padding визначає реалізація. Конкретних значень не дає."
  - source_id: iso-tr-18015
    title: "ISO/IEC TR 18015:2006 Technical Report on C++ Performance"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/TR18015.pdf
    accessed: 2026-10-06
    kind: spec
    version: "TR 18015:2006"
    applicability: "У розділі 5.3.1 каже, що клас без virtual-функції займає стільки ж місця, скільки struct з тими самими даними (поза можливим padding), що non-virtual функція не займає місця в об’єкті, а поліморфний клас платить одним вказівником на об’єкт плюс таблицею на клас. Звіт 2006 року: конкретні розміри залежать від реалізації."
  - source_id: cppcg-c120
    title: "C++ Core Guidelines: C.120 – Use class hierarchies to represent concepts with inherent hierarchical structure (only)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c120-use-class-hierarchies-to-represent-concepts-with-inherent-hierarchical-structure-only
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Настанова: ієрархію класів використовувати лише для понять із внутрішньо ієрархічною структурою; називає успадкування тісним зчепленням і радить не використовувати його, коли досить data member. Числових порогів не задає."
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
---

## Short answer

**Передбачуваний розмір, гнучка підміна, слабке зчеплення.** Клас без virtual-функцій займає стільки ж місця, скільки struct з тими самими полями, тож член-компонент додає лише власний розмір і padding, без vptr.[^iso-tr-18015] Підміна можлива в runtime через вказівник чи посилання на інтерфейс, де різні реалізації взаємозамінні,[^cppcg-c122] або на етапі компіляції через параметр шаблону. Успадкування натомість дає тісне зчеплення з базою.[^cppcg-c120]

## Detailed explanation

Розмір об’єкта, що містить компоненти як члени за значенням, відомий на етапі компіляції: `sizeof` класу – це кількість байтів в об’єкті разом із padding, а скільки його і де, визначає реалізація.[^cpp-draft-expr-sizeof] Нижня межа – сума розмірів членів. Клас без virtual-функцій не платить за поліморфізм: за TR 18015 його об’єкт займає стільки ж місця, скільки struct з тими самими даними, а non-virtual метод у об’єкті місця не займає.[^iso-tr-18015] Звідси «передбачуваний розмір»: такий об’єкт можна покласти статично (у `.bss` чи `.data`) без heap, а його розмір можна перевірити на етапі компіляції через `static_assert`.

Важливе уточнення: це перевага не над будь-яким успадкуванням, а над поліморфною ієрархією. Non-virtual база теж не додає vptr. Поліморфний клас платить одним вказівником на об’єкт плюс таблицею на клас.[^iso-tr-18015] Тому твердження «композиція дає менший розмір» правильне лише в порівнянні з virtual-ієрархією; про вартість vptr і vtable докладніше в `qid:emb-cppoop-0013`.

Підміна компонента має дві форми з різною ціною. У runtime клас тримає вказівник чи посилання на інтерфейс, і різні реалізації взаємозамінні, поки доступ іде через нього;[^cppcg-c122] ціна – virtual-виклик і vptr у самому компоненті. На етапі компіляції компонент задається параметром шаблону: vptr немає, але кожна комбінація типів дає окремий код (порівняння – в `qid:emb-cppoop-0035`). Зчеплення слабшає саме тоді, коли між класом і компонентом стоїть інтерфейс чи параметр: Core Guidelines називають успадкування тісним зчепленням,[^cppcg-c120] а дані й реалізація в базі роблять інтерфейс крихким: зміна бази потребує перегляду й перекомпіляції нащадків і користувачів.[^cppcg-c129]

```cpp
// Ілюстративний фрагмент.
#include <cstdint>
#include <type_traits>

struct Gpio  { std::uint32_t pin; void set(bool on); };
struct Timer { std::uint16_t period; };

class Blinker {                 // композиція: компоненти – члени за значенням
public:
    void tick();
private:
    Gpio  led_;
    Timer timer_;
};

static_assert(!std::is_polymorphic_v<Blinker>);                    // vptr немає
static_assert(sizeof(Blinker) >= sizeof(Gpio) + sizeof(Timer));    // не менше суми членів
```

**Типові помилки:**

- Подавати «передбачуваний розмір» як перевагу над будь-яким успадкуванням: non-virtual база теж без vptr, виграш лише проти поліморфної ієрархії.
- Підміняти компонент через virtual-інтерфейс і не рахувати vptr та непрямий виклик у кожному компоненті.
- Тримати компонент за вказівником на heap там, де вистачило б члена за значенням.
- Вважати, що композиція сама по собі дає слабке зчеплення: клас, що тримає конкретний тип, залежить від нього.

## Sources

<!-- generated from frontmatter -->
